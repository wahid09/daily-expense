from django.db import models
from userautentication.models import Account
from category.models import Category, CategoryType


# Create your models here.


class Expense(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank', 'Bank Transfer'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='expense_user')
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    expense_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.amount} on {self.expense_date}"


class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name


class ExpenseTag(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='expense_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_expenses')

    class Meta:
        unique_together = ('expense', 'tag')  # Avoid duplicates
        verbose_name = "Expense Tag"
        verbose_name_plural = "Expense Tags"

    def __str__(self):
        return f"{self.expense} - {self.tag.tag_name}"


class ExpenseCategoryAmountTrack(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='expense_category_users')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expense_category_track')
    expenses = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='expense_track')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
