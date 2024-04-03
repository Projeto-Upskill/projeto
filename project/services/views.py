from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ServiceType, Service, ServiceDiscount
from .forms import ServiceTypeForm, ServiceForm, ServiceDiscountForm
from django.shortcuts import get_object_or_404


class ServiceTypeListView(ListView):
    model = ServiceType
    template_name = 'service_type_list.html'
    context_object_name = 'service_types'

class ServiceTypeCreateView(CreateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'service_type_form.html'
    success_url = reverse_lazy('services:service_type_list')

class ServiceTypeUpdateView(UpdateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'service_type_form.html'
    success_url = reverse_lazy('services:service_type_list')

    def get_object(self):
        id = self.kwargs.get('id_service_type')
        return get_object_or_404(ServiceType, id_service_type=id)

class ServiceTypeDeleteView(DeleteView):
    model = ServiceType
    template_name = 'service_type_confirm_delete.html'
    success_url = reverse_lazy('services:service_type_list')

    def get_object(self):
        id = self.kwargs.get('id_service_type')
        return get_object_or_404(ServiceType, id_service_type=id)

#Let's create views for services

class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('services:service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('services:service_list')

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(ServiceType, id_service=id)

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service_confirm_delete.html'
    success_url = reverse_lazy('services:service_list')

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(ServiceType, id_service=id)

#Let's create views for ServiceDiscount

class ServiceDiscountListView(ListView):
    model = ServiceDiscount
    template_name = 'service_discount_list.html'
    context_object_name = 'service_discount'

class ServiceDiscountCreateView(CreateView):
    model = ServiceDiscount
    form_class = ServiceDiscountForm
    template_name = 'service_discount_form.html'
    success_url = reverse_lazy('services:service_discount_list')

class ServiceDiscountUpdateView(UpdateView):
    model = ServiceDiscount
    form_class = ServiceDiscountForm
    template_name = 'service_discount_form.html'
    success_url = reverse_lazy('services:service_discount_list')

    def get_object(self):
        id = self.kwargs.get('id_service_discount')
        return get_object_or_404(ServiceType, id_service_discount=id)

class ServiceDiscountDeleteView(DeleteView):
    model = ServiceDiscount
    template_name = 'service_discount_confirm_delete.html'
    success_url = reverse_lazy('services:service_discount_list')

    def get_object(self):
        id = self.kwargs.get('id_service_discount')
        return get_object_or_404(ServiceType, id_service_discount=id)

