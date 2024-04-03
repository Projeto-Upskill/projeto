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
    
    #def form_valid(self, form):
        #form.instance.name = form.cleaned_data["name"]
        #form.instance.active = form.cleaned_data["active"]

        #return super().form_valid(form)

#class PackageUpdateView(UpdateView):
    #model = Package
    #form_class = PackageForm
    #template_name = 'packages/package_form.html'
    #success_url = reverse_lazy('packages:package_list')

    #def get_object(self):
        #id_package = self.kwargs.get('id_package')
        #return get_object_or_404(Package, id_package=id_package)
        
    #def form_valid(self, form):
        #form.instance.name = form.cleaned_data["name"]
        #form.instance.active = form.cleaned_data["active"]

        #return super().form_valid(form)

#class PackageDeleteView(DeleteView):
    #model = Package
    #template_name = 'packages/package_confirm_delete.html'
    #success_url = reverse_lazy('packages:package_list')

    #def get_object(self):
        #id_package = self.kwargs.get('id_package')
        #return get_object_or_404(Package, id_package=id_package)
        
    #def get_success_url(self):
        #return reverse_lazy('packages:package_list')
        
#class PackageIndex(TemplateView):
    #template_name = 'index_package.html'

