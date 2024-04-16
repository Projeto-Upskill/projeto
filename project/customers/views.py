from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Address, PostalCode, City
from .forms import CustomerForm, AddressForm, RegistrationForm, UserCustomerRegistrationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .permissions import *
from django.contrib.auth.mixins import PermissionRequiredMixin


create_group = create_customers_group()

class CustomerCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'customer_create.html'
    form_class = CustomerForm
    success_url = reverse_lazy('administrator:menu_customers')
    permission_required = 'customers.add_customer'


    def form_valid(self, form):
        form.name = form.cleaned_data["name"]
        form.tax_number = form.cleaned_data["tax_number"]
        form.email = form.cleaned_data["email"]
        form.birth_date = form.cleaned_data["birth_date"]
        form.active = form.cleaned_data["active"]

        return super().form_valid(form)


class CustomerListView(PermissionRequiredMixin, ListView):
    template_name = 'customer_list.html'
    model = Customer
    context_object_name = 'customer_list'
    permission_required = 'customers.view_customer'


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'customer_create.html'
    form_class = CustomerForm
    success_url = reverse_lazy("administrator:menu_customers")
    permission_required = 'customers.change_customer'

    def get_object(self):
        id_customer = self.kwargs.get("id_customer")
        return get_object_or_404(Customer, id_customer=id_customer)

    def form_valid(self, form):
        form.name = form.cleaned_data["name"]
        form.tax_number = form.cleaned_data["tax_number"]
        form.email = form.cleaned_data["email"]
        form.birth_date = form.cleaned_data["birth_date"]
        form.active = form.cleaned_data["active"]

        return super().form_valid(form)


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    permission_required = 'customers.delete_customer'

    def get_object(self):
        id_customer = self.kwargs.get("id_customer")
        return get_object_or_404(Customer, id_customer=id_customer)

    def get_success_url(self):
        return reverse_lazy("administrator:menu_customers")


class AddressCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'address_create.html'
    form_class = AddressForm
    success_url = reverse_lazy("administrator:menu_customers")
    permission_required = 'customers.add_address'

    def form_valid(self, form):
        form.street = form.cleaned_data["street"]
        form.door_number = form.cleaned_data["door_number"]
        form.instance.city = form.cleaned_data["city"]
        form.instance.postal_code = form.cleaned_data["postal_code"]
        form.instance.customer = form.cleaned_data["customer"]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['postal_codes'] = PostalCode.objects.all()
        context['customers'] = Customer.objects.all()
        return context


class AddressListView(PermissionRequiredMixin, ListView):
    template_name = 'address_list.html'
    model = Address
    context_object_name = 'address_list'
    permission_required = 'customers.view_address'


class AddressUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'address_create.html'
    form_class = AddressForm
    success_url = reverse_lazy("customers:address_list")
    permission_required = 'customers.change_address'

    def get_object(self):
        id_address = self.kwargs.get("id_address")
        return get_object_or_404(Address, id_address=id_address)

    def form_valid(self, form):
        form.street = form.cleaned_data["street"]
        form.door_number = form.cleaned_data["door_number"]
        form.instance.city = form.cleaned_data["city"]
        form.instance.postal_code = form.cleaned_data["postal_code"]
        form.instance.customer = form.cleaned_data["customer"]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['postal_codes'] = PostalCode.objects.all()
        context['customers'] = Customer.objects.all()
        return context


class AddressDeleteView(PermissionRequiredMixin, DeleteView):
    model = Address
    template_name = 'address_confirm_delete.html'
    permission_required = 'customers.delete_address'

    def get_object(self, queryset=None):
        id_address = self.kwargs.get("id_address")
        return get_object_or_404(Address, id_address=id_address)

    def get_success_url(self):
        return reverse_lazy("customers:address_list")


class RegistrationView(PermissionRequiredMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    permission_required = 'customers.add_customer'

    def form_valid(self, form):
        address = form.save(commit=False)
        customer = Customer.objects.create(
            name=form.cleaned_data['name'],
            tax_number=form.cleaned_data['tax_number'],
            email=form.cleaned_data['email'],
            birth_date=form.cleaned_data['birth_date'],
            active=form.cleaned_data['active'],
        )
        city = City.objects.create(name_city=form.cleaned_data['name_city'])
        postal_code = PostalCode.objects.create(postal_code=form.cleaned_data['postal_code'])
        address.customer = customer
        address.city = city
        address.postal_code = postal_code
        address.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("administrator:menu_customers")


class RegistrationListView(PermissionRequiredMixin, ListView):
    template_name = 'registration_list.html'
    model = Address
    context_object_name = 'register_list'
    permission_required = 'customers.view_address'


class RegistrationUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy("administrator:menu_customers")
    #i didnt add permisions since im not sure what this function is for - guilherme
    pk_url_kwarg = "id_address"

    def get_object_id_address(self):
        id_address = self.kwargs.get("id_address")
        return get_object_or_404(Address, id_address=id_address)

    def get_object_id_customer(self):
        id_customer = self.kwargs.get("id_customer")
        return get_object_or_404(Customer, id_customer=id_customer)

    def get_object_id_city(self):
        id_city = self.kwargs.get("id_city")
        return get_object_or_404(City, id_city=id_city)

    def get_object_id_postal_code(self):
        id_postal_code = self.kwargs.get("id_postal_code")
        return get_object_or_404(PostalCode, id_postal_code=id_postal_code)

    def get_queryset(self):
        return Address.objects.filter(id_address=self.kwargs['id_address'],
                                      customer=self.kwargs['id_customer'])

    def form_valid(self, form):
        address = form.save(commit=False)
        customer = self.get_object_id_customer()
        customer.name = form.cleaned_data['name']
        customer.tax_number = form.cleaned_data['tax_number']
        customer.email = form.cleaned_data['email']
        customer.birth_date = form.cleaned_data['birth_date']
        customer.active = form.cleaned_data['active']
        customer.save()
        city = self.get_object_id_city()
        city.name_city = form.cleaned_data["name_city"]
        city.save()
        postal_code = self.get_object_id_postal_code()
        postal_code.postal_code = form.cleaned_data["postal_code"]
        postal_code.save()
        address.customer = customer
        address.city = city
        address.postal_code = postal_code
        address.save()
        return super().form_valid(form)


def get_customer(request):
    return get_object_or_404(Customer, user=request.user)


def view_customer_package(request):
    customer = get_customer(request)
    return render(request, 'clientes/customer_package.html', {'package': customer.package})


def view_customer_unique_service(request):
    customer = get_customer(request)
    return render(request, 'clientes/customer_unique_service.html', {'unique_service': customer.unique_service})


# def view_customer_promotions(request):
#     customer = get_customer(request)
#     promotions = Promotion.objects.filter(customer=customer)
#     return render(request, 'clientes/customer_promotions.html', {'promotions': promotions})

def update_customer_data(request):
    customer = get_customer(request)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados com sucesso!')
            return redirect('view_customer_package')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/update_customer_data.html', {'form': form})

# def view_available_packages(request):
#     packages = Package.objects.all()
#     return render(request, 'clientes/available_packages.html', {'packages': packages})

# def view_available_unique_services(request):
#     unique_services = UniqueService.objects.all()
#     return render(request, 'clientes/available_unique_services.html', {'unique_services': unique_services})

# def view_available_promotions(request):
#     promotions = Promotion.objects.all()
#     return render(request, 'clientes/available_promotions.html', {'promotions': promotions})

def register_customer(request):
    if request.method == 'POST':
        form = UserCustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer.user)  # Log the user in after registration
            return redirect('index')  # Redirect to a home page or another relevant page
    else:
        form = UserCustomerRegistrationForm()
    return render(request, 'register.html', {'form': form})
