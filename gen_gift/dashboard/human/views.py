import requests as re
from django.shortcuts import render, redirect

from tg_bot.models import Human
from dashboard.human.forms import HumanForm1


def human_handler(requests):
    root = Human.objects.all()

    ctx = {
        'root': root
    }
    return render(requests, 'dashboard/human/human.html', ctx)


def human_add(requests):
    forms = HumanForm1()
    if requests.POST:
        form = HumanForm1(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_human')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/human/form.html', ctx)


def edit(requests, pk):
    if pk:
        root = Human.objects.get(pk=pk)
        forms = HumanForm1(instance=root)
    else:
        raise ValueError('Toplimadi 404')
    if requests.POST:
        form = HumanForm1(requests.POST, requests.FILES, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_human')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }

    return render(requests, 'dashboard/human/form.html', ctx)


def delete_human(requests, pk=None, dlt=None):
    if dlt:
        Human.objects.get(pk=dlt).delete()
        return redirect("dash_human")

    ctg = Human.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/human/delete.html", ctx)
