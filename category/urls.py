from django.urls import path, include

from . import views

app_name = 'category'
urlpatterns = [
    path('', views.get_category, name='category-list'),
    path('category-create', views.create_category, name='create-category')
]