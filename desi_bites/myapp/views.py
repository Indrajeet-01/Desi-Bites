from django.shortcuts import render , get_object_or_404, redirect
from django.http import JsonResponse
from menu.models import MenuItem
from decimal import Decimal
import json
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def index(request):
    return render(request, 'index.html')

def menu(request):
    categories = ['Starter', 'Lunch','Dinner', 'Desserts', 'Drinks','fast_food']
    menu_items = MenuItem.objects.all()
    context = {'categories': categories, 'menu_items': menu_items}
    return render(request, 'menu.html', context)

def add_to_cart(request, item_id):
    # Ensure the 'cart' key is initialized in the session
    if 'cart' not in request.session:
        request.session['cart'] = {}
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        item = MenuItem.objects.get(pk=item_id)
        cart = request.session['cart']
        if item_id in cart:
            cart[item_id]['quantity'] += quantity
        else:
            cart[item_id] = {
                'image': item.image,
                'name': item.name,
                'quantity': quantity,
                'price': float(item.price)
                }
        request.session.modified = True
        return redirect('view_cart')
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

def view_cart(request):
    cart = request.session.get('cart', {})
    # Convert the Decimal to float when calculating the total
    for item_data in cart.values():
        item_data['total'] = float(item_data['quantity']) * float(item_data['price'])
    total = sum(item_data['total'] for item_data in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total': total})

def remove_from_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if 'cart' in request.session:
            cart = request.session['cart']
            if item_id in cart:
                del cart[item_id]
                request.session.modified = True
                return redirect('view_cart')
    return JsonResponse({'success': False, 'error': 'Invalid request'})

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
