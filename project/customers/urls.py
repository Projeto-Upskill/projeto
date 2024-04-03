from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('package/', views.view_customer_package, name='view_customer_package'),
    path('unique_service/', views.view_customer_unique_service, name='view_customer_unique_service'),
    #path('customer/promotions/', views.view_customer_promotions, name='view_customer_promotions'),
    path('update/', views.update_customer_data, name='update_customer_data'),
    #path('available/packages/', views.view_available_packages, name='view_available_packages'),
    # path('available/unique_services/', views.view_available_unique_services, name='view_available_unique_services'),
    # path('available/promotions/', views.view_available_promotions, name='view_available_promotions'),
]
