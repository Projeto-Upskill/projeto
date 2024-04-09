from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .forms import OperatorsForm
from .models import Operators
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from packages.models import Package, PackageDiscount
from services.models import Service, ServiceDiscount
from packages.forms import PackageForm, PackageDiscountForm
from services.forms import ServiceForm, ServiceDiscountForm

class OperatorsCreateView(CreateView):
    template_name = 'operators_create.html'
    form_class = OperatorsForm
    success_url = reverse_lazy('administrator:administrator_index')

    def form_valid(self, form):
        form.instance.name = form.cleaned_data["name"]
        form.instance.email = form.cleaned_data["email"]
        form.instance.birth_date = form.cleaned_data["birth_date"]
        form.instance.admission_date = form.cleaned_data["admission_date"]
        form.instance.active = form.cleaned_data["active"]

        return super().form_valid(form)
    
class OperatorsListView(ListView):
    model = Operators
    template_name = 'operators_list.html'
    context_object_name = 'operators_list'


class OperatorsUpdateView(UpdateView):
    template_name = 'operators_create.html'
    form_class = OperatorsForm
    success_url = reverse_lazy("operators:operator_list")

    def get_object(self):
        id_operator = self.kwargs.get('id_operator')
        return get_object_or_404(Operators, id_operator=id_operator)

    def form_valid(self, form):
        form.instance.name = form.cleaned_data["name"]
        form.instance.email = form.cleaned_data["email"]
        form.instance.birth_date = form.cleaned_data["birth_date"]
        form.instance.admission_date = form.cleaned_data["admission_date"]
        form.instance.active = form.cleaned_data["active"]

        return super().form_valid(form)


class OperatorsDeleteView(DeleteView):
    model = Operators
    template_name = 'operators_confirm_delete.html'

    def get_object(self, queryset=None):
        id_operator = self.kwargs.get('id_operator')
        return get_object_or_404(Operators, id_operator=id_operator)

    def get_success_url(self):
        return reverse_lazy('operators:operator_list')


class OperatorsIndex(TemplateView):
    template_name = 'index_operators.html'


class MenuCustomers(TemplateView):
    template_name = 'menu_customers.html'


class MenuPackages(TemplateView):
    template_name = 'menu_packages.html'


class MenuDiscounts(TemplateView):
    template_name = 'menu_discounts.html'

#Views operators packages and services

class AssignPackageView(UpdateView):
    template_name = 'assign_package.html'
    form_class = PackageForm
    model = Package
    success_url = reverse_lazy('operators_list')

    def form_valid(self, form):
        # Atribuir um pacote comercial a um cliente
        return super().form_valid(form)

class AssignPackageDiscountView(UpdateView):
    template_name = 'assign_package_discount.html'
    form_class = PackageDiscountForm
    model = PackageDiscount
    success_url = reverse_lazy('operators_list')

    def form_valid(self, form):
        # Atribuir uma promoção a um pacote comercial
        return super().form_valid(form)

class PackageListView(ListView):
    model = Package
    template_name = 'package_list.html'
    context_object_name = 'package_list'

class PackageDiscountListView(ListView):
    model = PackageDiscount
    template_name = 'package_dicount_list.html'
    context_object_name = 'package_discount_list'
    

class AssignServiceView(UpdateView):
    template_name = 'assign_service.html'
    form_class = ServiceForm
    model = Service
    success_url = reverse_lazy('operators_list')

    def form_valid(self, form):
        # Atribuir um serviço a um cliente
        return super().form_valid(form)

class AssignServiceDiscountView(UpdateView):
    template_name = 'assign_service_discount.html'
    form_class = ServiceDiscountForm
    model = ServiceDiscount
    success_url = reverse_lazy('operators_list')

    def form_valid(self, form):
         # Atribuir uma promoção a um serviço
        return super().form_valid(form)

class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'service_list'

class ServiceDiscountListView(ListView):
    model = ServiceDiscount
    template_name = 'service_discount_list.html'
    context_object_name = 'service_discount_list'
    
