import requests as re
from django.shortcuts import render, redirect

from tg_bot.models import Agee
from dashboard.age.forms import AgeForm


def age_list(requests):
    root = Agee.objects.all()

    ctx = {
        'root': root
    }
    return render(requests, 'dashboard/age/age.html', ctx)


def age_add(requests):
    forms = AgeForm()
    if requests.POST:
        form = AgeForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_age_list')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/age/form.html', ctx)


def age_edit(requests, pk):
    if pk:
        root = Agee.objects.get(pk=pk)
        forms = AgeForm(instance=root)
    else:
        raise ValueError('Toplimadi 404')
    if requests.POST:
        form = AgeForm(requests.POST, requests.FILES, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_age_list')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }

    return render(requests, 'dashboard/age/form.html', ctx)


def age_delete(requests, pk=None, dlt=None):
    if dlt:
        Agee.objects.get(pk=dlt).delete()
        return redirect("dash_age_list")

    ctg = Agee.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/age/delete.html", ctx)
