from django.shortcuts import render

# Create your views here.


def get_budget(request):
    return render(request, 'budget/budget_list.html')
