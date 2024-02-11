from django.contrib import admin

#Registering models
from .models import Profile

admin.site.register(Profile)
