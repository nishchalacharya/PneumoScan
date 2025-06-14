from django.db import models
from loginapp.models import *

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime  

now =  datetime.now()
time = now.strftime("%d %B %Y")


# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=600)
    image = models.ImageField(upload_to='blog_images/posts',blank=True,null=True)
    content = models.CharField(max_length=100000)
    time = models.CharField(default=time,max_length=100, blank=True)
    likes = models.IntegerField(null=True,blank=True,default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str( self.postname)
    
    
class Comment(models.Model):
    content = models.CharField(max_length=200)
    time = models.CharField(default=time,max_length=100, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return  f"{self.id}.{self.content[:20]}..."
    
    
