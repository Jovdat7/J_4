from re import search
from django.urls import path

from . import views

urlpatterns = [
    path('products', views.ProductListView.as_view(), name='products'), # type: ignore
    path('products/categories/<slug:category_slug>', views.products_by_category, name='products-by-category'),
    path('products/<slug:product_slug>', views.product_detail, name='product-detail'),
    path('search', views.search, name='search')
]
