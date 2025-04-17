from django.urls import path, include

from . import views

app_name = 'income'
urlpatterns = [
    path('', views.get_income, name='income-list')
]
