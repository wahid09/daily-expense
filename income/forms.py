from django import forms
from .models import Income
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django_summernote.widgets import SummernoteWidget


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['category', 'amount', 'description', 'income_date', 'payment_method', 'is_active']

        widgets = {
            # 'user': forms.Select(attrs={
            #     'class': 'form-control',
            # }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount'
            }),
            'description': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Optional description',
                'rows': 3
            }),
            'income_date': DatePickerInput(attrs={
                'class': 'form-control'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
