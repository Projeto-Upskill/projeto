from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .forms import OperatorsForm
from .models import Operators
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

class OperatorsCreateView(CreateView):
    template_name = 'operators_create.html'
    form_class = OperatorsForm
    success_url = reverse_lazy('operators:operator_index')

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
    success_url = reverse_lazy("operators_list")

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
        return reverse_lazy('operators_list')


class OperatorsIndex(TemplateView):
    template_name = 'index_operators.html'


class MenuCustomers(TemplateView):
    template_name = 'menu_customers.html'


class MenuPackages(TemplateView):
    template_name = 'menu_packages.html'


class MenuDiscounts(TemplateView):
    template_name = 'menu_discounts.html'
    
    
