from ckeditor.widgets import CKEditorWidget
from django import forms

from elama.models import Principio, Descriptor


class DescriptorForm(forms.ModelForm):
    """
    Formulario para crear y editar objetos del modelo Descriptor.

    Este formulario permite seleccionar un Principio asociado, un Descriptor padre opcional,
    establecer un orden mediante 'step', y editar contenido en formato HTML usando CKEditor.

    Attributes:
        principio (ModelChoiceField): Campo para seleccionar el Principio al que pertenece el Descriptor.
        descriptor_padre (ModelChoiceField): Campo opcional para seleccionar un Descriptor padre.
        step (IntegerField): Campo oculto para indicar el orden o paso del Descriptor.
    """

    principio = forms.ModelChoiceField(
        queryset=Principio.objects.all().order_by('step'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Principio'
    )

    descriptor_padre = forms.ModelChoiceField(
        queryset=Descriptor.objects.all().order_by('step'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Descriptor Padre',
        required=False
    )

    step = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False,
        initial=None
    )

    class Meta:
        """
        Metadatos para configurar el formulario DescriptorForm.

        Attributes:
            model (Model): Modelo al que está asociado el formulario.
            fields (list): Lista de campos del modelo que se incluyen en el formulario.
            labels (dict): Etiquetas personalizadas para los campos del formulario.
            widgets (dict): Widgets personalizados para los campos del formulario.
        """
        model = Descriptor
        fields = ['titulo', 'principio', 'descriptor_padre', 'contenido_html', 'step']
        labels = {
            'titulo': 'Título',
            'principio': 'Principio',
            'descriptor_padre': 'Descriptor Padre',
            'contenido_html': 'Contenido'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el título del descriptor',
            }),
            'contenido_html': CKEditorWidget(config_name='default')
        }
