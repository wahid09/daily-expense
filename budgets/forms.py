from django import forms
from .models import Budget


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['user', 'category', 'month', 'amount']

        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'month': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'month',  # HTML5 input type for month picker
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter budget amount'
            }),
        }
