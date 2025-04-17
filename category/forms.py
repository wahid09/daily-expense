from django import forms
from .models import Category
from django.utils.text import slugify


class CategoryFrom(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['user', 'slug']

        # def clean(self):
        #     cleaned_data = super().clean()
        #     name = cleaned_data.get('category_name')
        #     if name and not cleaned_data.get('slug'):
        #         cleaned_data['slug'] = slugify(name)
        #     return cleaned_data

        widgets = {
            # 'user': forms.Select(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Select User (optional)'
            # }),
            'category_type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'category_icon': forms.Select(attrs={
                'class': 'form-select',
            }),
            'category_icon_color': forms.Select(attrs={
                'class': 'form-select color-picker',
            }),
            'category_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
            # 'slug': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'disabled': 'disabled',
            #     'readonly': 'readonly',
            #     'placeholder': 'Auto-generated or custom slug'
            # }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
