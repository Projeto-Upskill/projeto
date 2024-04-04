from django.urls import path
from .views import (CustomerCreateView,
                    CustomerListView,
                    CustomerUpdateView,
                    view_customer_package,
                    view_customer_unique_service,
                    update_customer_data)

app_name = 'customers'

urlpatterns = [
    path("create", CustomerCreateView.as_view(), name='create_customer'),
    path("list", CustomerListView.as_view(), name='customer_list'),
    path("<int:id_customer>/update", CustomerUpdateView.as_view(), name='customer_update'),
    path('package/', view_customer_package, name='view_customer_package'),
    path('unique_service/', view_customer_unique_service, name='view_customer_unique_service'),
    #path('customer/promotions/', views.view_customer_promotions, name='view_customer_promotions'),
    path('update/', update_customer_data, name='update_customer_data'),
    #path('available/packages/', views.view_available_packages, name='view_available_packages'),
    # path('available/unique_services/', views.view_available_unique_services, name='view_available_unique_services'),
    # path('available/promotions/', views.view_available_promotions, name='view_available_promotions'),
]
