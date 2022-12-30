from .views import ProductListCreateApi, ProductRetrievUpdateDestroyApi
from django.urls import path

urlpatterns = [
    path('', ProductListCreateApi.as_view()),
    path('<str:slug>', ProductRetrievUpdateDestroyApi.as_view()),
]
