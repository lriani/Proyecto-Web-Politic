from django.urls import path

from . import views 

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('new_product/', views.new_product, name='new_product'),
    path('edition_product/', views.edition_product, name='edition_product'),
    ]   
