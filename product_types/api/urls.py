from .views import TypeViewSet
#from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('', TypeViewSet, basename='types')

urlpatterns = router.urls
"""
urlpatterns = [
    path('', TypeListCreateApi.as_view()),
    path('<str:slug>', TypeRetrievUpdateDestroyApi.as_view()),
]
"""

