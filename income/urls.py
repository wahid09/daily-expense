from django.urls import path, include

from . import views

app_name = 'income'
urlpatterns = [
    path('', views.get_income, name='income-list'),
    path('create', views.create_income, name='income-create'),
    path('edit/<int:pk>', views.edit_income, name='income-edit'),
    path('delete/<int:pk>', views.delete_income, name='income-delete'),
    path('detail/<int:pk>', views.income_detail, name='income-detail')
]
