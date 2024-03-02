from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Homeview.as_view(),name='home'),
    path('product_list/',views.list_product_view,name='product_list'),
    path('category/<int:pk>',views.ListCategoryView.as_view(),name='category_list'),
    path('product/<int:pk>/',views.DeatilProductView.as_view(),name='product_detail'),
    path('search/',views.search_view,name='search'),
    path('wishlist/',views.WishlistView.as_view(),name='wishlist'),
    path('wishlist/add/<int:pk>',views.add_to_wishlist,name='wishlist_add'),
    path('wishlist/remove/<int:pk>',views.remove_from_wishlist,name='wishlist_remove'),
    ]