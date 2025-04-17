from django.db import models
from userautentication.models import Account
from category.models import Category

# Create your models here.


class Budget(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='budget_user')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='budgets')
    month = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"
        unique_together = ('user', 'category', 'month')

    def __str__(self):
        return f"{self.user} - {self.category.name} - {self.month.strftime('%B %Y')}"

