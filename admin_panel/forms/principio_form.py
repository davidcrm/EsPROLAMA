from django import forms

from elama.models import Principio, Estrategia


class PrincipioForm(forms.ModelForm):
    """
    Formulario para crear y editar objetos del modelo Principio.

    Este formulario permite definir un Principio, asignarle una Estrategia asociada
    y establecer su título mediante un campo de texto personalizado.

    Attributes:
        estrategia (ModelChoiceField): Campo para seleccionar la Estrategia a la que pertenece el Principio.
    """

    estrategia = forms.ModelChoiceField(
        queryset=Estrategia.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Estrategia'
    )

    class Meta:
        """
        Metadatos para configurar el formulario PrincipioForm.

        Attributes:
            model (Model): Modelo al que está asociado el formulario.
            fields (list): Lista de campos del modelo que se incluyen en el formulario.
            labels (dict): Etiquetas personalizadas para los campos del formulario.
            widgets (dict): Widgets personalizados para los campos del formulario.
        """
        model = Principio
        fields = ['titulo', 'estrategia']
        labels = {
            'titulo': 'Título',
            'principio': 'Principio'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el título del principio',
            })
        }
