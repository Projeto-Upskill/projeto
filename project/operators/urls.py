from django.contrib import admin
from django.urls import path
from .views import (OperatorsCreateView,
                    OperatorsListView,
                    OperatorsUpdateView,
                    OperatorsDeleteView,
                    OperatorsIndex,
                    MenuCustomers,
                    MenuPackages,
                    MenuDiscounts)

app_name = 'operators'

urlpatterns = [
    path("", OperatorsIndex.as_view(), name="operator_index"),
    path("create", OperatorsCreateView.as_view(), name="operator_create"),
    path("list", OperatorsListView.as_view(), name='operator_list'),
    path("<int:id_operator>/update", OperatorsUpdateView.as_view(), name='operator_update'),
    path("<int:id_Operator>/delete", OperatorsDeleteView.as_view(), name='operator_delete'),
    path("menu_customers", MenuCustomers.as_view(), name='menu_customers'),
    path("menu_packages", MenuPackages.as_view(), name='menu_packages'),
    path("menu_discounts", MenuDiscounts.as_view(), name='menu_discounts')
]