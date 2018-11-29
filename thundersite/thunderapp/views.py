from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.utils import timezone
from thunderapp.models import Member, Message
from django.db import IntegrityError
from django.db.models import Q

from thunderapp.templatetags.extras import display_message

appname = "Thunder"

# decorator that tests whether user is logged in
def loggedin(view):
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Member.objects.get(username=username)
            except Member.DoesNotExist: raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request,'thunderapp/not-logged-in.html',{})
    return mod_view

@csrf_exempt
def home(request):
    return render(request, 'thunderapp/base.html', {})


def index(request):
    context = { 'appname': appname }
    return render(request,'thunderapp/index.html',context)

@csrf_exempt
def signup(request):
    context = { 'appname': appname }
    return render(request,'thunderapp/signup.html',context)

@csrf_exempt
def profile(request,member_id):
    member = get_object_or_404(Member, pk=member_id)
    context = {'member': member}
    return render(request, 'thunderapp/profile.html', context)

def matchlist(request, member_id):
    currentMember = get_object_or_404(Member, pk=member_id)
    matches = []
    followers = Member.objects.filter(following__pk=member_id)

    for member in currentMember.following.all():
        if member in followers:
            matches.append(member)

    matchRank = []

    for match in matches:
        count = 0
        for hobby in currentMember.hobbies.all():
            if hobby in match.hobbies.all():
                count += 1
        matchRank.append(count)

    insertionSort(matches, matchRank)

    context = {'currentMember': matches}
    return render(request,'thunderapp/matchlist.html', context)


def messages(request):
    context = { 'appname': appname }
    return render(request,'thunderapp/messages.html',context)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        g = request.POST.get('gender')
        d = request.POST.get('DofB')
        e = request.POST.get('email')
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')

        try:
            Member.objects.create(username=u,password=p,gender=g,dateOfBirth=d,email=e,firstName=fn,lastName=ln)

        except IntegrityError:
            raise Http404('Invalid value in field')

        return HttpResponse()
    else:
        raise Http404('POST data missing')

@csrf_exempt
def upload_image(request,member_id):
    profileimage = request.FILES.get('profileimage')

    m = get_object_or_404(Member,id=member_id)

    m.profileImage = profileimage
    m.save()
    return HttpResponse()

@loggedin
def friends(request,user):
    # # list of people user is following
    # following = user.following.all()
    # # list of people that are following me
    # followers = Member.objects.filter(following__username=user.username)
    # # render reponse
    # context = {
    #     'appname': appname,
    #     'username': user.username,
    #     'members': members,
    #     'following': following,
    #     'followers': followers,
    #     'loggedin': True
    # }
    return render(request, 'mainapp/friends.html', context)


# view function that responses to Ajax requests on login/register pages

@csrf_exempt
def checkuser(request):
    if 'username' in request.POST:
        try:
            member = Member.objects.get(username=request.POST['username'])
        except Member.DoesNotExist:
            if request.POST['page'] == 'login':
                return HttpResponse("<span class='taken'>&nbsp;&#x2718; Invalid username</span>")
            if request.POST['page'] == 'register':
                return HttpResponse("<span class='available'>&nbsp;&#x2714; This username is available</span>")
    if request.POST['page'] == 'login':
        return HttpResponse("<span class='available'>&nbsp;&#x2714; Valid username</span>")
    if request.POST['page'] == 'register':
        return HttpResponse("<span class='taken'>&nbsp;&#x2718; This username is taken</span>")
    return HttpResponse("<span class='taken'>&nbsp;&#x2718; Invalid request</span>")
@loggedin
def post_message(request, user):
    if request.method=='POST' and 'recip' in request.POST:
        recip = request.POST['recip']
        try: recip_user = Member.objects.get(username=recip)
        except Member.DoesNotExist: raise Http404('Member does not exist')
        text = request.POST['text']
        pm = request.POST['pm'] == '0'
        message = Message(sender=user,recip=recip_user,public=pm,time=timezone.now(),text=text)
        message.save()
        return HttpResponse(display_message(message, user.username))
    else:
        raise Http404('POST not used, or recip missing in POST request')


@loggedin
def erase_message(request, user):
    if 'id' in request.POST:
        msg_id = request.POST['id']
        try: message = Message.objects.get(id=msg_id)
        except Message.DoesNotExist: raise Http404('Message does not exist')
        # Check if user has permission to delete message
        if message.sender==user or message.recip==user:
            message.delete()
            return HttpResponse('message deleted')
        else:
            raise Http404('User does not have permission to delete message')
    else:
        raise Http404('Missing id in POST')


@csrf_exempt
def login(request):
    if not ('loginusername' in request.POST and 'loginpassword' in request.POST):
        context = { 'appname': appname }
        return render(request,'thunderapp/login.html',context)
    else:
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        correctpassword = None
        mid = None
        try:
            member = Member.objects.get(username=username)
            mid = member.id
            correctpassword = member.password
        except Member.DoesNotExist:
            Http404('Username/password is incorrect')

        if password == correctpassword:
            # remember user in session variable
            request.session['username'] = username
            request.session['password'] = password
            context = {
                'appname': appname,
                'username': username,
                'loggedin': True
            }
            response = JsonResponse({"redirect":True,"redirect_url":"http://127.0.0.1:8000/profile/"+str(mid)})
            # remember last login in cookie
            now = D.datetime.utcnow()
            max_age = 365 * 24 * 60 * 60  #one year
            delta = now + D.timedelta(seconds=max_age)
            format = "%a, %d-%b-%Y %H:%M:%S GMT"
            expires = D.datetime.strftime(delta, format)
            response.set_cookie('last_login',now,expires=expires)
            return response
        else:
            raise Http404('Username/password is incorrect')


def insertionSort(matchList, matchRank):
    for i in range(len(matchList)):
        insert(matchRank[i], matchRank, i, matchList, matchList[i])

def insert(k, matchRank, hi, matchList, member):
    for i in range(hi, 0, -1):
        if k < matchRank[i - 1]:
            matchRank[i] = k
            matchList[i] = member
            return
        else:
            matchRank[i] = matchRank[i - 1]
            matchList[i] = matchList[i - 1]
    matchRank[0] = k
    matchList[0] = member


