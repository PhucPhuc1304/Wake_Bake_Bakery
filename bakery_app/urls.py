from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('menu', views.menu, name = 'menu'),
    path('productdetail/<int:product_id>/', views.productdetail, name='productdetail'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
    path('checkout', views.checkout, name = 'checkout'),
    path('cart', views.cart, name = 'cart'),
    path('about', views.about, name='about'),

]