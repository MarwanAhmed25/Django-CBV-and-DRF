from django import forms 
from .models import BrandModel


class Model_Form(forms.ModelForm):
    
    class Meta:
        model = BrandModel
        fields = ("title",)

