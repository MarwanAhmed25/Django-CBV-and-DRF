from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('update/<str:slug>', views.ProductUpdateView.as_view(), name='product_update'),
    path('create', views.ProductCreateView.as_view(), name='product_create'),
    path('delete/<str:slug>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('<str:slug>', views.ProductDetailView.as_view(), name='product_detail'),

]