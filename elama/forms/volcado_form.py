from django import forms

from elama.models import Volcado


class VolcadoForm(forms.ModelForm):
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