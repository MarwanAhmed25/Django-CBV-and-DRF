from .views import BrandModelListCreateApi, BrandModelRetrievUpdateDestroyApi
from django.urls import path

urlpatterns = [
    path('', BrandModelListCreateApi.as_view()),
    path('<str:slug>', BrandModelRetrievUpdateDestroyApi.as_view()),
]
