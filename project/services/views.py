from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ServiceType, Service, ServiceDiscount, ServiceDiscountService, InvoiceService
from .forms import ServiceTypeForm, ServiceForm, ServiceDiscountForm, ServiceDiscountServiceForm, InvoiceServiceForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin



class ServiceTypeListView(ListView):
    model = ServiceType
    template_name = 'service_type_list.html'
    context_object_name = 'service_types'


class ServiceTypeCreateView(PermissionRequiredMixin, CreateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'service_type_form.html'
    success_url = reverse_lazy('services:service_type_list')
    permission_required = 'services.add_servicetype'

class ServiceTypeUpdateView(PermissionRequiredMixin, UpdateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'service_type_form.html'
    success_url = reverse_lazy('services:service_type_list')
    permission_required = 'services.change_servicetype'

    def get_object(self):
        id = self.kwargs.get('id_service_type')
        return get_object_or_404(ServiceType, id_service_type=id)


class ServiceTypeDeleteView(PermissionRequiredMixin, DeleteView):
    model = ServiceType
    template_name = 'service_type_confirm_delete.html'
    success_url = reverse_lazy('services:service_type_list')
    permission_required = 'services.delete_servicetype'

    def get_object(self):
        id = self.kwargs.get('id_service_type')
        return get_object_or_404(ServiceType, id_service_type=id)



#Let's create views for services


class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'service'


class ServiceCreateView(PermissionRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('services:service_list')
    permission_required = 'services.add_service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_types'] = ServiceType.objects.all()
        return context


class ServiceUpdateView(PermissionRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('services:service_list')
    permission_required = 'services.change_service'

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(Service, id_service=id)


class ServiceDeleteView(PermissionRequiredMixin, DeleteView):
    model = Service
    template_name = 'service_confirm_delete.html'
    success_url = reverse_lazy('services:service_list')
    permission_required = 'services.delete_service'

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(Service, id_service=id)



#Let's create views for ServiceDiscount

class ServiceDiscountListView(ListView):
    model = ServiceDiscount
    template_name = 'service_discount_list.html'
    context_object_name = 'service_discount'


class ServiceDiscountCreateView(PermissionRequiredMixin, CreateView):
    model = ServiceDiscount
    form_class = ServiceDiscountForm
    template_name = 'service_discount_form.html'
    success_url = reverse_lazy('services:service_discount_list')
    permission_required = 'services.add_servicediscount'


class ServiceDiscountUpdateView(PermissionRequiredMixin, UpdateView):
    model = ServiceDiscount
    form_class = ServiceDiscountForm
    template_name = 'service_discount_form.html'
    success_url = reverse_lazy('services:service_discount_list')
    permission_required = 'services.change_servicediscount'

    def get_object(self):
        id = self.kwargs.get('id_service_discount')
        return get_object_or_404(ServiceDiscount, id_service_discount=id)


class ServiceDiscountDeleteView(PermissionRequiredMixin, DeleteView):
    model = ServiceDiscount
    template_name = 'service_discount_confirm_delete.html'
    success_url = reverse_lazy('services:service_discount_list')
    permission_required = 'services.delete_servicediscount'

    def get_object(self):
        id = self.kwargs.get('id_service_discount')
        return get_object_or_404(ServiceDiscount, id_service_discount=id)


#Let's create views for ServiceDiscountService

class ServiceDiscountServiceListView(PermissionRequiredMixin, ListView):
    model = ServiceDiscountService
    template_name = 'service_discount_service_list.html'
    context_object_name = 'service_discount_service'
    permission_required = 'services.view_servicediscountservice'


class ServiceDiscountServiceCreateView(PermissionRequiredMixin, CreateView):
    model = ServiceDiscountService
    form_class = ServiceDiscountServiceForm
    template_name = 'service_discount_service_form.html'
    success_url = reverse_lazy('services:service_discount_service_list')
    permission_required = 'services.add_servicediscountservice'


class ServiceDiscountServiceUpdateView(PermissionRequiredMixin, UpdateView):
    model = ServiceDiscountService
    form_class = ServiceDiscountServiceForm
    template_name = 'service_discount_service_form.html'
    success_url = reverse_lazy('services:service_discount_service_list')
    permission_required = 'services.change_servicediscountservice'

    def get_object(self):
        id = self.kwargs.get('id_service_discount_service')
        return get_object_or_404(ServiceDiscountService, id_service_discount_service=id)


class ServiceDiscountServiceDeleteView(PermissionRequiredMixin, DeleteView):
    model = ServiceDiscountService
    template_name = 'service_discount_service_confirm_delete.html'
    success_url = reverse_lazy('services:service_discount_service_list')
    permission_required = 'services.delete_servicediscountservice'

    def get_object(self):
        id = self.kwargs.get('id_service_discount_service')
        return get_object_or_404(ServiceDiscountService, id_service_discount_service=id)


#Let's create views for InvoiceService

class InvoiceServiceListView(PermissionRequiredMixin, ListView):
    model = InvoiceService
    template_name = 'invoice_service_list.html'
    context_object_name = 'invoice_service'
    permission_required = 'services.view_invoiceservice'


class InvoiceServiceCreateView(PermissionRequiredMixin, CreateView):
    model = InvoiceService
    form_class = InvoiceServiceForm
    template_name = 'invoice_service_form.html'
    success_url = reverse_lazy('services:invoice_service_list')
    permission_required = 'services.add_invoiceservice'


class InvoiceServiceUpdateView(PermissionRequiredMixin, UpdateView):
    model = InvoiceService
    form_class = InvoiceServiceForm
    template_name = 'invoice_service_form.html'
    success_url = reverse_lazy('services:invoice_service_list')
    permission_required = 'services.change_invoiceservice'

    def get_object(self):
        id = self.kwargs.get('id_invoice_service')
        return get_object_or_404(InvoiceService, id_invoice_service=id)


class InvoiceServiceDeleteView(PermissionRequiredMixin, DeleteView):
    model = InvoiceService
    template_name = 'invoice_service_confirm_delete.html'
    success_url = reverse_lazy('services:invoice_service_list')
    permission_required = 'services.delete_invoiceservice'

    def get_object(self):
        id = self.kwargs.get('id_invoice_service')
        return get_object_or_404(InvoiceService, id_invoice_service=id)