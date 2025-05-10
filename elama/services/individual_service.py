from typing import Optional

from django.utils.html import strip_tags
from elama.forms.volcado_form import VolcadoForm
from elama.models import Autoevaluacion, Descriptor, Volcado


class IndividualService:
    def paginacion(self, descriptor: Descriptor):
        descriptores = Descriptor.objects.all().order_by("step")

        primer_descriptor = descriptores.first()
        ultimo_descriptor = descriptores.last()

        if self.contenido_html_vacio(primer_descriptor):
            primer_descriptor = primer_descriptor.descriptor_set.order_by("step").first()

        if self.contenido_html_vacio(ultimo_descriptor):
            ultimo_descriptor = ultimo_descriptor.descriptor_set.order_by("step").last()

        siguiente_descriptor = descriptores.filter(step__gt=descriptor.step).first()

        if siguiente_descriptor is None:
            siguiente_descriptor = descriptor
        elif self.contenido_html_vacio(siguiente_descriptor):
            siguiente_descriptor = descriptores.filter(
                step__gt=siguiente_descriptor.step,
                contenido_html__isnull=False
            ).first()

        anterior_descriptor = descriptores.filter(step__lt=descriptor.step).last()

        if anterior_descriptor is None:
            anterior_descriptor = descriptor
        elif self.contenido_html_vacio(anterior_descriptor):
            anterior_descriptor = descriptores.filter(
                step__lt=anterior_descriptor.step,
                contenido_html__isnull=False
            ).last()

        return {
            'primer_descriptor': primer_descriptor,
            'ultimo_descriptor': ultimo_descriptor,
            'siguiente_descriptor': siguiente_descriptor,
            'anterior_descriptor': anterior_descriptor,
        }

    def contenido_html_vacio(self, descriptor: Optional[Descriptor]) -> bool:
        if descriptor is None or not descriptor.contenido_html:
            return True
        return strip_tags(descriptor.contenido_html).strip() == ""

    # data = request.POST
    def crear_volcado(self, data, autoevaluacion: Autoevaluacion, descriptor: Descriptor):
        volcado = Volcado.objects.filter(
            autoevaluacion_id=autoevaluacion.id,
            descriptor_id=descriptor.id
        ).first()

        if volcado is not None:
            form = VolcadoForm(instance=volcado, data=data)
            if form.is_valid():
                form.save()
        else:
            form = VolcadoForm(data=data)
            if form.is_valid():
                volcado = form.save(commit=False)
                volcado.autoevaluacion = autoevaluacion
                volcado.descriptor = descriptor
                volcado.save()

