from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by("-updated_at")

    return render(request,'index.html',{"posts":posts})




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
    

def postdetail(request,id): 
    try : 
        post = Post.objects.get(id = id)



    except: 
        return render(request,'404.html')

    return render(request,'postdetail.html',{'post':post})