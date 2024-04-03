from django.contrib import admin
from django.urls import path
from .views import (AdministratorCreateView,
                    AdministratorListView,
                    AdministratorUpdateView,
                    AdministratorDeleteView,
                    AdministratorIndex,
                    MenuOperators,
                    MenuCustomers,
                    MenuPackages,
                    MenuDiscounts,
                    MenuServices)

app_name = 'administrator'

urlpatterns = [
    path("", AdministratorIndex.as_view(), name="administrator_index"),
    path("create", AdministratorCreateView.as_view(), name="administrator_create"),
    path("list", AdministratorListView.as_view(), name='administrator_list'),
    path("<int:id_administrator>/update", AdministratorUpdateView.as_view(), name='administrator_update'),
    path("<int:id_administrator>/delete", AdministratorDeleteView.as_view(), name='administrator_delete'),
    path("menu_operators", MenuOperators.as_view(), name='menu_operators'),
    path("menu_customers", MenuCustomers.as_view(), name='menu_customers'),
    path("menu_packages", MenuPackages.as_view(), name='menu_packages'),
    path("menu_discounts", MenuDiscounts.as_view(), name='menu_discounts'),
    path("menu_services", MenuServices.as_view(), name='menu_services')
]
