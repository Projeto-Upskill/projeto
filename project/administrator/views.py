from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .forms import AdministratorForm, AdministratorUpdateForm
from .models import Administrator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.db.models import Q
from project.views import *
from .permissions import *

admin = Administrator()
administrator_group_permissions = Group.objects.get(name='administrator_group')


class AdministratorCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'administrator_create.html'
    form_class = AdministratorForm
    permission_required = "project.add_administrator"
    success_url = reverse_lazy("project:system_admin")

    def handle_no_permission(self):
        return redirect("forbidden")

    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        birth_date = form.cleaned_data["birth_date"]
        active = form.cleaned_data["active"]
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = User.objects.create_user(username=username, password=password)
        user.is_active = active

        user.save()

        administrator = Administrator.objects.create(user=user, first_name=first_name, last_name=last_name,
                                                     email=email, birth_date=birth_date, active=active)

        administrator.user.groups.add(administrator_group_permissions)

        return redirect("system_admin")


class AdministratorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Administrator
    template_name = 'administrator_list.html'
    permission_required = "project.view_administrator"
    context_object_name = 'administrator_list'

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_queryset(self):
        first_name = self.request.GET.get('first_name')
        last_name = self.request.GET.get('last_name')

        queryset = super().get_queryset()

        if first_name:
            queryset = queryset.filter(Q(first_name__icontains=first_name))
        if last_name:
            queryset = queryset.filter(Q(last_name__icontains=last_name))

        return queryset.order_by('first_name')


class AdministratorUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'administrator_create.html'
    form_class = AdministratorUpdateForm
    permission_required = "project.change_administrator"
    success_url = reverse_lazy("administrator:administrator_list")

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self):
        id_administrator = self.kwargs.get('id_administrator')
        return get_object_or_404(Administrator, id_administrator=id_administrator)

    def form_valid(self, form):
        form.first_name = form.cleaned_data["first_name"]
        form.last_name = form.cleaned_data["last_name"]
        form.instance.email = form.cleaned_data["email"]
        form.instance.birth_date = form.cleaned_data["birth_date"]
        form.instance.active = form.cleaned_data["active"]

        return super().form_valid(form)


class AdministratorDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Administrator
    template_name = 'administrator_confirm_delete.html'
    permission_required = "project.delete_administrator"

    def handle_no_permission(self):
        return redirect("forbidden")

    def get_object(self, queryset=None):
        id_administrator = self.kwargs.get('id_administrator')
        return get_object_or_404(Administrator, id_administrator=id_administrator)

    def get_success_url(self):
        return reverse_lazy('administrator:administrator_list')


class AdministratorIndex(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'index_administrator.html'
    permission_required = "administrator.view_administrator_index"

    def handle_no_permission(self):
        return redirect("forbidden")


class MenuOperators(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'operators.html'
    permission_required = "administrator.view_menu_operators"

    def handle_no_permission(self):
        return redirect("forbidden")


class MenuCustomers(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'customers.html'
    permission_required = "administrator.view_menu_customers"

    def handle_no_permission(self):
        return redirect("forbidden")


class MenuPackages(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'packages.html'
    permission_required = "administrator.view_menu_packages"

    def handle_no_permission(self):
        return redirect("forbidden")


class MenuDiscounts(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'discounts.html'
    permission_required = "administrator.view_menu_discounts"

    def handle_no_permission(self):
        return redirect("forbidden")


class MenuServices(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'services.html'
    permission_required = "administrator.view_menu_services"

    def handle_no_permission(self):
        return redirect("forbidden")
