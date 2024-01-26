from django.shortcuts import render
from menu.models import MenuItem

def index(request):
    return render(request, 'index.html')

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def singleBlog(request):
    return render(request, 'blog-single.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
# Create your views here.
