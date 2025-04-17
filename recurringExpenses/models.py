from django.db import models
from userautentication.models import Account
from category.models import Category

# Create your models here.


class RecurringExpense(models.Model):
    RECURRENCE_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='recurring_expenses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recurring_expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recurrence = models.CharField(max_length=10, choices=RECURRENCE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Recurring Expense"
        verbose_name_plural = "Recurring Expenses"

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.recurrence})"
