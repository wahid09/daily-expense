from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from django.urls import reverse

from .models import Goals, GoalsDeposited
from django.utils.timezone import now
from datetime import timedelta, date
from django.db import models
from dateutil.relativedelta import relativedelta
from .forms import GoalsForm, GoalsDepositedForm


# Get all goals list


def get_goals(request):
    goals = Goals.objects.filter(user=request.user, is_active=True)

    goals_data = []
    for goal in goals:
        total_deposited = goal.goals_deposited.aggregate(total=Sum('deposited_amount'))['total'] or 0

        deposited_percentage = (total_deposited / goal.goals_amount * 100) if goal.goals_amount > 0 else 0

        goals_data.append({
            'goal': goal,
            'deposits': goal.goals_deposited.all().order_by('-deposited_month'),
            'total_deposited': total_deposited,
            'deposited_percentage': round(deposited_percentage),
        })
    context = {'goals_data': goals_data}
    return render(request, 'goals/goals_list.html', context)


# def goal_detail(request, goal_id):
#     goal = get_object_or_404(Goals, id=goal_id, user=request.user)
#     deposits = GoalsDeposited.objects.filter(goals=goal, is_active=True)
#     today = now().date()
#     first_day_of_this_month = today.replace(day=1)
#     last_month = first_day_of_this_month - timedelta(days=1)
#     last_month_start = last_month.replace(day=1)
#     last_month_end = last_month.replace(day=last_month.day)
#     last_month_deposited = deposits.filter(
#         deposited_month__year=last_month_start.year,
#         deposited_month__month=last_month_start.month
#     ).aggregate(total=models.Sum('deposited_amount'))['total'] or 0
#     total_deposited = deposits.aggregate(Sum('deposited_amount'))['deposited_amount__sum'] or 0
#     deposited_percentage = round((total_deposited / goal.goals_amount) * 100, 2) if goal.goals_amount else 0
#     remaining_percentage = 100 - deposited_percentage
#
#     return render(request, 'goals/goal_detail_partial.html', {
#         'goal': goal,
#         'total_deposited': total_deposited,
#         'deposited_percentage': deposited_percentage,
#         'remaining_percentage': remaining_percentage,
#         'deposits': deposits,
#         'last_month_deposited': last_month_deposited
#     })

def goal_detail(request, goal_id):
    goal = Goals.objects.select_related('category').get(id=goal_id, user=request.user)
    deposited_qs = goal.goals_deposited.filter(is_active=True)
    deposits = GoalsDeposited.objects.filter(goals=goal, is_active=True)

    total_deposited = deposited_qs.aggregate(Sum('deposited_amount'))['deposited_amount__sum'] or 0
    percentage = round((total_deposited / goal.goals_amount) * 100, 2) if goal.goals_amount else 0

    # Last month deposited
    last_month = date.today().replace(day=1) - relativedelta(months=1)
    last_month_deposit = \
        deposited_qs.filter(deposited_month__year=last_month.year, deposited_month__month=last_month.month).aggregate(
            Sum('deposited_amount'))['deposited_amount__sum'] or 0

    context = {
        'goal_data': {
            'goal': goal,
            'total_deposited': total_deposited,
            'deposited_percentage': percentage,
            'last_month_deposited': last_month_deposit,
        },
        'deposits': deposits
    }
    return render(request, 'goals/goal_detail_partial.html', context)


def goals_create(request):
    form_action = reverse('goals:goals-create')
    if request.method == 'POST':
        form = GoalsForm(request.POST)
        if form.is_valid():
            goals = form.save(commit=False)
            goals.user = request.user
            goals.save()
            return redirect('goals:goals-list')
    else:
        form = GoalsForm()
        context = {
            'form_action': form_action,
            'form': form
        }
    return render(request, 'goals/goals_create.html', context)


def goals_deposited(request, goal_id):
    form_action = reverse('goals:goals-deposited', args=[goal_id])
    goal_instance = get_object_or_404(Goals, pk=goal_id)

    if request.method == 'POST':
        form = GoalsDepositedForm(request.POST, user=request.user, goal=goal_instance)
        if form.is_valid():
            goal_deposited = form.save(commit=False)
            goal_deposited.goals = goal_instance
            goal_deposited.user = request.user
            goal_deposited.save()
            return redirect('goals:goals-list')
    else:
        form = GoalsDepositedForm(user=request.user, goal=goal_instance)

    context = {
        'form_action': form_action,
        'form': form
    }
    return render(request, 'goals/goals_deposited.html', context)
