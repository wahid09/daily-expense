from django import forms
from .models import Goals, PaymentMethod, GoalsDeposited
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django_summernote.widgets import SummernoteWidget
from django.core.exceptions import ValidationError
from datetime import date
from django.db import models


class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['category', 'goals_amount', 'goals_time_duration', 'payment_method', 'is_active']

        widgets = {
            # 'category_type': forms.Select(attrs={
            #     'class': 'form-select',
            #     'id': 'id_category_type',
            #     'hx-get': '/expenses/load-categories/',
            #     'hx-target': '#id_category',
            #     'hx-trigger': 'change',
            #     'hx-include': '[name="category_type"]'
            # }),
            'category': forms.Select(attrs={'class': 'form-select select2', 'id': 'id_category'}),
            'goals_amount': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter goals amount'
            }),
            # 'description': SummernoteWidget(attrs={'class': 'form-control form-control-sm'}),
            'goals_time_duration': DatePickerInput(attrs={'class': 'form-control form-control-sm'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class GoalsDepositedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.goal = kwargs.pop('goal', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        deposited_month = cleaned_data.get('deposited_month')
        deposited_amount = cleaned_data.get('deposited_amount')

        if self.user and self.goal and deposited_month and deposited_amount:
            total_deposited = GoalsDeposited.objects.filter(
                user=self.user,
                goals=self.goal
            ).aggregate(total=models.Sum('deposited_amount'))['total'] or 0

            if total_deposited + deposited_amount > self.goal.goals_amount:
                raise ValidationError(
                    f"Depositing ${deposited_amount} would exceed the goal limit of ${self.goal.goals_amount}. "
                    f"Currently deposited: ${total_deposited}."
                )

        return cleaned_data

    class Meta:
        model = GoalsDeposited
        fields = ['deposited_month', 'deposited_amount', 'is_active']
        widgets = {
            # 'goals': forms.Select(attrs={'class': 'form-select select2'}),
            'deposited_amount': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter expense amount'
            }),
            # 'description': SummernoteWidget(attrs={'class': 'form-control form-control-sm'}),
            'deposited_month': DatePickerInput(attrs={'class': 'form-control form-control-sm'}),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
