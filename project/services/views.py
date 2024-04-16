from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ServiceType, Service, ServiceDiscount, ServiceDiscountService, InvoiceService
from .forms import ServiceTypeForm, ServiceForm, ServiceDiscountForm, ServiceDiscountServiceForm, InvoiceServiceForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_types'] = ServiceType.objects.all()
        return context


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('services:service_list')

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(Service, id_service=id)


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service_confirm_delete.html'
    success_url = reverse_lazy('services:service_list')

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(Service, id_service=id)



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
        return get_object_or_404(ServiceDiscount, id_service_discount=id)


class ServiceDiscountDeleteView(DeleteView):
    model = ServiceDiscount
    template_name = 'service_discount_confirm_delete.html'
    success_url = reverse_lazy('services:service_discount_list')

    def get_object(self):
        id = self.kwargs.get('id_service_discount')
        return get_object_or_404(ServiceDiscount, id_service_discount=id)


#Let's create views for ServiceDiscountService

class ServiceDiscountServiceListView(ListView):
    model = ServiceDiscountService
    template_name = 'service_discount_service_list.html'
    context_object_name = 'service_discount_service'


class ServiceDiscountServiceCreateView(CreateView):
    model = ServiceDiscountService
    form_class = ServiceDiscountServiceForm
    template_name = 'service_discount_service_form.html'
    success_url = reverse_lazy('services:service_discount_service_list')


class ServiceDiscountServiceUpdateView(UpdateView):
    model = ServiceDiscountService
    form_class = ServiceDiscountServiceForm
    template_name = 'service_discount_service_form.html'
    success_url = reverse_lazy('services:service_discount_service_list')

    def get_object(self):
        id = self.kwargs.get('id_service_discount_service')
        return get_object_or_404(ServiceDiscountService, id_service_discount_service=id)


class ServiceDiscountServiceDeleteView(DeleteView):
    model = ServiceDiscountService
    template_name = 'service_discount_service_confirm_delete.html'
    success_url = reverse_lazy('services:service_discount_service_list')

    def get_object(self):
        id = self.kwargs.get('id_service_discount_service')
        return get_object_or_404(ServiceDiscountService, id_service_discount_service=id)


#Let's create views for InvoiceService

class InvoiceServiceListView(ListView):
    model = InvoiceService
    template_name = 'invoice_service_list.html'
    context_object_name = 'invoice_service'


class InvoiceServiceCreateView(CreateView):
    model = InvoiceService
    form_class = InvoiceServiceForm
    template_name = 'invoice_service_form.html'
    success_url = reverse_lazy('services:invoice_service_list')


class InvoiceServiceUpdateView(UpdateView):
    model = InvoiceService
    form_class = InvoiceServiceForm
    template_name = 'invoice_service_form.html'
    success_url = reverse_lazy('services:invoice_service_list')

    def get_object(self):
        id = self.kwargs.get('id_invoice_service')
        return get_object_or_404(InvoiceService, id_invoice_service=id)


class InvoiceServiceDeleteView(DeleteView):
    model = InvoiceService
    template_name = 'invoice_service_confirm_delete.html'
    success_url = reverse_lazy('services:invoice_service_list')

    def get_object(self):
        id = self.kwargs.get('id_invoice_service')
        return get_object_or_404(InvoiceService, id_invoice_service=id)