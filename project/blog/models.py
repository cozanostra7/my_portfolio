from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=250,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(null=True, blank=True, default='salems.png')
    description =models.TextField(blank=True,null=True)
    demo_link = models.CharField(max_length=250,null=True,blank=True)
    tags = models.ManyToManyField('Tags',blank=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=250,null=True,blank=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
       return self.name




class Tags(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=250,null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(null=True,blank=True,default='salems.png')
    location =models.CharField(max_length=250,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    short_intro = models.CharField(max_length=250,null=True,blank=True)




    def __str__(self):
       return self.name


class Messages(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.TextField()