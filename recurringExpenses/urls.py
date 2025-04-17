from django.urls import path, include

from . import views

app_name = 'recurringBudget'
urlpatterns = [
    path('', views.get_recurring_budget, name='recurring_budget-list')
]
