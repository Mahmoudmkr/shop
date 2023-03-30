from django import forms
from . import models

class ShopCreateForm(forms.ModelForm):
    class Meta:
        model=models.Shop
        fields=['category','title','description']
        widgets={
            'category':forms.Select(),
            'title':forms.TextInput(),
            'description':forms.Textarea()
        }

class ShopUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = ['title', 'category', 'status']
        widgets = {
            'title': forms.TextInput(),
            'category': forms.Select(),
            'status':forms.Select()
        }
