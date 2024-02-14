from django.urls import path, re_path
from .views import *

urlpatterns = [
path('events/list', EventView.as_view({'get': 'list'}), name='all-events'), # вывести все заявки из таблицы
path('events/get/<int:id_user>/', EventView.as_view({'get': 'get_by_user'}), name='events-by-user'), #вывести все мероприятия от человека по его айди
path('events/get/<int:id>', EventView.as_view({'get': 'get_by_id'}), name='events-by-id'), # вывести мероприятие по айди
path('events/get/<str:id_status>', EventView.as_view({'get': 'get_by_id_status'}), name='events-by-id-status'), # вывести все мероприятия по айди статуса
path('events/create', EventView.as_view({'post':'create'}), name='create'), #создать мероприятие
path('offers/delete/<int:id>', EventView.as_view({'delete':'destroy'}), name='delete-event'),#удалить мероприятие по его айди

]