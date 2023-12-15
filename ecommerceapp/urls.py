from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.index,name='index'),
   path('login',views.login,name='login'),
   path('admin_home',views.admin_home,name='admin_home'),
   path('user_home',views.user_home,name='user_home'),
   path('log_in',views.log_in,name='log_in'),
   path('add_category',views.add_category,name='add_category'),
   path('add_product',views.add_product,name='add_product'),
   path('addc',views.addc,name='addc'),
   path('add_pro',views.add_pro,name='add_pro'),
   path('show_product',views.show_product,name='show_product'),
   path('delete_prod/<int:pk>',views.delete_prod,name='delete_prod'),
   path('user_signup',views.user_signup,name='user_signup'),
   path('add_user',views.add_user,name='add_user'),
   path('user_details',views.user_details,name='user_details'),
   path('delete_user/<int:pk>',views.delete_user,name='delete_user'),
   path('log_out',views.log_out,name='log_out'),
   path('all_products',views.all_products,name='all_products'),
   path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
   path('Cart',views.Cart,name='Cart'),
   path('remove_from_cart/<int:pk>',views.remove_from_cart,name='remove_from_cart'),
   path('category_detail/<int:pk>',views.category_detail,name='category_detail'),
   
]