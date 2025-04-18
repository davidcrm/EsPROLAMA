from django import forms
from elama.models.descriptor_anotacion import DescriptorAnotacion

class AnotacionForm(forms.ModelForm):
    class Meta:
        model = DescriptorAnotacion
        fields = ['logro', 'mejora']
        labels = {
            'logro': 'Logro',
            'mejora': 'Mejora',
        }
        widgets = {
            'logro': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Apunta un logro para el programa de ELAMA en tu entidad.',
                'style': 'resize: none;'
            }),
            'mejora': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Apunta una posible mejora para el programa de ELAMA en tu entidad.',
                'style': 'resize: none;'
            }),
        }
