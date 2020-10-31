from django.contrib import admin
from .models import Profile, Neighbourhood, Business, Post, Services

admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Services)