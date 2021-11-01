from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('payment/', views.payment, name="payment"),
    path('about/', views.about, name="about"),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]