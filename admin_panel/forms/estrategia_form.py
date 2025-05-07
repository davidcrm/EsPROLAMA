from django import forms

from elama.models import Estrategia


class EstrategiaForm(forms.ModelForm):
    class Meta:
        model = Estrategia
        fields = ['titulo']
        labels = {'titulo': 'Título'}

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el título de la estrategia',
            })
        }