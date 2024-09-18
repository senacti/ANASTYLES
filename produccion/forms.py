from django import forms
from .models import Produccion

class ProduccionForms(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['nombre', 'categoria', 'color', 'talla', 'cantidad', 'fecha_produccion', 'fecha_finalizacion', 'estado']