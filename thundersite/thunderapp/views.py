from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from thunderapp.models import Member
from django.db import IntegrityError

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
            return render(request,'thunderapp/index.html',{})
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

def matchlist(request):
    context = { 'appname': appname }
    return render(request,'thunderapp/matchlist.html',context)

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
        try:
            Member.objects.create(username=u,password=p,gender=g,dateOfBirth=d,email=e)

        except IntegrityError:
            raise Http404('Username '+u+' already taken: Usernames must be unique')

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
