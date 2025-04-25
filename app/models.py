from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)


class Post(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null = True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null = True,blank=True)


class Images(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="images")
    img = models.ImageField(upload_to='img/')

