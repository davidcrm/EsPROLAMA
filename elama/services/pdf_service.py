from datetime import datetime
from io import BytesIO

from django.contrib.auth.base_user import AbstractBaseUser
from xhtml2pdf import pisa
from typing import Optional, List
from elama.models import Autoevaluacion, Estrategia, Volcado


class PdfService:
    @staticmethod
    def export_autoevaluacion_individual(autoevaluacion: Autoevaluacion, user: AbstractBaseUser, volcados: Optional[List[Volcado]] = None):
        """
        Genera un PDF con la autoevaluación individual o grupal de un usuario.

        Args:
            autoevaluacion (Autoevaluacion): Autoevaluación a exportar.
            user (AbstractBaseUser): Usuario evaluador.
            volcados (Optional[List[Volcado]]): Lista opcional de volcados para optimizar consultas.

        Returns:
            BytesIO | None: Archivo PDF generado en memoria, o None si falla la generación.
        """

        # Obtener todas las estrategias ordenadas por el campo 'step'
        estrategias = Estrategia.objects.all().order_by("step")

        # Inicio del contenido HTML para el PDF
        html_string = """
        <html>
        <head>
            <style> 
                ul, ul ul {
                    list-style-type: none; 
                }
                .header {
                    text-align: center;
                    margin-bottom: 20px;
                }
                .header h2 {
                    font-size: 24px;
                }
                .header p {
                    font-size: 16px;
                    margin: 5px 0;
                }
            </style>
        </head>
        <body>
        """

        # Cabecera con información del tipo de autoevaluación
        html_string += f"""
        <div class="header">
        """
        if autoevaluacion.grupo:
            html_string += f"""
                <h2>AUTOEVALUACION GRUPAL</h2>
                <p>Grupo: <strong>{autoevaluacion.grupo.nombre}</strong></p>
            """
        else:
            html_string += f"""
                <h2>AUTOEVALUACION INDIVIDUAL</h2>
                <p>Evaluador: <strong>{user.username}</strong></p>
            """

        # Fecha actual formateada
        html_string += f"""
            <p>{datetime.now().strftime('%d/%m/%Y')}</p>
        </div>
        """

        # Recorrer todas las estrategias para mostrar principios y descriptores
        for estrategia in estrategias.order_by('step'):
            html_string += f"""
                <h2>{estrategia.titulo}</h2>
                <ul>
            """
            for principio in estrategia.principio_set.all().order_by("step"):
                html_string += f"""
                    <li><h3>{principio.titulo}</h3></li>
                    <ul>
                """
                for descriptor in principio.descriptor_set.all().order_by("step"):
                    titulo = descriptor.titulo.rstrip()
                    # Contar puntos para el estilo de indentación
                    if titulo.endswith('.'):
                        puntos = titulo[:-1].count('.')
                    else:
                        puntos = titulo.count('.')

                    padding_left = 8 if puntos > 2 else 0
                    volcado = None

                    # Buscar volcado según si se pasan volcados por parámetro o no
                    if volcados is None:
                        volcado = descriptor.volcado_set.filter(autoevaluacion_id=autoevaluacion.id).first()
                    elif type(volcados) == list:
                        volcado = list(filter(
                            lambda v: v.autoevaluacion_id == autoevaluacion.id and v.descriptor_id == descriptor.id,
                            volcados
                        ))

                        volcado = volcado[0] if len(volcado) > 0 else None

                    # Añadir el descriptor con valoración si existe
                    html_string += f"""
                        <li style="padding-left: {padding_left * puntos}px;">
                            {descriptor.titulo}  {f" &#10132; <strong>{volcado.valoracion}</strong>" if volcado else ''}
                             """

                    """
                    SI QUEREMOS MOSTRAR LAS ANOTACIONES EN EL PDF
                    """
                    if volcado:
                        if volcado.logro:
                            html_string += f"""
                            <h4>Logro</h4>
                            <p>{volcado.logro}</p>
                            """

                        if volcado.mejora:
                            html_string += f"""
                            <h4>Mejora</h4>
                            <p>{volcado.mejora}</p>
                            """

                html_string += "</ul>"
            html_string += "</ul>"

        # Cierre del HTML
        html_string += """    
        </body>
        </html>
        """

        # Crear PDF en memoria a partir del HTML
        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        pdf_file.seek(0)

        # Devolver el PDF generado o None si hubo error
        return pdf_file if not pisa_status.err else None
