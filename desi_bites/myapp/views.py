from django.shortcuts import render , get_object_or_404
from menu.models import MenuItem

def index(request):
    return render(request, 'index.html')

def menu(request):
    categories = ['Starter', 'Lunch','Dinner', 'Desserts', 'Drinks','fast_food']
    menu_items = MenuItem.objects.all()
    context = {'categories': categories, 'menu_items': menu_items}
    return render(request, 'menu.html', context)

def singleItem(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    context = {'item': item}
    return render(request, 'product-single.html', context)

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def singleBlog(request):
    return render(request, 'blog-single.html')

def services(request):
    return render(request, 'services.html')

def reserve(request):
    return render(request, 'reserve.html')
# Create your views here.
