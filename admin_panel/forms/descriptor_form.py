from ckeditor.widgets import CKEditorWidget
from django import forms

from elama.models import Principio, Descriptor

class DescriptorForm(forms.ModelForm):

    principio = forms.ModelChoiceField(
        queryset=Principio.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Principio'
    )

    class Meta:
        model = Descriptor
        fields = ['titulo', 'principio', 'contenido_html']
        labels = {
            'titulo': 'Título',
            'principio': 'Principio',
            'contenido_html': 'Contenido'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el título del descriptor',
            }),
            'contenido_html': CKEditorWidget(config_name='default')
        }
