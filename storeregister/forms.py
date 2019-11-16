from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['store_title', 'region', 'address', 'detailaddr', 
                'homepage', 'describe', 'photo']

        widgets={
            'store_title' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'제목을 입력하세요',
                }
            ),

            'region' : forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),

            'homepage': forms.TextInput(
                attrs={
                    'class':'form-control',
                }                
            ),

            'describe' : forms.Textarea(
                attrs={
                    'class':'form-control',
                }                
            ),
        }

        labels = {
            'store_title' : '스토어 이름', 
            'region' : '지역',  
            'homepage' : '홈페이지',
            'describe' : '설명', 
            'photo' : '사진',
        }