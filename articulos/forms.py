from django import forms
from .models import Articulo
from ckeditor.fields import RichTextFormField

class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['nombre','tipo','precio','cantidad','descripcion']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}),
            'precio' : forms.NumberInput(attrs={'class':'form-control','placeholder':'precio'}),
            'cantidad' : forms.NumberInput(attrs={'class':'form-control','placeholder':'cantidad'}),
            'descripcion' :RichTextFormField(),
            
        }
        labels = {
            'nombre': '',
            'tipo': '',
            'precio':'',
            'cantidad':'',
            'descripcion':'',
        }


        