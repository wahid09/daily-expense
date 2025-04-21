from django.contrib import admin
from .models import Category, Icon, Color, CategoryType
# Register your models here.


class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('category_type_name', 'user', 'created_at', 'is_active')
    fields = ('user', 'category_type_name', 'is_active')
    list_editable = ['is_active']
    search_fields = ['category_type_name']


admin.site.register(CategoryType, CategoryTypeAdmin)


class IconAdmin(admin.ModelAdmin):
    list_display = ('icon_name', 'created_at', 'is_active')
    list_editable = ['is_active']
    search_fields = ['icon_name']


admin.site.register(Icon, IconAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name', 'created_at', 'is_active')
    list_editable = ['is_active']
    search_fields = ['color_name']


admin.site.register(Color, ColorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'category_type', 'user', 'created_at', 'is_active')
    list_editable = ['is_active']
    search_fields = ['category_name', 'slug']


admin.site.register(Category, CategoryAdmin)
