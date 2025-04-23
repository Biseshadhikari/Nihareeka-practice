from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.method =="POST": 
        print(request.POST.get('username'))
    students = Profile.objects.all()
    context = { 
        "students":students
    }
    return render(request,'index.html',context)




def profileDetail(request,username): 
    try :
        user = User.objects.get(username = username) #bisesh
        profile = Profile.objects.get(user = user) #bisesh ko profile 

    except: 
        return render(request,'404.html')
    context = { 
        'profile':profile
    }
    
    return render(request,'detailpage.html',context)
    

def contact(request): 
    return render(request,'contact.html')