from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Product, ProductAdmin)