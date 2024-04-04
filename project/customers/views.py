from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Address, PostalCode, City
from .forms import CustomerForm
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy


class CustomerCreateView(CreateView):
    template_name = 'customer_create.html'
    form_class = CustomerForm
    success_url = reverse_lazy('administrator:menu_customers')

    def form_valid(self, form):
        form.name = form.cleaned_data["name"]
        form.tax_number = form.cleaned_data["tax_number"]
        form.email = form.cleaned_data["email"]
        form.birth_date = form.cleaned_data["birth_date"]
        form.active = form.cleaned_data["active"]

        return super().form_valid(form)


class CustomerListView(ListView):
    template_name = 'customer_list.html'
    model = Customer
    context_object_name = 'customer_list'


class CustomerUpdateView(UpdateView):
    template_name = 'customer_create.html'
    form_class = CustomerForm
    success_url = reverse_lazy("administrator:menu_customers")

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
