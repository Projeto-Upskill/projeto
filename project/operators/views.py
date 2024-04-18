from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, View
from .forms import OperatorsForm
from .models import Operators
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from packages.models import Package, PackageDiscount
from services.models import Service, ServiceDiscount
from packages.forms import PackageForm, PackageDiscountForm
from services.forms import ServiceForm, ServiceDiscountForm
from .permissions import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import PermissionRequiredMixin


operators_permissions_group = Group.objects.get(name="operator_group")



class OperatorsCreateView(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    template_name = 'operators_create.html'
    form_class = OperatorsForm
    permission_required = "administrator.add_operators"
    success_url = reverse_lazy('administrator:administrator_index')
    permission_required = 'operators.add_operator'

    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        birth_date = form.cleaned_data["birth_date"]
        admission_date = form.cleaned_data["admission_date"]
        active = form.cleaned_data["active"]
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = User.objects.create_user(username=username, password=password)
        user.is_active = active

        user.save()
        operator_group, created = Group.objects.get_or_create(name='operator_group')
        operator_group.user_set.add(user)

        operator = Operators.objects.create(user=user, first_name=first_name, last_name=last_name,
                                            email=email, birth_date=birth_date, admission_date=admission_date,
                                            active=active)

        operator.user.groups.add(operators_permissions_group)

        return redirect("administrator:administrator_index")


class OperatorsListView(ListView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Operators
    template_name = 'operators_list.html'
    permission_required = "administrator.view_operators"
    context_object_name = 'operators_list'
    permission_required = 'operators.view_operator'



class OperatorsUpdateView(UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    template_name = 'operators_create.html'
    form_class = OperatorsForm
    permission_required = 'administrator.change_operators'
    success_url = reverse_lazy("operators:operator_list")
    permission_required = 'operators.change_operator'

    def get_object(self):
        id_operator = self.kwargs.get('id_operator')
        return get_object_or_404(Operators, id_operator=id_operator)

    def form_valid(self, form):
        form.instance.name = form.cleaned_data["first_name"]
        form.instance.name = form.cleaned_data["last_name"]
        form.instance.email = form.cleaned_data["email"]
        form.instance.birth_date = form.cleaned_data["birth_date"]
        form.instance.admission_date = form.cleaned_data["admission_date"]
        form.instance.active = form.cleaned_data["active"]

        return super().form_valid(form)



class OperatorsDeleteView(DeleteView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Operators
    template_name = 'operators_confirm_delete.html'
    permission_required = "administrator.delete_operators"

    def get_object(self, queryset=None):
        id_operator = self.kwargs.get('id_operator')
        return get_object_or_404(Operators, id_operator=id_operator)

    def get_success_url(self):
        return reverse_lazy('operators:operator_list')


class OperatorsIndex(PermissionRequiredMixin, TemplateView):
    template_name = 'index_operators.html'
    permission_required = 'operators.view_operator'


class MenuCustomers(PermissionRequiredMixin, TemplateView):
    template_name = 'menu_customers.html'
    permission_required = 'operators.view_menucustomers'

class MenuPackages(PermissionRequiredMixin, TemplateView):
    template_name = 'menu_packages.html'
    permission_required = 'operators.view_menupackages'

class MenuDiscounts(PermissionRequiredMixin, TemplateView):
    template_name = 'menu_discounts.html'
    permission_required = 'operators.view_menudiscounts'


# Views operators packages and services

class AssignPackageView(PermissionRequiredMixin, View):
    template_name = 'assign_package.html'
    form_class = PackageForm
    model = Package
    success_url = reverse_lazy('operators_list')
    permission_required = 'packages.add_package'

    def form_valid(self, form):
        # Atribuir um pacote comercial a um cliente
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Lógica para atribuir um pacote comercial a um cliente
            return redirect('operators_list')  # Redirecionar para a página de lista de operadores após o sucesso
        return render(request, self.template_name, {'form': form})


class AssignPackageDiscountView(PermissionRequiredMixin, View):
    template_name = 'assign_package_discount.html'
    form_class = PackageDiscountForm
    model = PackageDiscount
    success_url = reverse_lazy('operators_list')
    permission_required = 'packages.add_packagediscount'

    def form_valid(self, form):
        # Atribuir uma promoção a um pacote comercial
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Lógica para atribuir uma promoção a um pacote comercial
            return redirect('operators_list')  # Redirecionar para a página de lista de operadores após o sucesso
        return render(request, self.template_name, {'form': form})


class OperatorsPackageListView(PermissionRequiredMixin, ListView):
    model = Package
    template_name = 'operators_package_list.html'
    context_object_name = 'package_list'
    permission_required = 'packages.view_package'


class OperatorsPackageDiscountListView(PermissionRequiredMixin, ListView):
    model = PackageDiscount
    template_name = 'operators_package_discount_list.html'
    context_object_name = 'package_discount_list'
    permission_required = 'packages.view_packagediscount'

class AssignServiceView(PermissionRequiredMixin, View):
    template_name = 'assign_service.html'
    form_class = ServiceForm
    model = Service
    success_url = reverse_lazy('operators_list')
    permission_required = 'services.add_service'

    def form_valid(self, form):
        # Atribuir um serviço a um cliente
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Lógica para atribuir um serviço a um cliente
            return redirect('operators_list')  # Redirecionar para a página de lista de operadores após o sucesso
        return render(request, self.template_name, {'form': form})


class AssignServiceDiscountView(PermissionRequiredMixin, View):
    template_name = 'assign_service_discount.html'
    form_class = ServiceDiscountForm
    model = ServiceDiscount
    success_url = reverse_lazy('operators_list')
    permission_required = 'services.add_servicediscount'

    def form_valid(self, form):
        # Atribuir uma promoção a um serviço
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Lógica para atribuir uma promoção a um serviço
            return redirect('operators_list')  # Redirecionar para a página de lista de operadores após o sucesso
        return render(request, self.template_name, {'form': form})


class OperatorsServiceListView(PermissionRequiredMixin, ListView):
    model = Service
    template_name = 'operators_service_list.html'
    context_object_name = 'service_list'
    permission_required = 'services.view_service'


class OperatorsServiceDiscountListView(PermissionRequiredMixin, ListView):
    model = ServiceDiscount
    template_name = 'operators_service_discount_list.html'
    context_object_name = 'service_discount_list'
    permission_required = 'services.view_servicediscount'
