from django.urls import path
from .views import index,about, blog, services, reserve, singleBlog, menu, singleItem, cart

urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu' ),
    path('menu/<int:item_id>/', singleItem, name='singleItem'),
    path('cart/', cart, name='cart'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog/blog-single.html', singleBlog, name='singleBlog'),
    path('services/', services, name='services'),
    path('reserve/', reserve, name='reserve')
] 