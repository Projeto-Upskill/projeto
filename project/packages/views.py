from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from .models import Package
#from .forms import PackageForm
from django.shortcuts import get_object_or_404

#class PackageListView(ListView):
    #model = Package
    #template_name = 'packages/package_list.html'
    #context_object_name = 'package'

#class PackageCreateView(CreateView):
    #model = Package
    #form_class = PackageForm
    #template_name = 'packages/package_form.html'
    #success_url = reverse_lazy('packages:package_list')

#class PackageUpdateView(UpdateView):
    #model = Package
    #form_class = PackageForm
    #template_name = 'packages/package_form.html'
    #success_url = reverse_lazy('packages:package_list')

    #def get_object(self):
        #id_package = self.kwargs.get('id_package')
        #return get_object_or_404(Package, id_package=id_package)

#class PackageDeleteView(DeleteView):
    #model = Package
    #template_name = 'packages/package_confirm_delete.html'
    #success_url = reverse_lazy('packages:package_list')

    #def get_object(self):
        #id_package = self.kwargs.get('id_package')
        #return get_object_or_404(Package, id_package=id_package)

