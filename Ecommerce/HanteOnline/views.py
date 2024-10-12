from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, Category
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
def AddToCart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total=cart.total
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})
def Mobiles(request):
    category = get_object_or_404(Category, name='Phones')
    products = Product.objects.filter(category=category)
    return render(request, 'Mobiles.html', {'products': products,'category':category})
def Computers(request):
    category = get_object_or_404(Category, name='Computers')
    products = Product.objects.filter(category=category)
    return render(request, 'Computers.html', {'products': products,'category':category})
