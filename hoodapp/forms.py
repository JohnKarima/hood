from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Business, Services, Neighbourhood

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']

class PostUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post']

    def form_valid(self, form):
        form.instance.user = self.request.profile
        return super().form_valid(form)

class BizUploadForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['biz_name', 'biz_description', 'biz_digits', 'biz_email' ]

    def form_valid(self, form):
        form.instance.user = self.request.profile
        return super().form_valid(form)

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['hood_name', 'hood_location', 'family_size']

    def form_valid(self, form):
        form.instance.user = self.request.profile
        return super().form_valid(form)