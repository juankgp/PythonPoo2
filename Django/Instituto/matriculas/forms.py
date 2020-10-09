from django import forms
from .models import Matriculas

class MatriculasForm(forms.ModelForm):

    def __init__(self, *args , **Kwargs):
        super(MatriculasForm, self).__init__(*args , **Kwargs)

        self.fields['Estudiante'].widget.attrs={ 
            'class': 'form-control col-md-6'}

        self.fields['Carrera'].widget.attrs={ 
            'class': 'form-control col-md-6'}

        self.fields['Semestre'].widget.attrs={ 
            'class': 'form-control col-md-6'}

        self.fields['Fecha'].widget.attrs={ 
            'class': 'form-control col-md-6'}
        
        self.fields['Costo'].widget.attrs={ 
            'class': 'form-control col-md-6'}
        
        self.fields['Paralelo'].widget.attrs={ 
            'class': 'form-control col-md-6'}

        self.fields['NotaSemAnt'].widget.attrs={ 
            'class': 'form-control col-md-6'}
    class Meta:
        model= Matriculas
        fields=('Estudiante', 'Carrera', 'Semestre', 'Fecha','Costo','Paralelo','NotaSemAnt')