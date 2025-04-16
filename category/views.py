from django.shortcuts import render
from .models import Category

# Create your views here.

def get_category(request):
    categories = Category.objects.all()  # get all categories
    return render(request, 'categories/category_list.html', {'categories': categories})
def create_category(request):
    pass
