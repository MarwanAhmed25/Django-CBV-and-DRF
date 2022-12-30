from .views import BrandModelViewSet
from rest_framework.routers import SimpleRouter
#from django.urls import path

router = SimpleRouter()

router.register('', BrandModelViewSet, basename='models')

urlpatterns = router.urls




""" 
urlpatterns = [
    path('', BrandModelListCreateApi.as_view()),
    path('<str:slug>', BrandModelRetrievUpdateDestroyApi.as_view()),
] 
"""
