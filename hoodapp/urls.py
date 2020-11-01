from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('upload_post/', views.upload_post, name='upload_post'),
    path('business/', views.business, name='business'),
    path('upload_business/', views.upload_business, name='upload_business'),
    path('search/', views.search_results, name='search_results'),
    path('services/', views.services, name='services'),
]