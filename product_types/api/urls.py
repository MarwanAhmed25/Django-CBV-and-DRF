from .views import TypeListCreateApi, TypeRetrievUpdateDestroyApi
from django.urls import path

urlpatterns = [
    path('', TypeListCreateApi.as_view()),
    path('<str:slug>', TypeRetrievUpdateDestroyApi.as_view()),
]
