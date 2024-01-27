from django.urls import path
from .views import BookingsCreateView

urlpatterns = [
    path('table', BookingsCreateView.as_view(),name='bookings-create'),
    # Add other URLs as needed
]