from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
import datetime as dt

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    profile_photo = CloudinaryField('profile_photo', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length = 60)
    hood_location = models.CharField(max_length = 60)
    hood_pic = CloudinaryField('hood_pic', null=True)
    hood_description = models.TextField()
    occupant_count = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='neighbourhoods', null=True)

    class Meta:
    
        ordering = ['pub_date']

    @classmethod
    def update_occupant_count(cls,id,new_occupant):
        cls.objects.filter(id=id).update(occupant_count =new_occupant)


class Business(models.Model):
    biz_name = models.CharField(max_length = 60)
    biz_email = models.EmailField()
    biz_description = models.TextField()
    biz_digits = models.IntegerField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    hood_ref = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='businesses', null=True)

    class Meta:
    
        ordering = ['pub_date']

    @classmethod
    def search_business(cls, search_term):
        biz = cls.objects.filter(biz_name__icontains=search_term)
        return biz

    
    def __str__(self):
        return self.biz_name

class Post(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', null=True)
    hood_ref = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='posts', null=True)


    class Meta:
    
        ordering = ['pub_date']
    
    def __str__(self):
        return self.title

class Services(models.Model):
    police_station = models.CharField(max_length = 60,blank = True)
    police_no = models.IntegerField(10,blank = True)
    hospital_name = models.CharField(max_length = 60,blank = True)
    hospital_no = models.IntegerField(10,blank = True)
    firedpt_name = models.CharField(max_length = 60,blank = True)
    firedpt_no = models.IntegerField(10,blank = True)
    hood_ref = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='services', null=True)
