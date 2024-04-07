# services/urls.py
from django.urls import path
from .views import ServiceTypeListView, ServiceTypeCreateView, ServiceTypeUpdateView, ServiceTypeDeleteView
from .views import ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView
from .views import ServiceDiscountListView, ServiceDiscountCreateView, ServiceDiscountUpdateView, ServiceDiscountDeleteView
from .views import ServiceDiscountServiceListView, ServiceDiscountServiceCreateView, ServiceDiscountServiceUpdateView, ServiceDiscountServiceDeleteView
from .views import InvoiceServiceListView, InvoiceServiceCreateView, InvoiceServiceDeleteView, InvoiceServiceUpdateView

app_name = 'services'

urlpatterns = [
    #for service-types
    path('service-types/', ServiceTypeListView.as_view(), name='service_type_list'), #read
    path('service-types/new/', ServiceTypeCreateView.as_view(), name='service_type_create'), #create
    path('service-types/<int:id_service_type>/edit/', ServiceTypeUpdateView.as_view(), name='service_type_update'), #update
    path('service-types/<int:id_service_type>/delete/', ServiceTypeDeleteView.as_view(), name='service_type_delete'), #delete
    #for service
    path('service/', ServiceListView.as_view(), name='service_list'), #read
    path('service/new/', ServiceCreateView.as_view(), name='service_create'),  # create
    path('service/<int:id_service>/edit/', ServiceUpdateView.as_view(), name='service_update'), #update
    path('service/<int:id_service>/delete/', ServiceDeleteView.as_view(), name='service_delete'), #delete
    #for service-discount
    path('service-discount/', ServiceDiscountListView.as_view(), name='service_discount_list'), #read
    path('service-discount/new/', ServiceDiscountCreateView.as_view(), name='service_discount_create'), #create
    path('service-discount/<int:id_service_discount>/edit/', ServiceDiscountUpdateView.as_view(), name='service_discount_update'), #update
    path('service-discount/<int:id_service_discount>/delete/', ServiceDiscountDeleteView.as_view(), name='service_discount_delete'), #delete
    #for service-discount-service
    path('service-discount-service/', ServiceDiscountServiceListView.as_view(), name='service_discount_service_list'), #read
    path('service-discount-service/new/', ServiceDiscountServiceCreateView.as_view(), name='service_discount_service_create'), #create
    path('service-discount-service/<int:id_service_discount>/edit/', ServiceDiscountServiceUpdateView.as_view(), name='service_discount_service_update'), #update
    path('service-discount-service/<int:id_service_discount>/delete/', ServiceDiscountServiceDeleteView.as_view(), name='service_discount_service_delete'), #delete
    #for invoice-service
    path('invoice-service/', InvoiceServiceListView.as_view(), name='invoice_service_list'), #read
    path('invoice-service/new/', InvoiceServiceCreateView.as_view(), name='invoice_service_create'), #create
    path('invoice-service/<int:id_invoice_service>/edit/', InvoiceServiceUpdateView.as_view(), name='invoice_service_update'), #update
    path('invoice-service/<int:id_invoice_service>/delete/', InvoiceServiceDeleteView.as_view(), name='invoice_service_delete'), #delete
]
