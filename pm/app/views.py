from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from app.models import Passmanager 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        obj=Passmanager.objects.filter(user=request.user)
        return render(request,'home.html',{'obj':obj})
    else:
        messages.success(request,"please login !!")
        return redirect('login')



def mlogin(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    return render(request,'login.html',{'form':form})

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user registered successfully")
            return redirect('login')
    return render(request,'signup.html',{'form':form})



def signout(request):
    logout(request)
    messages.success(request,"User logged out successfully")
    return redirect('login')


@login_required()
def add(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        site=request.POST['site']
        
        if not Passmanager.objects.filter(user=request.user).filter(site=site).exists():
            pm=Passmanager(username=username,password=password,site=site,user=request.user)
            pm.save()
            return redirect('home')
        else:
            messages.success(request,"This Site has already been added")
    

    return render(request,'add.html')



def mdelete(request,id):
    obj=Passmanager.objects.get(pk=id)
    obj.delete()
    messages.success(request,"Deleted Successfully")

    return redirect('home')


def update(request,id):
    obj=Passmanager.objects.get(pk=id)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        site=request.POST['site']
        obj.username=username
        obj.password=password
        obj.site=site
        obj.save()
        messages.success(request,"Updated Successfully")
        return redirect('home')
        
    return render(request,'update.html',{'obj':obj})
        
