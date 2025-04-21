from django.urls import path, include

from . import views

app_name = 'goals'
urlpatterns = [
    path('', views.get_goals, name='goals-list'),
    path('goal-detail/<int:goal_id>/', views.goal_detail, name='goal-detail'),
    path('create', views.goals_create, name='goals-create'),
    path('deposited/<int:goal_id>', views.goals_deposited, name='goals-deposited'),
]
