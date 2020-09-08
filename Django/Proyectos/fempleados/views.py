#Incorpora codigo html en py
from django.shortcuts import render
#Hace llamado a las listas genericas urls
from django.urls import reverse_lazy

#Genericas de CRD

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin

#Clases
from .forms import EmpleadosForm
from .models import Empleados
#template 
from django.views.generic import TemplateView

class EmpleadosList(ListView):
    model = Empleados

class EmpleadosDetail(DetailView):
    model = Empleados

class EmpleadosCreate(SuccessMessageMixin,CreateView):
    model = Empleados
    form_class = EmpleadosForm
    success_url = reverse_lazy('empleados_list')
    succes_message = "Empleado creado con Exito"

class EmpleadosUpdate(SuccessMessageMixin,UpdateView):
    model = Empleados
    form_class = EmpleadosForm
    success_url = reverse_lazy('empleados_list')
    succes_message = "Empleado actualizado con Exito"

class EmpleadosDelete(SuccessMessageMixin,DeleteView):
    model = Empleados
    success_url = reverse_lazy('empleados_list')
    succes_message = "Empleado borrado con Exito"    

#Guardar y Editar
def empleados_new(request):
    form = EmpleadosForm()
    return render (request, 'empleados/empleados_list.html',{'form':form})

class BlogDetailsPageView(TemplateView):
    template_name='blog/base.html'

class UserDetailsPageView(TemplateView):
    template_name='users/login.html'

