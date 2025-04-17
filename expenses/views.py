from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Expense
from .forms import ExpenseForm

# Create your views here.


def get_expense(request):
    expense = Expense.objects.all().order_by('-created_at')
    context = {'expense':expense}
    return render(request, 'expense/expense_list.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            print("Working")
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense:expense-list')
    else:
        form = ExpenseForm()
        form_action = reverse('expense:expense-create')
    return render(request, 'expense/expense_create.html', {'form': form, 'form_action': form_action})


def edit_expense(request):
    pass


def delete_expense(request):
    pass


def expense_detail(request):
    pass
