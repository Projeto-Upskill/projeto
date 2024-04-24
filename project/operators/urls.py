from django.contrib import admin
from django.urls import path
from .views import (OperatorsCreateView,
                    OperatorsListView,
                    OperatorsUpdateView,
                    OperatorsDeleteView,
                    OperatorsIndex,
                    MenuPackages,
                    MenuDiscounts,
                    MenuServices,
                    AssignPackageView,
                    AssignPackageDiscountView,
                    OperatorsPackageListView,
                    OperatorsPackageDiscountListView,
                    AssignServiceView,
                    AssignServiceDiscountView,
                    OperatorsServiceListView,
                    OperatorsServiceDiscountListView)

app_name = 'operators'

urlpatterns = [
    path("", OperatorsIndex.as_view(), name="operator_index"),
    path("create", OperatorsCreateView.as_view(), name="operator_create"),
    path("list", OperatorsListView.as_view(), name='operator_list'),
    path("<int:id_operator>/update", OperatorsUpdateView.as_view(), name='operator_update'),
    path("<int:id_operator>/delete", OperatorsDeleteView.as_view(), name='operator_delete'),
    path("menu_packages", MenuPackages.as_view(), name='menu_packages'),
    path("menu_services", MenuServices.as_view(), name='menu_services'),
    path("menu_discounts", MenuDiscounts.as_view(), name='menu_discounts'),
    path("assign_package_view", AssignPackageView.as_view(), name='assign_package_view'),
    path("assign_package_discount_view", AssignPackageDiscountView.as_view(), name='assign_package_discount_view'),
    path("operators_package_list_view", OperatorsPackageListView.as_view(), name='operators_package_list_view'),
    path("operators_package_discount_list_view", OperatorsPackageDiscountListView.as_view(), name='operators_package_discount_list_view'),
    path("assign_service_view", AssignServiceView.as_view(), name='assign_service_view'),
    path("assign_service_discount_view", AssignServiceDiscountView.as_view(), name='assign_service_discount_view'),
    path("operators_service_list_view", OperatorsServiceListView.as_view(), name='operators_service_list_view'),
    path("operators_service_discount_list_view", OperatorsServiceDiscountListView.as_view(), name='operators_service_discount_list_view')
]