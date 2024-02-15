from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login

class RegisterView(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    @swagger_auto_schema(tags=["Registration"])
    def register(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                # Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
                # Save the User object
                new_user.save()
                profile_serializer = ProfileSerializer(data=request.data)
                if profile_serializer.is_valid():
                    profile_data = {'user': new_user.id, 'role': 'bookcrosser'}
                    profile_serializer = ProfileSerializer(data=profile_data)
                    if profile_serializer.is_valid():
                        profile_serializer.save()
               
                return render(request, 'users/register_done.html', {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
        return render(request, 'users/register.html', {'user_form': user_form})

class LoginView(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    @swagger_auto_schema(tags=["Authorization"])
    def user_login(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse('Authenticated successfully')
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileDetailSerializer
    @swagger_auto_schema(tags=["Profile"])
    def get_user_profile(self, request, *args, **kwargs):
        data = list(User.objects.filter(username=kwargs['username']).values_list('id'))
        profile_data = list(Profile.objects.filter(user_id__in=data).values())
        return Response(profile_data)