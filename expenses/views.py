from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Expense
from .forms import ExpenseForm

# Create your views here.


def get_expense(request):
    expense = Expense.objects.all().order_by('-created_at')
    context = {'expense':expense}
    return render(request, 'expense/expense_list.html', context)


def create_expense(request):
    form_action = reverse('expense:expense-create')
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense:expense-list')
    else:
        form = ExpenseForm()

    return render(request, 'expense/expense_create.html', {'form': form, 'form_action': form_action})


def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    form_action = reverse('expense:expense-edit', args=[expense.pk])
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense.save()
            return redirect('expense:expense-list')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expense/expense_create.html', {'form': form, 'form_action': form_action})


def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    return redirect('expense:expense-list')


def expense_detail(request):
    pass
