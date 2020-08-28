from django import forms
from .models import Empleados

class EmpleadosForm(forms.ModelForm):
    def __init__ (self,*args,**kwargs):
        super(EmpleadosForm, self).__init__(*args,**kwargs)
        self.fields['Apellido'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['Nombres'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['Cedula'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['FechaNacimiento'].widget.attrs={
            'class': 'form-control col-md-6'
        }
    class Meta:
        model = Empleados
        fields=('Apellido','Nombres','Cedula','FechaNacimiento')