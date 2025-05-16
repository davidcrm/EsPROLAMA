from django import forms

from elama.models import Volcado


class VolcadoForm(forms.ModelForm):
    """
    Formulario para el modelo Volcado.

    Campos incluidos:
        - valoracion: campo de valoración con opciones de 1 a 4 (RadioSelect).
        - logro: campo de texto para apuntar un logro.
        - mejora: campo de texto para apuntar una mejora.

    Personalización:
        - Las etiquetas para los campos son personalizadas.
        - Los campos 'logro' y 'mejora' usan Textarea con atributos de estilo específicos.
    """
    class Meta:
        model = Volcado
        fields = ['valoracion', 'logro', 'mejora']
        labels = {'valoracion': '', 'logro': 'Logro', 'mejora': 'Mejora'}

        OPCIONES = (
            ('1', 'Uno'),
            ('2', 'Dos'),
            ('3', 'Tres'),
            ('4', 'Cuatro')
        )

        widgets = {
            'valoracion': forms.RadioSelect(choices=OPCIONES),
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
