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

    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_profile(cls,id,new_name):
        cls.objects.filter(id=id).update(user = new_name)

    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all()
        return profile

    def __str__(self):
        return f'{self.user.username} Profile'

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length = 60)
    hood_location = models.CharField(max_length = 60)
    family_size = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='neighbourhoods', null=True)

    class Meta:
    
        ordering = ['pub_date']

    def save_hood(self):
        self.save() 

    @classmethod
    def delete_hood(cls,id):
        cls.objects.filter(id).delete()
    @classmethod
    def update_hood(cls,id,new_name):
        cls.objects.filter(id=id).update(hood_name = new_name)

    @classmethod
    def update_family_count(cls,id,new_occupant):
        cls.objects.filter(id=id).update(family_size =new_occupant)

    @classmethod
    def search_hood(cls, search_term):
        hood = cls.objects.filter(hood_name__icontains=search_term)
        return hood

    def __str__(self):
        return self.hood_name

class Business(models.Model):
    biz_name = models.CharField(max_length = 60)
    biz_email = models.EmailField()
    biz_description = models.TextField()
    biz_digits = models.IntegerField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    hood_ref = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='businesses', null=True)

    class Meta:
    
        ordering = ['pub_date']

    def save_business(self):
        self.save()

    @classmethod
    def delete_business(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_business(cls,id,new_name):
        cls.objects.filter(id=id).update(biz_name = new_name)

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

    def __str__(self):
        return self.police_station