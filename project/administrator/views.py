from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .forms import AdministratorForm
from .models import Administrator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

admin = Administrator()


class AdministratorCreateView(CreateView):
    template_name = 'administrator_create.html'
    form_class = AdministratorForm
    success_url = reverse_lazy("project:system_admin")

    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        birth_date = form.cleaned_data["birth_date"]
        active = form.cleaned_data["active"]
        username = f"{last_name.split()[0]}.{first_name.split()[-1]}"
        password = admin.generate_password

        user = User.objects.create_user(username, password)
        user.is_active = active

        user.save()

        administrator = Administrator.objects.create(user=user, first_name=first_name, last_name=last_name, email=email,
                                                     birth_date=birth_date, active=active)

        admin.send_welcome_email(user)

        return redirect("system_admin")


class AdministratorListView(ListView):
    model = Administrator
    template_name = 'administrator_list.html'
    context_object_name = 'administrator_list'


class AdministratorUpdateView(UpdateView):
    template_name = 'administrator_create.html'
    form_class = AdministratorForm
    success_url = reverse_lazy("administrator:administrator_list")

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


class AdministratorDeleteView(DeleteView):
    model = Administrator
    template_name = 'administrator_confirm_delete.html'

    def get_object(self, queryset=None):
        id_administrator = self.kwargs.get('id_administrator')
        return get_object_or_404(Administrator, id_administrator=id_administrator)

    def get_success_url(self):
        return reverse_lazy('administrator:administrator_list')


class AdministratorIndex(TemplateView):
    template_name = 'index_administrator.html'


class MenuOperators(TemplateView):
    template_name = 'menu_operators.html'


class MenuCustomers(TemplateView):
    template_name = 'menu_customers.html'


class MenuPackages(TemplateView):
    template_name = 'menu_packages.html'


class MenuDiscounts(TemplateView):
    template_name = 'menu_discounts.html'


class MenuServices(TemplateView):
    template_name = 'menu_services.html'

