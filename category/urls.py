from django.urls import path, include

from . import views

app_name = 'category'
urlpatterns = [
    path('', views.get_category, name='category-list'),
    path('create', views.create_category, name='category-create'),
    path('edit/<int:pk>/', views.edit_category, name='category-edit'),
    path('delete/<int:pk>/', views.delete_category, name='category-delete'),
    path('view/<int:pk>/', views.category_detail, name='category-detail'),
]