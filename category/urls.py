from django.urls import path, include

from . import views

app_name = 'category'
urlpatterns = [
    path('category-list', views.get_category, name='category'),
]