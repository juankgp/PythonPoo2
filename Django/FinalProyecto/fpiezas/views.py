#Incorpora codigo html en py
from django.shortcuts import render
#Hace llamado a las listas genericas urls
from django.urls import reverse_lazy

#Genericas de CRD

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin

#Clases
from .forms import PiezasForm, ProveedorForm, SuministraForm
from .models import Piezas,Proveedor,Suministra
#template 
from django.views.generic import TemplateView

#### CRUD Piezas
class PiezasList(ListView):
    model = Piezas

class PiezasDetail(DetailView):
    model = Piezas

class PiezasCreate(SuccessMessageMixin,CreateView):
    model = Piezas
    form_class = PiezasForm
    success_url = reverse_lazy('piezas_list')
    succes_message = "Pieza creado con Exito"

class PiezasUpdate(SuccessMessageMixin,UpdateView):
    model = Piezas
    form_class = PiezasForm
    success_url = reverse_lazy('piezas_list')
    succes_message = "Pieza actualizado con Exito"

class PiezasDelete(SuccessMessageMixin,DeleteView):
    model = Piezas
    success_url = reverse_lazy('piezas_list')
    succes_message = "Pieza borrado con Exito"    

#Guardar y Editar
def piezas_new(request):
    form = PiezasForm()
    return render (request, 'piezas/piezas_list.html',{'form':form})


#### CRUD PROVEEDORES
class ProveedorList(ListView):
    model = Proveedor

class ProveedorDetail(DetailView):
    model = Proveedor

class ProveedorCreate(SuccessMessageMixin,CreateView):
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')
    succes_message = "Proveedor creado con Exito"

class ProveedorUpdate(SuccessMessageMixin,UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')
    succes_message = "Proveedor actualizado con Exito"

class ProveedorDelete(SuccessMessageMixin,DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedor_list')
    succes_message = "Proveedor borrado con Exito"    

#Guardar y Editar
def proveedor_new(request):
    form = ProveedorForm()
    return render (request, 'piezas/proveedor_list.html',{'form':form})


#### CRUD stock
class SuministraList(ListView):
    model = Suministra

class SuministraDetail(DetailView):
    model = Suministra

class SuministraCreate(SuccessMessageMixin,CreateView):
    model = Suministra
    form_class = SuministraForm
    success_url = reverse_lazy('suministra_list')
    succes_message = "Proveedor creado con Exito"

class SuministraUpdate(SuccessMessageMixin,UpdateView):
    model = Suministra
    form_class = SuministraForm
    success_url = reverse_lazy('suministra_list')
    succes_message = "Proveedor actualizado con Exito"

class SuministraDelete(SuccessMessageMixin,DeleteView):
    model = Suministra
    success_url = reverse_lazy('suministra_list')
    succes_message = "Proveedor borrado con Exito"    

#Guardar y Editar
def suministra_new(request):
    form = SuministraForm()
    return render (request, 'piezas/suministra_list.html',{'form':form})





class BlogDetailsPageView(TemplateView):
    template_name='blog/base.html'

class UserDetailsPageView(TemplateView):
    template_name='users/login.html'    

