from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ServiceType, Service
from .forms import ServiceTypeForm, ServiceForm
from django.shortcuts import get_object_or_404


class ServiceTypeListView(ListView):
    model = ServiceType
    template_name = 'services/templates/service_type_list.html'
    context_object_name = 'service_types'

class ServiceTypeCreateView(CreateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'services/templates/service_type_form.html'
    success_url = reverse_lazy('services:service_type_list')

class ServiceTypeUpdateView(UpdateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'services/templates/service_type_form.html'
    success_url = reverse_lazy('services:service_type_list')

    def get_object(self):
        id = self.kwargs.get('id_service_type')
        return get_object_or_404(ServiceType, id_service_type=id)

class ServiceTypeDeleteView(DeleteView):
    model = ServiceType
    template_name = 'services/templates/service_type_confirm_delete.html'
    success_url = reverse_lazy('services:service_type_list')

    def get_object(self):
        id = self.kwargs.get('id_service_type')
        return get_object_or_404(ServiceType, id_service_type=id)

#Let's create views for services

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:service_list')

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(ServiceType, id_service=id)

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('services:service_list')

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(ServiceType, id_service=id)


