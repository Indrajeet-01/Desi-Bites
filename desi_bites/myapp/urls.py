from django.urls import path
from .views import index,about, blog, services, reserve, singleBlog, menu, singleItem, cart, checkout, add_to_cart, view_cart, remove_from_cart

urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu' ),
    path('menu/<int:item_id>/', singleItem, name='singleItem'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog/blog-single.html', singleBlog, name='singleBlog'),
    path('services/', services, name='services'),
    path('reserve/', reserve, name='reserve')
] 