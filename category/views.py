from django.shortcuts import render
from .models import Category


# Create your views here.

def get_category(request):
    categories = Category.objects.all().order_by('-created_at')  # get all categories
    print(categories)
    context = {'categories': categories}
    return render(request, 'categories/category_list.html', context)


def create_category(request):
    pass
