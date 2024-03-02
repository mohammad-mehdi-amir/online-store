from django.contrib import admin
from django.urls import path
from . import views
app_name='carts'
urlpatterns = [
    path('',views.cart_detail_view,name='cart_detail'),
    path('add/<int:product_id>/',views.add_to_cart_view,name='cart_add'),
    path('remove/<int:product><str:color><str:size>',views.remove_cart,name='cart_remove'),
    path('clean/',views.clean_cart,name='cart_clean'),
    
    # path('wishlist/',views.,name='wishlist'),

]
    
