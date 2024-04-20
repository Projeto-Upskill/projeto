from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as app_login, logout as app_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from .permissions import *


super_admin = Group.objects.get(name="superadmin_group")
User = get_user_model()


def login(request):
    return render(request, "login.html")


def submit_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            app_login(request, user)
            request.session['id'] = user.id
            request.session['username'] = username
            return render(request, 'index.html')
        else:
            messages.error(request, "Login incorrect, try again!")
    return redirect("login")


def check_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        return redirect("login")


def logout(request):
    app_logout(request)
    request.session.delete()
    return redirect('login')


@permission_required('project.view_administrator')
@login_required
def system_administrator(request):
    return render(request, 'system_admin.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def discounts_main_page(request):
    return render(request, 'discounts_main_page.html')


def forbidden_page(request):
    return render(request, 'forbidden.html')
