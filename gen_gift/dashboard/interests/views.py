from django.shortcuts import render, redirect

from tg_bot.models import Interests
from dashboard.interests.forms import InterestsForm


def interests_list(requests):
    lists = Interests.objects.all()
    ctx = {
        'lists': lists
    }
    return render(requests, 'dashboard/interests/interests.html', ctx)


def edit_interests(requests, pk):
    if pk:
        root = Interests.objects.get(pk=pk)
        forms = InterestsForm(instance=root)
    else:
        raise ValueError('Toplimadi 404')
    if requests.POST:
        form = InterestsForm(requests.POST, requests.FILES, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_tables')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }

    return render(requests, 'dashboard/interests/form.html', ctx)


def add_interests(requests):
    forms = InterestsForm()
    if requests.POST:
        form = InterestsForm(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('dash_tables')
    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/interests/form.html', ctx)


def delete_interests(requests, pk=None, dlt=None):
    if dlt:
        Interests.objects.get(pk=dlt).delete()
        return redirect("dash_tables")

    ctg = Interests.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/interests/delete.html", ctx)
