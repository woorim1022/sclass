from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['user', 'store_title', 'region', 'address', 'detailaddr', 
                'homepage', 'describe', 'photo']
