from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ServiceType, Service, ServiceDiscount, ServiceDiscountService, InvoiceService, ServiceCustomer
from .forms import ServiceTypeForm, ServiceForm, ServiceDiscountForm, ServiceDiscountServiceForm, InvoiceServiceForm, CustomerServiceForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from customers.models import Customer


class ServiceTypeListView(ListView):
    model = ServiceType
    template_name = 'service_type_list.html'
    context_object_name = 'service_types'


class ServiceTypeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'service_type_form.html'
    success_url = reverse_lazy('services:service_type_list')
    permission_required = 'services.add_servicetype'

    def handle_no_permission(self):
        return redirect("forbidden")


class ServiceTypeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = ServiceType
    form_class = ServiceTypeForm
    template_name = 'service_type_form.html'
    success_url = reverse_lazy('services:service_type_list')
    permission_required = 'services.change_servicetype'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_service_type')
        return get_object_or_404(ServiceType, id_service_type=id)


class ServiceTypeDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = ServiceType
    template_name = 'service_type_confirm_delete.html'
    success_url = reverse_lazy('services:service_type_list')
    permission_required = 'services.delete_servicetype'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_service_type')
        return get_object_or_404(ServiceType, id_service_type=id)


class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'service'


class ServiceCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('services:service_list')
    permission_required = 'services.add_service'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_types'] = ServiceType.objects.all()
        return context


class ServiceUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('services:service_list')
    permission_required = 'services.change_service'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(Service, id_service=id)


class ServiceDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Service
    template_name = 'service_confirm_delete.html'
    success_url = reverse_lazy('services:service_list')
    permission_required = 'services.delete_service'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_service')
        return get_object_or_404(Service, id_service=id)


class ServiceDiscountListView(ListView):
    model = ServiceDiscount
    template_name = 'service_discount_list.html'
    context_object_name = 'service_discount'


class ServiceDiscountCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = ServiceDiscount
    form_class = ServiceDiscountForm
    template_name = 'service_discount_form.html'
    success_url = reverse_lazy('services:service_discount_list')
    permission_required = 'services.add_servicediscount'

    def handle_no_permission(self):
        return redirect("forbidden")


class ServiceDiscountUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = ServiceDiscount
    form_class = ServiceDiscountForm
    template_name = 'service_discount_form.html'
    success_url = reverse_lazy('services:service_discount_list')
    permission_required = 'services.change_servicediscount'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_service_discount')
        return get_object_or_404(ServiceDiscount, id_service_discount=id)


class ServiceDiscountDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = ServiceDiscount
    template_name = 'service_discount_confirm_delete.html'
    success_url = reverse_lazy('services:service_discount_list')
    permission_required = 'services.delete_servicediscount'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_service_discount')
        return get_object_or_404(ServiceDiscount, id_service_discount=id)


class ServiceDiscountServiceListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = ServiceDiscountService
    template_name = 'service_discount_service_list.html'
    context_object_name = 'service_discount_service'
    permission_required = 'services.view_servicediscountservice'

    def handle_no_permission(self):
        return redirect("forbidden")


class ServiceDiscountServiceCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = ServiceDiscountService
    form_class = ServiceDiscountServiceForm
    template_name = 'service_discount_service_form.html'
    success_url = reverse_lazy('services:service_discount_service_list')
    permission_required = 'services.add_servicediscountservice'

    def handle_no_permission(self):
        return redirect("forbidden")


class ServiceDiscountServiceUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = ServiceDiscountService
    form_class = ServiceDiscountServiceForm
    template_name = 'service_discount_service_form.html'
    success_url = reverse_lazy('services:service_discount_service_list')
    permission_required = 'services.change_servicediscountservice'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_service_discount_service')
        return get_object_or_404(ServiceDiscountService, id_service_discount_service=id)


class ServiceDiscountServiceDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = ServiceDiscountService
    template_name = 'service_discount_service_confirm_delete.html'
    success_url = reverse_lazy('services:service_discount_service_list')
    permission_required = 'services.delete_servicediscountservice'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_service_discount_service')
        return get_object_or_404(ServiceDiscountService, id_service_discount_service=id)


class ServiceCustomerCreateView(CreateView):
    model = ServiceCustomer
    form_class = CustomerServiceForm
    template_name = 'service_customer_create.html'
    success_url = reverse_lazy('administrator:menu_services')


class ServiceCustomerUpdateView(UpdateView):
    model = ServiceCustomer
    form_class = CustomerServiceForm
    template_name = 'service_customer_create.html'
    success_url = reverse_lazy('administrator:menu_services')

    def get_object(self):
        id_service_customer = self.kwargs.get("id_service_customer")
        return get_object_or_404(ServiceCustomer, id_service_customer=id_service_customer)


class ServiceCustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ServiceCustomer
    template_name = 'service_client_list.html'
    context_object_name = 'service_customer'
    permission_required = 'services.view_servicecustomer'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_queryset(self):
        service = self.request.GET.get('id_service')
        user = self.request.user
        if service:
            object_list = self.model.objects.filter(Q(service__incontains=service), user_id=user)
        else:
            object_list = self.model.objects.filter(user_id=user)
        return object_list


class InvoiceServiceListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = InvoiceService
    template_name = 'invoice_service_list.html'
    context_object_name = 'invoice_service'
    permission_required = 'services.view_invoiceservice'

    def handle_no_permission(self):
        return redirect("forbidden")


class InvoiceServiceCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = InvoiceService
    form_class = InvoiceServiceForm
    template_name = 'invoice_service_form.html'
    success_url = reverse_lazy('services:invoice_service_list')
    permission_required = 'services.add_invoiceservice'

    def handle_no_permission(self):
        return redirect("forbidden")


class InvoiceServiceUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = InvoiceService
    form_class = InvoiceServiceForm
    template_name = 'invoice_service_form.html'
    success_url = reverse_lazy('services:invoice_service_list')
    permission_required = 'services.change_invoiceservice'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_invoice_service')
        return get_object_or_404(InvoiceService, id_invoice_service=id)


class InvoiceServiceDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = InvoiceService
    template_name = 'invoice_service_confirm_delete.html'
    success_url = reverse_lazy('services:invoice_service_list')
    permission_required = 'services.delete_invoiceservice'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id = self.kwargs.get('id_invoice_service')
        return get_object_or_404(InvoiceService, id_invoice_service=id)
