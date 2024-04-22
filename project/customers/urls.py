from django.urls import path
from .views import (CustomerCreateView,
                    CustomerListView,
                    CustomerUpdateView,
                    CustomerDeleteView,
                    AddressCreateView,
                    AddressListView,
                    AddressUpdateView,
                    AddressDeleteView,
                    RegistrationView,
                    RegistrationListView,
                    RegistrationUpdateView,
                    view_customer_package,
                    view_customer_unique_service,
                    update_customer_data,
                    register_customer,
                    CustomerDashboardView)



app_name = 'customers'

urlpatterns = [
    path("create", CustomerCreateView.as_view(), name='create_customer'),
    path("list", CustomerListView.as_view(), name='customer_list'),
    path("<int:id_customer>/update", CustomerUpdateView.as_view(), name='customer_update'),
    path("<int:id_customer>/delete", CustomerDeleteView.as_view(), name='customer_delete'),
    path("address_create", AddressCreateView.as_view(), name='address_create'),
    path("address_list", AddressListView.as_view(), name='address_list'),
    path("<int:id_address>/address_update", AddressUpdateView.as_view(), name="address_update"),
    path("<int:id_address>/address_delete", AddressDeleteView.as_view(), name="address_delete"),
    path("registration", RegistrationView.as_view(), name="registration"),
    path("registration_list", RegistrationListView.as_view(), name='registration_list'),
    path("<int:id_customer>/<int:id_address>/registration_update",
         RegistrationUpdateView.as_view(), name="registration_update"),
    path('package/', view_customer_package, name='view_customer_package'),
    path('unique_service/', view_customer_unique_service, name='view_customer_unique_service'),
    #path('customer/promotions/', views.view_customer_promotions, name='view_customer_promotions'),
    path('update/', update_customer_data, name='update_customer_data'),
    #path('available/packages/', views.view_available_packages, name='view_available_packages'),
    # path('available/unique_services/', views.view_available_unique_services, name='view_available_unique_services'),
    # path('available/promotions/', views.view_available_promotions, name='view_available_promotions'),
    path('register/', register_customer, name='register_customer'),
    path('dashboard/', CustomerDashboardView.as_view(), name='customer_dashboard'),
]
