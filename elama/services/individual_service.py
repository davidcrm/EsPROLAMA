from typing import Optional

from django.utils.html import strip_tags
from elama.forms.volcado_form import VolcadoForm
from elama.models import Autoevaluacion, Descriptor, Volcado


class IndividualService:
    """
    Servicio para operaciones relacionadas con la gestión individual de descriptores
    y volcado de datos en autoevaluaciones.
    """

    def paginacion(self, descriptor: Descriptor):
        """
        Gestiona la paginación entre descriptores según su orden (step).

        Args:
            descriptor (Descriptor): Descriptor actual.

        Returns:
            dict: Diccionario con el primer, último, siguiente y anterior descriptor.
        """
        descriptores = Descriptor.objects.all().order_by("step")

        # Obtener primer y último descriptor
        primer_descriptor = descriptores.first()
        ultimo_descriptor = descriptores.last()

        # Si el primer descriptor está vacío (contenido_html), buscar en sus hijos
        if self.contenido_html_vacio(primer_descriptor):
            primer_descriptor = primer_descriptor.descriptor_set.order_by("step").first()

        # Si el último descriptor está vacío, buscar en sus hijos
        if self.contenido_html_vacio(ultimo_descriptor):
            ultimo_descriptor = ultimo_descriptor.descriptor_set.order_by("step").last()

        # Buscar siguiente descriptor que tenga step mayor al actual
        siguiente_descriptor = descriptores.filter(step__gt=descriptor.step).first()

        if siguiente_descriptor is None:
            siguiente_descriptor = descriptor
        # Si siguiente descriptor está vacío, buscar el siguiente con contenido no nulo
        elif self.contenido_html_vacio(siguiente_descriptor):
            siguiente_descriptor = descriptores.filter(
                step__gt=siguiente_descriptor.step,
                contenido_html__isnull=False
            ).first()

        # Buscar anterior descriptor con step menor
        anterior_descriptor = descriptores.filter(step__lt=descriptor.step).last()

        if anterior_descriptor is None:
            anterior_descriptor = descriptor
        # Si anterior descriptor está vacío, buscar el último con contenido no nulo antes de ese step
        elif self.contenido_html_vacio(anterior_descriptor):
            anterior_descriptor = descriptores.filter(
                step__lt=anterior_descriptor.step,
                contenido_html__isnull=False
            ).last()

        # Devolver los descriptores relevantes para la paginación
        return {
            'primer_descriptor': primer_descriptor,
            'ultimo_descriptor': ultimo_descriptor,
            'siguiente_descriptor': siguiente_descriptor,
            'anterior_descriptor': anterior_descriptor,
        }

    def contenido_html_vacio(self, descriptor: Optional[Descriptor]) -> bool:
        """
        Comprueba si el contenido HTML de un descriptor está vacío.

        Args:
            descriptor (Optional[Descriptor]): Descriptor a evaluar.

        Returns:
            bool: True si está vacío o es None, False si tiene contenido.
        """
        if descriptor is None or not descriptor.contenido_html:
            return True
        return strip_tags(descriptor.contenido_html).strip() == ""

    # Método para crear o actualizar un Volcado a partir de datos del formulario
    def crear_volcado(self, data, autoevaluacion: Autoevaluacion, descriptor: Descriptor):
        """
        Crea o actualiza un objeto Volcado con los datos proporcionados.

        Args:
            data (dict): Datos enviados desde el formulario (POST).
            autoevaluacion (Autoevaluacion): Autoevaluación relacionada.
            descriptor (Descriptor): Descriptor relacionado.
        """
        # Buscar si ya existe un Volcado para esta autoevaluación y descriptor
        volcado = Volcado.objects.filter(
            autoevaluacion_id=autoevaluacion.id,
            descriptor_id=descriptor.id
        ).first()

        if volcado is not None:
            # Actualizar el volcado existente
            form = VolcadoForm(instance=volcado, data=data)
            if form.is_valid():
                form.save()
        else:
            # Crear nuevo volcado
            form = VolcadoForm(data=data)
            if form.is_valid():
                volcado = form.save(commit=False)
                volcado.autoevaluacion = autoevaluacion
                volcado.descriptor = descriptor
                volcado.save()
