import requests as re
from django.shortcuts import render, redirect

from tg_bot.models import Product
from dashboard.product.forms import ProductForm


def product_list(requests):
    root = Product.objects.all()
    ctx = {
        'root': root
    }
    return render(requests, 'dashboard/product/product.html', ctx)


def product_add(requests):
    forms = ProductForm()
    if requests.POST:
        form = ProductForm(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('dash_product')
    ctx = {
        "forms": forms
    }
    return render(requests, f"dashboard/product/form.html", ctx)


def product_edit(requests, pk):
    if pk:
        root = Product.objects.get(pk=pk)
        forms = ProductForm(instance=root)
    else:
        raise ValueError('topilmadi 404')
    if requests.POST:
        form = ProductForm(requests.POST, requests.FILES or None, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_product')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/product/form.html', ctx)


def delete_product(requests, pk=None, dlt=None):
    if dlt:
        Product.objects.get(pk=dlt).delete()
        return redirect("dash_product")

    ctg = Product.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/product/delete.html", ctx)
