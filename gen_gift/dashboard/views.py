from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

from dashboard.models import User


def index(request):
    user = request.user
    if user.is_anonymous:
        return redirect('dash_login')

    ctx = {
        'user': user,
        'home': True
    }

    return render(request, "dashboard/base.html", ctx)


def register(requests):
    if requests.POST:
        first_name = requests.POST.get('first_name')
        last_name = requests.POST.get('last_name')
        user_name = requests.POST.get('user_name')
        password = requests.POST.get('password')
        password_conf = requests.POST.get('password_conf')

        if password_conf != password:
            return redirect('dash_register')

        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.user_name = user_name
        user.set_password(password)
        user.save()

        user = authenticate(requests, user_name=user_name, password=password)
        login(requests, user)
        return redirect('dashboardHome')

    return render(requests, 'dashboard/register.html')


def dash_login(request):
    print("aassad")
    ctx = {
        'error': False
    }
    if request.POST:
        print("Asads")
        password = request.POST.get('pass')
        username = request.POST.get('username')

        print("Asads")
        user = User.objects.filter(user_name=username).first()
        print("Asads")
        if not user:
            print("Asads")
            ctx = {
                'error': True
            }
            return render(request, 'dashboard/login.html', ctx)
        print("Asads")
        if user.check_password(password):
            user = authenticate(request, user_name=username, password=password)
            login(request, user)
            return redirect("dashboardHome")
        else:
            ctx = {
                'error': True
            }

    return render(request, 'dashboard/login.html', ctx)


@staff_member_required(login_url='dash_login')
def account(request):
    user = request.user
    if user.is_anonymous:
        return redirect('dash_login')

    if request.POST:
        user_name = request.POST.get('user_name')
        firstName = request.POST.get('name')
        lastName = request.POST.get('last_name')

        user.user_name = user_name
        user.first_name = firstName
        user.last_name = lastName
        user.save()

        return redirect('dash_account')

    ctx = {
        'user': user
    }

    return render(request, "dashboard/account.html", ctx)


def dash_logout(request):
    user = request.user
    if user.is_anonymous:
        return redirect('dash_login')
    logout(request)
    return redirect('dash_login')


def changePassword(requests):
    user = requests.user
    if user.is_anonymous:
        return redirect('dash_login')
    if requests.POST:
        old = requests.POST.get('old')
        password = requests.POST.get('pass')
        pass_conf = requests.POST.get('pass_conf')
        user = User.objects.get(id=requests.user.id)

        if not user.check_password(old):
            return redirect('dash_password_change')

        if password and pass_conf != password:
            return redirect('dash_password_change')

        user.set_password(password)
        user.save()
        user = authenticate(requests, user_name=user.user_name, password=user.password)
        login(requests, user)
        return redirect('dashboardHome')
    return render(requests, 'dashboard/changePassword.html')
