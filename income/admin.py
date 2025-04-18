from django.contrib import admin
from .models import Income

# Register your models here.

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'income_date', 'created_at', 'is_active')
    fields = ('user', 'category', 'amount', 'income_date', 'is_active')
    list_editable = ['is_active']
    search_fields = ['user__username', 'category__name', 'amount']


admin.site.register(Income, IncomeAdmin)
