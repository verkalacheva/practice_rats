from .views import *
from django.urls import path, include

urlpatterns = [
    path('offers/list', OfferView.as_view({'get': 'list'}), name='all-offers'),
    path('offers/get/<int:id_from>/', OfferView.as_view({'get': 'retrieve_from'}), name='offers-from-user'),
    path('offers/get/<int:id_to>/', OfferView.as_view({'get': 'retrieve_to'}), name='offers-to-user'),
    path('offers/get/<int:id_status>/', OfferView.as_view({'get': 'retrieve_status'}), name='offers-by-status'),
    path('offers/create', OfferView.as_view({'post': 'create'}), name='create-offer'),
    path('offers/delete/<int:id>', OfferView.as_view({'delete': 'destroy'}), name='delete-offer')
]