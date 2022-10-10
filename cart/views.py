from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from .cart import Cart
from books.models import Book
from .forms import AddToCartProduct
from django.contrib import messages


def detail_cart(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartProduct(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
    return render(request, 'cart/detail_cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Book, id=product_id)
    form = AddToCartProduct(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])
        messages.success(request, 'محصول به سبد خرید اضافه شد')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_cart(request, product_id):
    cart = Cart(request)

    book = get_object_or_404(Book, id=product_id)

    cart.remove(book)

    return redirect('cart:cart')


def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()

    return redirect('home')
