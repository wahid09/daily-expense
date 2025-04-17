from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Category
from .forms import CategoryFrom


# Create your views here.

def get_category(request):
    categories = Category.objects.filter(user=request.user).order_by('-created_at')
    context = {'categories': categories}
    return render(request, 'categories/category_list.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryFrom(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category:category-list')
    else:
        form = CategoryFrom()
        form_action = reverse('category:category-create')
    return render(request, 'categories/category_create.html', {'form': form, 'form_action': form_action})


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)

    if request.method == 'POST':
        form = CategoryFrom(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user  # Optional: reaffirm user
            category.save()
            return redirect('category:category-list')
    else:
        category = get_object_or_404(Category, pk=pk, user=request.user)
        form = CategoryFrom(instance=category)
        form_action = reverse('category:category-edit', args=[category.pk])
    return render(request, 'categories/category_create.html', {'form': form, 'form_action': form_action})


def category_detail(request, pk):
    pass
    # category = get_object_or_404(Category, pk=pk, user=request.user)
    # return render(request, 'categories/category_detail.html', {'category': category})


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    category.delete()
    return redirect('category:category-list')
