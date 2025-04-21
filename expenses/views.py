from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Expense, ExpenseCategoryAmountTrack
from .forms import ExpenseForm
from django.db import transaction
from datetime import date
from budgets.models import Budget
from django.core.exceptions import ValidationError
from category.models import Category


# Create your views here.


def get_expense(request):
    expense = Expense.objects.all().order_by('-created_at')
    context = {'expense': expense}
    return render(request, 'expense/expense_list.html', context)


# @transaction.atomic
# def create_expense(request):
#     form_action = reverse('expense:expense-create')
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST, user=request.user)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     expense = form.save(commit=False)
#                     expense.user = request.user
#                     expense.save()
#
#                     # Update ExpenseCategoryAmountTrack
#                     track, created = ExpenseCategoryAmountTrack.objects.get_or_create(
#                         user=expense.user,
#                         category=expense.category,
#                         defaults={'amount': expense.amount, 'expenses': expense}
#                     )
#                     if not created:
#                         track.amount += expense.amount
#                         track.expenses = expense
#                         track.save()
#
#                 return redirect('expense:expense-list')
#
#             except Exception as e:
#                 form.add_error(None, f"An error occurred: {str(e)}")
#     else:
#         form = ExpenseForm()
#
#     return render(request, 'expense/expense_create.html', {'form': form, 'form_action': form_action})
@transaction.atomic
def create_expense(request):
    form_action = reverse('expense:expense-create')

    if request.method == 'POST':
        form = ExpenseForm(request.POST, user=request.user)
        if form.is_valid():
            try:
                with transaction.atomic():
                    expense = form.save(commit=False)
                    expense.user = request.user
                    expense.save()

                    # Get or update ExpenseCategoryAmountTrack
                    track, created = ExpenseCategoryAmountTrack.objects.get_or_create(
                        user=expense.user,
                        category=expense.category,
                        defaults={'amount': expense.amount, 'expenses': expense}
                    )
                    if not created:
                        track.amount += expense.amount
                        track.expenses = expense
                        track.save()

                    # Deduct from Budget
                    month_start = date(expense.expense_date.year, expense.expense_date.month, 1)
                    budget = Budget.objects.filter(
                        user=request.user,
                        category=expense.category,
                        month__year=month_start.year,
                        month__month=month_start.month
                    ).first()

                    if budget:
                        if expense.amount > budget.amount:
                            raise ValidationError(
                                f"Expense exceeds budget by {expense.amount - budget.amount:.2f}!"
                            )
                        budget.amount -= expense.amount
                        budget.save()

                return redirect('expense:expense-list')

            except ValidationError as ve:
                form.add_error(None, ve.message)
            except Exception as e:
                form.add_error(None, f"An unexpected error occurred: {str(e)}")
    else:
        form = ExpenseForm(user=request.user)

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


def load_categories(request):
    category_type_id = request.GET.get('category_type')
    categories = Category.objects.filter(category_type_id=category_type_id)
    return render(request, 'expense/partials/category_dropdown_options.html', {
        'categories': categories
    })


def expense_detail(request):
    pass
