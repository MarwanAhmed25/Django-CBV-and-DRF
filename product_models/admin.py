from django.contrib import admin
from .models import BrandModel
# Register your models here.

@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    fields = ('title',)
    
