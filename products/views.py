from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "products_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detial.html"

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "create_product.html"

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_update.html"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_delete.html"

