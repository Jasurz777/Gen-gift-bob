import requests as re
from django.shortcuts import render, redirect

from tg_bot.models import Cash
from dashboard.cash.forms import CashForm


def fact_list(requests, pk=None):
    forms = CashForm()
    if pk:
        html = 'detail'
        lists = Cash.objects.get(pk=pk)
        forms = CashForm(instance=lists)
    else:
        html = 'cash'
        lists = Cash.objects.all()
    ctx = {
        "lists": lists,
        "forms": forms
    }
    return render(requests, f"dashboard/cash/{html}.html", ctx)


def add(requests):
    forms = CashForm()
    if requests.POST:
        form = CashForm(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('dash_cash_list')
        else:
            print(form.errors)
    ctx = {
        "forms": forms
    }
    return render(requests, "dashboard/cash/form.html", ctx)


def edit_cash(requests, pk):
    if pk:
        root = Cash.objects.get(pk=pk)
        forms = CashForm(instance=root)
    else:
        raise ValueError('Toplimadi 404')
    if requests.POST:
        form = CashForm(requests.POST, requests.FILES or None, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_cash_list')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }

    return render(requests, 'dashboard/cash/form.html', ctx)


def delete_cash(requests, pk=None, dlt=None):
    if dlt:
        Cash.objects.get(pk=dlt).delete()
        return redirect("dash_cash_list")

    ctg = Cash.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/cash/delete.html", ctx)
