from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from thunderapp.models import Member
from django.db import IntegrityError

appname = "Thunder"

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

def matchList(request):
    context = { 'appname': appname }
    return render(request,'thunderapp/matchList.html',context)

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
