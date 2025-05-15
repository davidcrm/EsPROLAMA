from ckeditor.widgets import CKEditorWidget
from django import forms

from elama.models import Principio, Descriptor

class DescriptorForm(forms.ModelForm):

    principio = forms.ModelChoiceField(
        queryset=Principio.objects.all().order_by('step'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Principio'
    )

    descriptor_padre = forms.ModelChoiceField(
        queryset=Descriptor.objects.all().order_by('step'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Descriptor Padre',
        required = False
    )

    step = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False,
        initial=None
    )

    class Meta:
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
