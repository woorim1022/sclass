from django import forms
from .models import Class

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('class_title', 'summary', 'describe', 'price', 
        'date', 'category', 'max_number', 
        'img1', 'img2', 'img3', 'img4', 'img5')
