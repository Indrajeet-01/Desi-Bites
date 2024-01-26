from django.urls import path
from .views import MenuItemListCreateView, MenuItemDetailView

urlpatterns = [
    path('menu', MenuItemListCreateView.as_view(), name='menu'),
    path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item')
]