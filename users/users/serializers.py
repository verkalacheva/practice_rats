from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
         model = Profile
         fields = ['user', 'description', 'role']

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ['email', 'password', 'username']
         extra_kwargs = {'password': {'write_only': True}}

     def create(self, validated_data):
         user = User.objects.create_user(**validated_data)
         return user

class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'password2')

class LoginSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ['username', 'password']