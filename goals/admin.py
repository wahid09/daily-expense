from django.contrib import admin
from .models import PaymentMethod, Goals, GoalsDeposited


# Register your models here.

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('payment_method_name', 'is_active', 'created_at')
    fields = ('payment_method_name', 'is_active')
    list_editable = ['is_active']
    search_fields = ['payment_method_name']


admin.site.register(PaymentMethod, PaymentMethodAdmin)


class GoalsAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'goals_amount', 'payment_method', 'goals_time_duration', 'is_active', 'created_at')
    fields = ('user', 'category', 'payment_method', 'goals_amount', 'goals_time_duration', 'is_active')
    list_editable = ['goals_amount', 'is_active']
    search_fields = ['user__username', 'category__name', 'goals_amount']


admin.site.register(Goals, GoalsAdmin)


class GoalsDepositedAdmin(admin.ModelAdmin):
    list_display = ('user', 'goals', 'deposited_month', 'deposited_amount', 'is_active', 'created_at')
    fields = ('user', 'goals', 'deposited_month', 'deposited_amount', 'is_active')
    list_editable = ['deposited_amount', 'is_active']
    search_fields = ['user__username', 'deposited_amount']


admin.site.register(GoalsDeposited, GoalsDepositedAdmin)
