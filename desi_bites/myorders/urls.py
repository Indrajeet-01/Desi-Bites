# urls.py
from django.urls import path
from .views import checkout, place_order

urlpatterns = [
    path('checkout', checkout, name='checkout'),
    path('place_order', place_order, name='place_order'),
    
]