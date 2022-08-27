from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from app.models import Passmanager 

# Create your views here.

def home(request):
    obj=Passmanager.objects.filter(user=request.user)
    return render(request,'home.html',{'obj':obj})



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
            return redirect('login')
    return render(request,'signup.html',{'form':form})



def signout(request):
    logout(request)
    return redirect('login')



def add(request,id):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        site=request.POST['site']
        
        if not Passmanager.objects.filter(user=request.user).filter(site=site).exists():
            pm=Passmanager(username=username,password=password,site=site,user=request.user)
            pm.save()
            return redirect('home')
    

    return render(request,'add.html')



def delete(request,id):
    obj=Passmanager.objects.get(pk=id)
    obj.delete()
    return redirect('home')


def update(request,id):
    obj=Passmanager.objects.get(pk=id)
    if request.method=='POST':
        obj.delete()
        username=request.POST['username']
        password=request.POST['password']
        site=request.POST['site']
        pm=Passmanager(username=username,password=password,site=site,user=request.user)
        pm.save()
        return redirect('home')
        
    return render(request,'update.html',{'obj':obj})
        




    
    
        

    

