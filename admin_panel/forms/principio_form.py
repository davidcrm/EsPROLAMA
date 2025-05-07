from django import forms

from elama.models import Principio, Estrategia


class PrincipioForm(forms.ModelForm):

    estrategia = forms.ModelChoiceField(
        queryset=Estrategia.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Estrategia'
    )
    class Meta:
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
