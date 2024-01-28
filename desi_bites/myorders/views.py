# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import UserOrder, UserOrderItem
from menu.models import MenuItem

def checkout(request):
    # Retrieve cart details and total from the session
    cart = request.session.get('cart', {})
    total = sum(item_data.get('total', 0) for item_data in cart.values())
    # Update total in the cart
    cart['total'] = total

    # Save the updated cart in the session
    request.session['cart'] = cart

    print(cart)

    return render(request, 'checkout.html', {'total': total})

def place_order(request):
    if request.method == 'POST':
        # Retrieve billing details and cart details from the form and session
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        cart = request.session.get('cart', {})
        total = request.session.get('cart_total', 0)

        # Create an order
        order = UserOrder.objects.create(
            full_name=full_name,
            phone=phone,
            address=address,
            total_amount=total
        )

        # Add items to the order
        for item_id, item_data in cart.items():
            menu_item = MenuItem.objects.get(pk=item_id)
            quantity = item_data['quantity']
            
            UserOrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

        # Clear the cart after placing the order
        request.session['cart'] = {}

        return render(request, 'index.html')
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
