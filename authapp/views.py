from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout
from .forms import SignupForm
from .models import Signup


# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        #logincheck=authenticate(username=unm,password=pas)
        logincheck=Signup.objects.filter(username=unm,password=pas)
        if logincheck:
            print('Login Successfully!')
            request.session['username']=unm
            return redirect('home')
        else:
            print('Error...Somthing ewnt wrong!')
    else:
        pass
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newform=SignupForm(request.POST)
        if newform.is_valid():
            newform.save()
            request.session['username']=Signup.objects.get('username')
            print("Signup Successfully!")
            return redirect('home')
        else:
            print('Error')
    else:
        newform=SignupForm()
    return render(request,'signup.html',{'newform':newform})

def home(request):
    usernm=request.session.get('username')
    return render(request,'home.html',{'usernm':usernm})

def user_logout(request):
    logout(request)
    return redirect('index')
