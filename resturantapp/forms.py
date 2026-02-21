from django import forms
from . models import FoodItem


class FoodUpload(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['category', 'name', 'description', 'price', 'image' ]
        