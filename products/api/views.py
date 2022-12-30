from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permission import IsAuthorOrReadOnly
from .serializers import ProductSerializer, Product

class ProductListCreateApi(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrievUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'