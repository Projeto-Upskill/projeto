"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'project'

urlpatterns = [
    path("login", views.login, name='login'),
    path("login/submit", views.submit_login, name='submit_login'),
    path("logout", views.logout, name='logout'),
    path("", views.index,  name='index'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
    path("system_admin", views.system_administrator, name='system_admin'),
    path('administrator/', include("administrator.urls")),
    path('customer/', include('customers.urls')),
    path('operators/', include("operators.urls")),
    path('package/', include("packages.urls")),
    path('discounts_main_page/', views.discounts_main_page, name='discounts_main_page')
]
