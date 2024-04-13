from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as app_login, logout as app_logout
from django.contrib import messages


def login(request):
    return render(request, "login.html")


def submit_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"username: {username}, password: {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f'user: {user}')
            app_login(request, user)
            return redirect('administrator:administrator_index')
        else:
            print('error. User is none')
            messages.error(request, "Login incorrect, try again!")
    return redirect("login")


def check_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        return redirect("login")


def logout(request):
    app_logout(request)
    return redirect('login')


def index(request):
    return render(request, 'index.html')


def system_administrator(request):
    return render(request, 'system_admin.html')


def about(request):
    return render(request, 'about.html')


def discounts_main_page(request):
    return render(request, 'discounts_main_page.html')
