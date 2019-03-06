from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def home(request):
    return render(request,'index.html')


def map(request):
    return render(request,'map.html')

def signup(request):
    if request.method=="POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user( username=request.POST['username'],password=request.POST['password'])
            auth.login(request,user)
            return redirect('blog')
    return render(request, 'signup.html')