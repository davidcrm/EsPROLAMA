import unicodedata
from django import forms
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
    """
    Formulario para crear y editar objetos del modelo User de Django.

    Este formulario permite gestionar usuarios, incluyendo nombre, apellidos, correo y contraseña.
    Además, genera automáticamente el campo `username` a partir de nombre y apellidos
    y gestiona la creación o edición de la contraseña.

    Attributes:
        password (CharField): Campo personalizado para la contraseña, visible solo al crear usuario.
    """

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False  # Opcional para edición
    )

    class Meta:
        """
        Metadatos para configurar el formulario UsuarioForm.

        Attributes:
            model (Model): Modelo al que está asociado el formulario.
            fields (list): Lista de campos del modelo que se incluyen en el formulario.
            labels (dict): Etiquetas personalizadas para los campos del formulario.
            widgets (dict): Widgets personalizados para los campos del formulario.
        """
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el email del usuario'
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Inicializa el formulario. Si se está editando un usuario existente,
        elimina el campo de contraseña para no mostrarlo.
        """
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields.pop('password')

    def save(self, commit=True):
        """
        Sobreescribe el método save para personalizar la creación/edición de un usuario.

        - Genera automáticamente el username combinando la inicial del nombre
          y las tres primeras letras de cada apellido.
        - Elimina acentos y caracteres especiales del username.
        - Asigna la contraseña si se ha proporcionado.
        - Guarda el usuario en base de datos si `commit` es True.

        Args:
            commit (bool): Si es True, guarda el usuario en base de datos.

        Returns:
            User: El objeto usuario creado o modificado.
        """
        user = super().save(commit=False)

        nombre = self.cleaned_data.get('first_name', '').strip().lower()
        apellidos = self.cleaned_data.get('last_name', '').strip().lower()
        partes_apellido = apellidos.split()

        primer_apellido = partes_apellido[0] if len(partes_apellido) > 0 else ''
        segundo_apellido = partes_apellido[1] if len(partes_apellido) > 1 else ''

        username = (
            (nombre[0] if nombre else '') +
            (primer_apellido[:3] if primer_apellido else '') +
            (segundo_apellido[:3] if segundo_apellido else '')
        ).lower()

        username = unicodedata.normalize('NFKD', username)
        username = username.encode('ascii', 'ignore').decode('utf-8')

        user.username = username

        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        """
        Valida los datos del formulario.

        Si se está creando un usuario nuevo (sin `instance.pk`), obliga a que se
        proporcione una contraseña. Si no, añade un error al campo `password`.
        """
        cleaned_data = super().clean()
        if not self.instance.pk:
            password = cleaned_data.get('password')
            if not password:
                self.add_error('password', 'La contraseña es obligatoria al crear un usuario.')
