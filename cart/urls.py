from django.urls import path

from .views import detail_cart, add_to_cart, remove_cart, clear_cart

app_name = 'cart'

urlpatterns = [
    path('', detail_cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_cart'),
    path('remove/<int:product_id>/', remove_cart, name='remove_cart'),
    path('clear/', clear_cart, name='clear_cart'),
]
