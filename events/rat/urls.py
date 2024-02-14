"""
URL configuration for rat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Events Users",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
path('events/list', EventView.as_view({'get': 'list'}), name='all-events'), # вывести все заявки из таблицы
path('events/get/<int:id_user>/', EventView.as_view({'get': 'get_by_user'}), name='events-by-user'), #вывести все мероприятия от человека по его айди
path('events/get/<int:id>', EventView.as_view({'get': 'get_by_id'}), name='events-by-id'), # вывести мероприятие по айди
path('events/get/<str:id_status>', EventView.as_view({'get': 'get_by_id_status'}), name='events-by-id-status'), # вывести все мероприятия по айди статуса
path('events/create', EventView.as_view({'post':'create'}), name='create'), #создать мероприятие
path('offers/delete/<int:id>', EventView.as_view({'delete':'destroy'}), name='delete-event'),#удалить мероприятие по его айди

]
