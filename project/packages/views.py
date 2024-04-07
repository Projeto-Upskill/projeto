from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Package, PackageDiscount, PackageDiscountPackage, InvoicePackage
from .forms import PackageForm, PackageDiscountForm, PackageDiscountPackageForm, InvoicePackageForm
from django.shortcuts import get_object_or_404


# Let's create views for Package

class PackageListView(ListView):
    model = Package
    template_name = 'package_list.html'
    context_object_name = 'package'


class PackageCreateView(CreateView):
    model = Package
    form_class = PackageForm
    template_name = 'package_form.html'
    success_url = reverse_lazy('packages:package_list')

    def form_valid(self, form):
        form.instance.name = form.cleaned_data["name"]
        form.instance.active = form.cleaned_data["active"]

        return super().form_valid(form)


class PackageUpdateView(UpdateView):
    model = Package
    form_class = PackageForm
    template_name = 'package_form.html'
    success_url = reverse_lazy('packages:package_list')

    def get_object(self):
        id_package = self.kwargs.get('id_package')
        return get_object_or_404(Package, id_package=id_package)

    def form_valid(self, form):
        form.instance.name = form.cleaned_data["name"]
        form.instance.active = form.cleaned_data["active"]

        return super().form_valid(form)


class PackageDeleteView(DeleteView):
    model = Package
    template_name = 'package_confirm_delete.html'
    success_url = reverse_lazy('packages:package_list')

    def get_object(self):
        id_package = self.kwargs.get('id_package')
        return get_object_or_404(Package, id_package=id_package)

    def get_success_url(self):
        return reverse_lazy('packages:package_list')


class PackageIndex(TemplateView):
    template_name = 'index_package.html'


# Let's create views for PackageDiscount


class PackageDiscountListView(ListView):
    model = PackageDiscount
    template_name = 'package_discount_list.html'
    context_object_name = 'package_discount'


class PackageDiscountCreateView(CreateView):
    model = PackageDiscount
    form_class = PackageDiscountForm
    template_name = 'package_discount_form.html'
    success_url = reverse_lazy('packages:package_discount_list')

    def form_valid(self, form):
        form.instance.discount_rate = form.cleaned_data["discount_rate"]
        form.instance.active = form.cleaned_data["active"]
        form.instance.id_package = form.cleaned_data["id_package"]

        return super().form_valid(form)


class PackageDiscountUpdateView(UpdateView):
    model = PackageDiscount
    form_class = PackageDiscountForm
    template_name = 'package_discount_form.html'
    success_url = reverse_lazy('packages:package_discount_list')

    def get_object(self):
        id = self.kwargs.get('id_package_discount')
        return get_object_or_404(PackageDiscount, id_package_discount=id)

    def form_valid(self, form):
        form.instance.discount_rate = form.cleaned_data["discount_rate"]
        form.instance.active = form.cleaned_data["active"]
        form.instance.id_package = form.cleaned_data["id_package"]

        return super().form_valid(form)


class PackageDiscountDeleteView(DeleteView):
    model = PackageDiscount
    template_name = 'package_discount_confirm_delete.html'
    success_url = reverse_lazy('packages:package_discount_list')

    def get_object(self, queryset=None):
        id_package_discount = self.kwargs.get('id_package_discount')
        return get_object_or_404(PackageDiscount, id_package_discount=id_package_discount)

    def get_success_url(self):
        return reverse_lazy('packages:package_list')


# Let's create views for PackageDiscountPackage


class PackageDiscountPackageListView(ListView):
    model = PackageDiscountPackage
    template_name = 'package_discount_package_list.html'
    context_object_name = 'package_discount_package'


class PackageDiscountPackageCreateView(CreateView):
    model = PackageDiscountPackage
    form_class = PackageDiscountPackageForm
    template_name = 'package_discount_package_form.html'
    success_url = reverse_lazy('packages:package_discount_package_list')

    def form_valid(self, form):
        form.instance.id_package = form.cleaned_data["id_package"]
        form.instance.id_package_discount = form.cleaned_data["id_package_discount"]

        return super().form_valid(form)


class PackageDiscountPackageUpdateView(UpdateView):
    model = PackageDiscountPackage
    form_class = PackageDiscountPackageForm
    template_name = 'package_discount_package_form.html'
    success_url = reverse_lazy('packages:package_discount_package_list')

    def get_object(self):
        id = self.kwargs.get('id_package_discount_package')
        return get_object_or_404(PackageDiscountPackage, id_package_discount_package=id)

    def form_valid(self, form):
        form.instance.id_package = form.cleaned_data["id_package"]
        form.instance.id_package_discount = form.cleaned_data["id_package_discount"]

        return super().form_valid(form)


class PackageDiscountPackageDeleteView(DeleteView):
    model = PackageDiscountPackage
    template_name = 'package_discount_package_delete.html'
    success_url = reverse_lazy('packages:package_discount_package_list')

    def get_object(self, queryset=None):
        id_package_discount_package = self.kwargs.get('id_package_discount_package')
        return get_object_or_404(PackageDiscountPackage, id_package_discount_package=id_package_discount_package)


# Let's create views for InvoicePackage

class InvoicePackageListView(ListView):
    model = InvoicePackage
    template_name = 'invoice_package_list.html'
    context_object_name = 'invoice_package'


class InvoicePackageCreateView(CreateView):
    model = InvoicePackage
    form_class = InvoicePackageForm
    template_name = 'invoice_package_form.html'
    success_url = reverse_lazy('packages:invoice_package_list')

    def form_valid(self, form):
        form.id_customer = form.cleaned_data["id_customer"]
        form.id_package = form.cleaned_data["id_package"]
        form.final_package_price = form.cleaned_data["final_package_price"]

        return super().form_valid(form)


class InvoicePackageUpdateView(UpdateView):
    model = InvoicePackage
    form_class = InvoicePackageForm
    template_name = 'invoice_package_form.html'
    success_url = reverse_lazy('packages:invoice_package_list')

    def get_object(self):
        id = self.kwargs.get('id_invoice_package')
        return get_object_or_404(InvoicePackage, id_invoice_package=id)

    def form_valid(self, form):
        form.id_customer = form.cleaned_data["id_customer"]
        form.id_package = form.cleaned_data["id_package"]
        form.final_package_price = form.cleaned_data["final_package_price"]

        return super().form_valid(form)


class InvoicePackageDeleteView(DeleteView):
    model = InvoicePackage
    template_name = 'invoice_package_confirm_delete.html'
    success_url = reverse_lazy('packages:invoice_package_list')

    def get_object(self, queryset=None):
        id_invoice_package = self.kwargs.get('id_invoice_package')
        return get_object_or_404(InvoicePackage, id_invoice_package=id_invoice_package)

    def get_object(self):
        id = self.kwargs.get('id_invoice_package')
        return get_object_or_404(InvoicePackage, id_invoice_package=id)
