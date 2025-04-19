from django import forms
from .models import Expense
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django_summernote.widgets import SummernoteWidget


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'expense_date', 'payment_method']

        widgets = {
            # 'user': forms.Select(attrs={
            #     'class': 'form-control'
            # }),
            'category': forms.Select(attrs={
                'class': 'form-select select2'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter expense amount'
            }),
            # 'description': forms.Textarea(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Optional description',
            #     'rows': 3
            # }),
            'description': SummernoteWidget(attrs={
                'class': 'form-control form-control-sm'
            }),
            'expense_date': DatePickerInput(attrs={
                'class': 'form-control form-control-sm'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
