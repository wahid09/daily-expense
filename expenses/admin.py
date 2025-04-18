from django.contrib import admin
from .models import Expense, ExpenseTag, Tag


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'expense_date', 'created_at', 'is_active')
    fields = ('user', 'category', 'amount', 'expense_date', 'is_active')
    list_editable = ['is_active']
    search_fields = ['user__username', 'category__name', 'amount']


admin.site.register(Expense, ExpenseAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    fields = ('tag_name',)
    # list_editable = ['tag_name']
    search_fields = ['tag_name']


admin.site.register(Tag, TagAdmin)


class ExpenseTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'expense')
    fields = ('expense', 'tag')
    search_fields = ['expense__id', 'tag__name']


admin.site.register(ExpenseTag, ExpenseTagAdmin)



