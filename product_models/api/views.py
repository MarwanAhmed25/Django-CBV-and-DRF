#from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BrandModelSerializer, BrandModel
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly

class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'



""" 
class BrandModelListCreateApi(ListCreateAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer


class BrandModelRetrievUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer
    lookup_field = 'slug'

"""