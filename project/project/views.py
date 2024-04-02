from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def system_administrator(request):
    return render(request, 'system_admin.html')
