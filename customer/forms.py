from django import forms
from . import models

attrs={'class':'form-control'}

class ShopCreateForm(forms.ModelForm):
    class Meta:
        model=models.Shop
        fields=['category','title','description']
        widgets={
            'category':forms.Select(attrs=attrs),
            'title':forms.TextInput(attrs=attrs),
            'description':forms.Textarea(attrs=attrs)
        }

class ShopUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = ['title', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs=attrs),
            'category': forms.Select(attrs=attrs),
            'status':forms.Select(attrs=attrs)
        }
