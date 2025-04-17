from typing import Optional

from django.db.models import QuerySet
from elama.models import Autoevaluacion, Descriptor, Volcado
from elama.forms import VolcadoForm


class IndividualService:
    def paginacion(self, descriptor: Descriptor):
        descriptores = Descriptor.objects.all().order_by("id")

        primer_descriptor = descriptores.first()
        ultimo_descriptor = descriptores.last()

        if self.contenido_html_vacio(primer_descriptor):
            primer_descriptor = self.buscar_descriptores_hijos(primer_descriptor.descriptor_set.all()).first()

        if self.contenido_html_vacio(ultimo_descriptor):
            ultimo_descriptor = self.buscar_descriptores_hijos(ultimo_descriptor.descriptor_set.all()).last()

        siguiente_descriptor = descriptores.filter(id__gt=descriptor.id).first()

        if siguiente_descriptor is None:
            siguiente_descriptor = descriptor
        elif self.contenido_html_vacio(siguiente_descriptor):
            siguiente_descriptor = self.buscar_descriptores_hijos(siguiente_descriptor.descriptor_set.all()).first()

        anterior_descriptor = descriptores.filter(id__lt=descriptor.id).last()

        if anterior_descriptor is None:
            anterior_descriptor = descriptor
        elif self.contenido_html_vacio(anterior_descriptor):
            anterior_descriptor = descriptores.filter(
                id__lt=anterior_descriptor.id,
                contenido_html__isnull=False
            ).last()

        return {
            'primer_descriptor': primer_descriptor,
            'ultimo_descriptor': ultimo_descriptor,
            'siguiente_descriptor': siguiente_descriptor,
            'anterior_descriptor': anterior_descriptor,
        }

    def contenido_html_vacio(self, descriptor: Optional[Descriptor]):
        if descriptor is None:
            return True
        return descriptor.contenido_html is None or len(descriptor.contenido_html.strip()) == 0

    def buscar_descriptores_hijos(self, descriptores: Optional[QuerySet]):
        if descriptores is None or descriptores.count() == 0:
            return descriptores
        for descriptor in descriptores.all():
            if descriptor.descriptor_set.count() > 0:
                return self.buscar_descriptores_hijos(descriptor.descriptor_set.all())
        return descriptores

    # data = request.POST
    def crear_volcado(self, data, autoevaluacion: Autoevaluacion, descriptor: Descriptor):
        volcado = Volcado.objects.filter(autoevaluacion_id=autoevaluacion.id, descriptor_id=descriptor.id).first()

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
