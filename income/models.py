from django.db import models
from userautentication.models import Account
from category.models import Category

# Create your models here.


class Income(models.Model):
    class Income(models.Model):
        PAYMENT_METHODS = [
            ('cash', 'Cash'),
            ('card', 'Card'),
            ('bank', 'Bank Transfer'),
            ('other', 'Other'),
        ]

        user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='income_user', null=True, blank=True)
        category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='incomes')
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        description = models.TextField(blank=True)
        income_date = models.DateField()
        payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
        is_active = models.BooleanField(default=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            verbose_name = 'Income'
            verbose_name_plural = 'Incomes'

        def __str__(self):
            return f"{self.user} - {self.amount}"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user'].queryset = Account.objects.filter(is_active=True)


