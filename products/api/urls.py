from .views import ProductViewSet
from rest_framework.routers import SimpleRouter
#from django.urls import path

router = SimpleRouter()

router.register('', ProductViewSet, basename='products')

urlpatterns = router.urls



""" 
urlpatterns = [
    path('', ProductListCreateApi.as_view()),
    path('<str:slug>', ProductRetrievUpdateDestroyApi.as_view()),
]
"""