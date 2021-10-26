from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('payment/', views.payment, name="payment"),
    path('about/', views.about, name="about"),

    path('update_item/', views.updateItem, name="update_item"),
]