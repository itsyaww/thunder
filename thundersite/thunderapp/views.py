from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import Http404
from thunderapp.models import Member
from django.db import IntegrityError

appname = "Thunder"

@csrf_exempt
def home(request):
    return render(request, 'thunderapp/base.html', {})


def index(request):
    context = { 'appname': appname }
    return render(request,'thunderapp/index.html',context)


def signup(request):
    context = { 'appname': appname }
    return render(request,'thunderapp/signup.html',context)


def login(request):
    if not ('username' in request.POST and 'password' in request.POST):
        context = { 'appname': appname }
        return render(request,'thunderapp/login.html',context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try: member = Member.objects.get(username=username)
        except Member.DoesNotExist: raise Http404('User does not exist')
        if member.check_password(password):
            # remember user in session variable
            request.session['username'] = username
            request.session['password'] = password
            context = {
                'appname': appname,
                'username': username,
                'loggedin': True
            }
            response = render(request, 'thunderapp/login.html', context)
            # remember last login in cookie
            now = D.datetime.utcnow()
            max_age = 365 * 24 * 60 * 60  #one year
            delta = now + D.timedelta(seconds=max_age)
            format = "%a, %d-%b-%Y %H:%M:%S GMT"
            expires = D.datetime.strftime(delta, format)
            response.set_cookie('last_login',now,expires=expires)
            return response
        else:
            raise Http404('Wrong password')


def register(request):
    if 'username' in request.POST and 'password' in request.POST:
        u = request.POST['username']
        p = request.POST['password']
        user = Member(username=u)
        user.set_password(p)
        try: user.save()
        except IntegrityError: raise Http404('Username '+u+' already taken: Usernames must be unique')
        context = {
            'appname' : appname,
            'username' : u
        }
        return render(request,'thunderapp/user-registered.html',context)

    else:
        raise Http404('POST data missing')