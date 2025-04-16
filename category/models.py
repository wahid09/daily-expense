from django.db import models

# Create your models here.
from userautentication.models import Account


class CategoryType(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='category_type_user', null=True, blank=True)
    category_type_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_type_name


class Icon(models.Model):
    icon_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.icon_name


class Color(models.Model):
    color_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color_name


class Category(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='category_user', null=True, blank=True)
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE, related_name='cat_type')
    category_icon = models.ForeignKey(Icon, on_delete=models.CASCADE, related_name='icon')
    category_icon_color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='icon_color')
    category_name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=264, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

