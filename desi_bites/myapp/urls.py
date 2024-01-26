from django.urls import path
from .views import index,about, blog, services, contact, singleBlog, menu

urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu' ),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog/blog-single.html', singleBlog, name='singleBlog'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact')
] 