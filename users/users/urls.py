from django.urls import path, re_path
from .views import RegisterView, LoginView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^register/$', csrf_exempt(RegisterView.as_view({'post': 'register', 'get': 'register'})), name='register'),
    re_path(r'^login/$', csrf_exempt(LoginView.as_view({'get': 'user_login', 'post': 'user_login'})), name='login'),
    path('users/profile/<str:username>', ProfileView.as_view({'get': 'get_user_profile'}), name='profile'),
]