from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by("-updated_at")
        if request.method == "POST": 
            title = request.POST.get('title')
            content = request.POST.get('content')
            images = request.FILES.getlist('images')
            
            if title == "" or content == "": 
                return redirect('/')
            post = Post.objects.create(title = title ,content= content,user = request.user)
            for image in images: 
                Images.objects.create(post =post,img=image)

            # Images.objects.bulk_create([
            #         Images(post=post, img=image) for image in images
            # ])

            return redirect('/')
        return render(request,'index.html',{"posts":posts})
    else:
        return redirect('/login')




def profileDetail(request,username): 
    try :
        user = User.objects.get(username = username) #bisesh
        profile = Profile.objects.get(user = user)

         #bisesh ko profile 

    except: 
        return render(request,'404.html')
    context = { 
        'profile':profile
    }
    
    return render(request,'detailpage.html',context)
    

def postdetail(request,id): 
    try : 
        post = Post.objects.get(id = id)
        # images = post.images_set.all() if there is no related name # object_set
        #images = post.images.all()
        images = Images.objects.select_related('post').filter(post=post) #optimized


    except: 
        return render(request,'404.html')

    return render(request,'postdetail.html',{'post':post,'images':images})



def Postdelete(request,id): 
    try : 
        post = Post.objects.get(id = id)
        

    except: 
        return render(request,'404.html')
    
    post.delete()


    return redirect('/')







def update(request,id): 

    try : 
        post = Post.objects.get(id = id)

    except: 
        return render(request,'404.html')
    if request.method == "POST": 
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title == "" or content == "": 
            return redirect('/')
        post.title = title
        post.content = content
        post.save()
        return redirect('/')

    
    return render(request,'update.html',{'post':post})
    




def login_view(request): 
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            user = authenticate(username=username, password=password)

            if user:
                login(request,user=user)
                return redirect('/')
            else: 
                return redirect('/login')
                
        return render(request,'login.html')
    else:
        return redirect('/')




def logout_view(request): 
    logout(request)
    return redirect('/login')