from rest_framework.serializers import ModelSerializer
from ..models import BrandModel

class BrandModelSerializer(ModelSerializer):
    class Meta:
        model = BrandModel
        exclude = ('slug',)