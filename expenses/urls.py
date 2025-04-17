from django.urls import path, include

from . import views

app_name = 'expense'
urlpatterns = [
    path('', views.get_expense, name='expense-list'),
    path('create', views.create_expense, name='expense-create'),
    path('edit/<int:pk>/', views.edit_expense, name='expense-edit'),
    path('delete/<int:pk>/', views.delete_expense, name='expense-delete'),
    path('view/<int:pk>/', views.expense_detail, name='expense-detail'),
]
