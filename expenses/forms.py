from django import forms
from .models import Expense, ExpenseCategoryAmountTrack
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django_summernote.widgets import SummernoteWidget
from budgets.models import Budget
from django.core.exceptions import ValidationError
from datetime import date
from django.db import models


class ExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # pass user from view
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['category'].queryset = self.fields['category'].queryset.filter(
                user=self.user
            )

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        amount = cleaned_data.get('amount')
        expense_date = cleaned_data.get('expense_date')

        if self.user and category and amount and expense_date:
            month = date(expense_date.year, expense_date.month, 1)
            budget = Budget.objects.filter(
                user=self.user,
                category=category,
                month__year=month.year,
                month__month=month.month
            ).first()
            if budget:
                total_spent = ExpenseCategoryAmountTrack.objects.filter(
                    user=self.user,
                    category=category
                ).aggregate(models.Sum('amount'))['amount__sum'] or 0

                if total_spent + amount > budget.amount:
                    raise ValidationError(
                        f"Total expenses in '{category}' exceed your budget for {month.strftime('%B %Y')}."
                    )

        return cleaned_data

    class Meta:
        model = Expense
        fields = ['category_type', 'category', 'amount', 'description', 'expense_date', 'payment_method']
        widgets = {
            'category_type': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_category_type',
                'hx-get': '/expenses/load-categories/',
                'hx-target': '#id_category',
                'hx-trigger': 'change',
                'hx-include': '[name="category_type"]'
            }),
            'category': forms.Select(attrs={'class': 'form-select select2', 'id': 'id_category'}),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter expense amount'
            }),
            'description': SummernoteWidget(attrs={'class': 'form-control form-control-sm'}),
            'expense_date': DatePickerInput(attrs={'class': 'form-control form-control-sm'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }
