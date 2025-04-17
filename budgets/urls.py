from django.urls import path, include

from . import views

app_name = 'budget'
urlpatterns = [
    path('', views.get_budget, name='budget-list')
]
