from django.db import models
from category.models import Category
from userautentication.models import Account


class PaymentMethod(models.Model):
    payment_method_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.payment_method_name}"


class Goals(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='goals_user')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goals_category')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='goals_payment_method')
    goals_amount = models.DecimalField(max_digits=12, decimal_places=2)
    goals_time_duration = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.category} - {self.goals_amount} - {self.goals_time_duration.strftime('%B %Y')}"


class GoalsDeposited(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='goals_deposited_user')
    goals = models.ForeignKey(Goals, on_delete=models.CASCADE, related_name='goals_deposited')
    deposited_month = models.DateField()
    deposited_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.goals} - {self.deposited_amount} - {self.deposited_month.strftime('%B %Y')}"
