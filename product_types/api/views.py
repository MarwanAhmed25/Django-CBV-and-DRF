#from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TypeSerializer, Type
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


""" 
class TypeListCreateApi(ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeRetrievUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = 'slug' 
"""