from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def system_administrator(request):
    return render(request, 'system_admin.html')


def about(request):
    return render(request, 'about.html')

def discounts_main_page(request):
    return render(request, 'discounts_main_page.html')