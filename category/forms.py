from django import forms
from .models import Category


class CategoryFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'user',
            'category_type',
            'category_icon',
            'category_icon_color',
            'category_name',
            'slug',
            'is_active',
        ]
        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select User (optional)'
            }),
            'category_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'category_icon': forms.Select(attrs={
                'class': 'form-control',
            }),
            'category_icon_color': forms.Select(attrs={
                'class': 'form-control color-picker',
            }),
            'category_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Auto-generated or custom slug'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
