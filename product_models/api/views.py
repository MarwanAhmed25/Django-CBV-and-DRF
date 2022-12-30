from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BrandModelSerializer, BrandModel

class BrandModelListCreateApi(ListCreateAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer


class BrandModelRetrievUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer
    lookup_field = 'slug'