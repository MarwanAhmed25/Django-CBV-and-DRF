from rest_framework.serializers import ModelSerializer
from ..models import Type

class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        exclude = ('slug',)
        