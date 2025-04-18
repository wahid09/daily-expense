from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Income
from .forms import IncomeForm

# Create your views here.


def get_income(request):
    income = Income.objects.all().order_by('-created_at')
    context = {'income':income}
    return render(request, 'income/income_list.html', context)


def create_income(request):
    form_action = reverse('income:income-create')
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income:income-list')
    else:
        form = IncomeForm()
    return render(request, 'income/income_create.html', {
        'form_action': form_action,
        'form': form
    })


def edit_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    form_action = reverse('income:income-edit', args=[income.pk])
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income.save()
            return redirect('income:income-list')
    else:
        form = IncomeForm(instance=income)

    return render(request, 'income/income_create.html', {'form': form, 'form_action': form_action})


def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    income.delete()
    return redirect('income:income-list')


def income_detail(request, pk):
    pass
