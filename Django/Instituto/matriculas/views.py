# Incorpora y llamada codigo html
from django.urls import reverse_lazy
from django.shortcuts import render

# Genericas Crud

from django.views.generic import ListView , DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Clases de Modulo
from .forms import MatriculasForm
from .models import Matriculas
from django.views.generic import TemplateView
class MatriculasList(ListView):
    model=Matriculas

class MatriculasDetail(DetailView):
    model=Matriculas

class MatriculasCreate(SuccessMessageMixin, CreateView):
    model=Matriculas
    form_class=MatriculasForm
    success_url= reverse_lazy('matriculas_list')
    success_message="Matricula creada con éxito"

class MatriculasUpdate(SuccessMessageMixin, UpdateView):
    model=Matriculas
    form_class=MatriculasForm
    success_url= reverse_lazy('matriculas_list')
    success_message="Matricula actualizada con éxito"

class MatriculasDelete(SuccessMessageMixin, DeleteView):
    model=Matriculas
    success_url= reverse_lazy('matriculas_list')
    success_message="Matricula eliminada con éxito"

def matriculas_new(request):
    form = MatriculasForm()
    return render (request, 'matriculas/matriculas_list.html',{'form':form})

