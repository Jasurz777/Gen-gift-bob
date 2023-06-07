import requests as re
from django.shortcuts import render, redirect

from tg_bot.models import Situation
from dashboard.situation.forms import SituationForm


def situation_handler(requests):
    root = Situation.objects.all()

    ctx = {
        'root': root
    }
    return render(requests, 'dashboard/situation/situation.html', ctx)


def situation_add(requests):
    forms = SituationForm()
    if requests.POST:
        form = SituationForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_situation')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/situation/form.html', ctx)


def edit(requests, pk):
    if pk:
        root = Situation.objects.get(pk=pk)
        forms = SituationForm(instance=root)
    else:
        raise ValueError('Toplimadi 404')
    if requests.POST:
        form = SituationForm(requests.POST, requests.FILES, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_situation')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }

    return render(requests, 'dashboard/situation/form.html', ctx)


def delete_situation(requests, pk=None, dlt=None):
    if dlt:
        Situation.objects.get(pk=dlt).delete()
        return redirect("dash_situation")

    ctg = Situation.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/situation/delete.html", ctx)
