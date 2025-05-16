import unicodedata
from django import forms
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label= 'Contraseña',
        widget= forms.PasswordInput(attrs={'class': 'form-control'}),
        required= False # Opcional para edición
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el email del usuario'
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si el usuario ya existe (es edición), quitamos el campo contraseña
        if self.instance and self.instance.pk:
            self.fields.pop('password')

    # Sobreescribimos el métod0 save del formulario
    def save(self, commit=True):
        user = super().save(commit=False)

        # Recogemos y limpiamos nombre y apellidos en minúsculas
        nombre = self.cleaned_data.get('first_name', '').strip().lower()
        apellidos = self.cleaned_data.get('last_name', '').strip().lower()

        # Separamos apellidos por espacio
        partes_apellido = apellidos.split()

        primer_apellido = partes_apellido[0] if len(partes_apellido) > 0 else ''
        segundo_apellido = partes_apellido[1] if len(partes_apellido) > 1 else ''

        # Generamos el username
        username = (
            (nombre[0] if nombre else '') +
            (primer_apellido[:3] if primer_apellido else '') +
            (segundo_apellido[:3] if segundo_apellido else '')
        ).lower()

        # Quitamos tildes y caracteres especiales del username
        username = unicodedata.normalize('NFKD', username)  # Descompone los caracteres unicode
        username = username.encode('ascii', 'ignore').decode('utf-8')  # Quita lo no ascii

        # Asignamos el username al usuario
        user.username = username

        # Lo guardamos
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk:  # Si es un usuario nuevo carga el campo contraseña
            password = cleaned_data.get('password')
            if not password:
                self.add_error('password', 'La contraseña es obligatoria al crear un usuario.')