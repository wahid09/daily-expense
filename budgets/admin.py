from django.contrib import admin
from .models import Budget

# Register your models here.


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('category', 'user', 'amount', 'is_active', 'created_at')
    fields = ('user', 'category', 'month', 'amount', 'is_active')
    list_editable = ['is_active']
    search_fields = ['category']


admin.site.register(Budget, BudgetAdmin)
