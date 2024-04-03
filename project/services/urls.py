# services/urls.py
from django.urls import path
from .views import ServiceTypeListView, ServiceTypeCreateView, ServiceTypeUpdateView, ServiceTypeDeleteView

app_name = 'services'

urlpatterns = [
    path('service-types/', ServiceTypeListView.as_view(), name='service_type_list'), #read
    path('service-types/new/', ServiceTypeCreateView.as_view(), name='service_type_create'), #create
    path('service-types/<int:id_service_type>/edit/', ServiceTypeUpdateView.as_view(), name='service_type_update'), #update
    path('service-types/<int:id_service_type>/delete/', ServiceTypeDeleteView.as_view(), name='service_type_delete'), #delete
]
