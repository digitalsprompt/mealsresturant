from django import forms
from django.contrib.auth.models import User

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255, widget=forms.Textarea)
    phone = forms.CharField(max_length=15)