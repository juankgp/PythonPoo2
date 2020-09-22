from django import forms
from .models import Piezas, Proveedor, Suministra

class PiezasForm(forms.ModelForm):
    def __init__ (self,*args,**kwargs):
        super(PiezasForm, self).__init__(*args,**kwargs)
        self.fields['Nombre'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['Descripcion'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['Tipo'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        
    class Meta:
        model = Piezas
        fields=('Nombre','Descripcion','Tipo')

class ProveedorForm(forms.ModelForm):
    def __init__ (self,*args,**kwargs):
        super(ProveedorForm, self).__init__(*args,**kwargs)
        self.fields['Nombre'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['Direccion'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['Credito'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        
    class Meta:
        model = Proveedor
        fields=('Nombre','Direccion','Credito')

class SuministraForm(forms.ModelForm):
    def __init__ (self,*args,**kwargs):
        super(SuministraForm, self).__init__(*args,**kwargs)
        self.fields['Precio'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['Pieza_cod'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        self.fields['Proveedor_cod'].widget.attrs={
            'class': 'form-control col-md-6'
        }
        
    class Meta:
        model = Suministra
        fields=('Precio','Pieza_cod','Proveedor_cod')