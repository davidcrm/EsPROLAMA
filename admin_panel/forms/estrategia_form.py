from django import forms

from elama.models import Estrategia


class EstrategiaForm(forms.ModelForm):
    """
    Formulario para crear y editar objetos del modelo Estrategia.

    Este formulario permite definir el título de una Estrategia mediante un campo de texto personalizado.
    """

    class Meta:
        """
        Metadatos para configurar el formulario EstrategiaForm.

        Attributes:
            model (Model): Modelo al que está asociado el formulario.
            fields (list): Lista de campos del modelo que se incluyen en el formulario.
            labels (dict): Etiquetas personalizadas para los campos del formulario.
            widgets (dict): Widgets personalizados para los campos del formulario.
        """
        model = Estrategia
        fields = ['titulo']
        labels = {'titulo': 'Título'}
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el título de la estrategia',
            })
        }
