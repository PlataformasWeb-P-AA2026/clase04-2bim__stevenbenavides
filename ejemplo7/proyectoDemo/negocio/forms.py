from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from negocio.models import Restaurante, Chef, Plato, Comentario

class RestauranteForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'tipo_cocina', 'capacidad_meses']

class ChefForm(ModelForm):
    class Meta:
        model = Chef
        fields = ['nombres', 'anios_experiencia', 'especialidad_culinaria',
                  'restaurante']

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre_plato', 'descripcion', 'precio_plato',
                  'ingredientes_principales', 'chef']

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows':4,
                                                'class':'form-control'
                                                })
                    }
