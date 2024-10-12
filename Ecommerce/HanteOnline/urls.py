from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.AddToCart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('Mobiles/', views.Mobiles, name='Mobiles'),
    path('Computers/', views.Computers, name='Computers'),
]
