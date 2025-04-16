from django.urls import path, include

from . import views

app_name = 'userauthencation'
urlpatterns = [
    path('register', views.get_register, name='register'),
    path('', views.get_login, name='login'),
    path('logout/', views.get_logout, name='logout'),
    path('dashboard/', views.get_dashboard, name='dashboard'),
]