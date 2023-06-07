import requests as re
from django.shortcuts import render, redirect

from tg_bot.models import Category
from dashboard.category.forms import CategoryForms


def category(requests):
    lists = Category.objects.all()
    ctx = {
        'lists': lists
    }
    return render(requests, 'dashboard/category/category.html', ctx)


def category_form(requests):
    forms = CategoryForms()
    if requests.POST:
        form = CategoryForms(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('dash_category')
        else:
            print(form.errors)
        return redirect('dash_category')
    ctx = {
        "forms": forms
    }
    return render(requests, 'dashboard/category/form.html', ctx)


def category_edit(requests, pk):
    if pk:
        root = Category.objects.get(pk=pk)
        forms = CategoryForms(instance=root)
    else:
        raise ValueError('topilmadi 404')
    if requests.POST:
        form = CategoryForms(requests.POST, requests.FILES or None, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_category')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/category/form.html', ctx)


def delete_category(requests, pk=None, dlt=None):
    if dlt:
        Category.objects.get(pk=dlt).delete()
        return redirect("dash_category")

    ctg = Category.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/category/delete.html", ctx)

