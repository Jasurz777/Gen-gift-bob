import requests as re
from django.shortcuts import render, redirect

from dashboard.models import RegistrationModel
from dashboard.registiratsiya.forms import RegisterForm


def register(requests):
    lists = RegistrationModel.objects.all()
    ctx = {
        'lists': lists
    }
    return render(requests, 'dashboard/reg/register.html', ctx)


def register_add(requests):
    forms = RegisterForm()
    if requests.POST:
        form = RegisterForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_register_reg')
    ctx = {
        'forms': forms
    }
    return render(requests,'dashboard/reg/form.html', ctx)


def register_edit(requests, pk):
    if pk:
        lists = RegistrationModel.objects.get(pk=pk)
        forms = RegisterForm(instance=lists)
    else:
        raise ValueError('topilmadi 404')
    if requests.POST:
            form = RegisterForm(requests.POST, instance=lists)
            if form.is_valid():
                form.save()
                return redirect('dash_register_reg')
            else:
                print(form.errors)
    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/reg/form.html', ctx)


def delete_register(requests, pk=None, dlt=None):
    if dlt:
        RegistrationModel.objects.get(pk=dlt).delete()
        return redirect("dash_register_reg")

    ctg = RegistrationModel.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/reg/delete.html", ctx)


