from datetime import datetime
from io import BytesIO

from django.contrib.auth.models import User
from xhtml2pdf import pisa
from typing import Optional, List

from elama.models import Autoevaluacion, Estrategia, Volcado, Grupo


class PdfService:
    @staticmethod
    def export_autoevaluacion_individual(autoevaluacion: Autoevaluacion, user: User, volcados: Optional[List[Volcado]] = None):
        estrategias = Estrategia.objects.all()

        html_string = """
        <html>
        <head>
            <style> 
                ul, 
                ul ul, 
                ul ul ul, 
                ul ul ul ul {
                    list-style-type: none; 
                } 
            </style>
        </head>
        <body>
        """

        html_string += f"""
        <div>
            <p>Evaluador: <strong>{user.username}</strong></p>
            <p>{datetime.now().strftime('%d/%m/%Y')}</p>
        </div>
        """

        for estrategia in estrategias.order_by('step'):
            html_string += f"""
                <h2>{estrategia.titulo}</h2>
                <ul>
            """
            for principio in estrategia.principio_set.all().order_by('step'):
                html_string += f"""
                    <li><h3>{principio.titulo}</h3></li>
                    <ul>
                """
                for descriptor in principio.descriptor_set.all().order_by('step'):
                    titulo = descriptor.titulo.rstrip()
                    if titulo.endswith('.'):
                        puntos = titulo[:-1].count('.')
                    else:
                        puntos = titulo.count('.')
                    padding_left = 8 if puntos > 2 else 0

                    volcado = None

                    if volcados is None:
                        volcado = descriptor.volcado_set.filter(autoevaluacion_id=autoevaluacion.id).first()
                    elif type(volcados) == list :
                        volcado = list(filter(
                            lambda v: v.autoevaluacion_id == autoevaluacion.id and v.descriptor_id == descriptor.id,
                            volcados
                        ))

                        volcado = volcado[0] if len(volcado) > 0 else None

                    html_string += f"""
                        <li style="padding-left: {padding_left * puntos}px;">
                            {descriptor.titulo}  {f" &#10132; <strong>{volcado.valoracion}</strong>" if volcado else ''}
                                """


#                   if volcado:
#                        """
#                        SI QUEREMOS MOSTRAR LAS ANOTACIONES EN EL PDF
#                        """
#                        if volcado.logro:
#                            html_string += f"""
#                            <h4>Logro</h4>
#                            <p>{volcado.logro}</p>
#                            """
#                        if volcado.mejora:
#                            html_string += f"""
#                            <h4>Mejora</h4>
#                            <p>{volcado.mejora}</p>
#                            """

                html_string += "</ul>"
            html_string += "</ul>"

        html_string += """    
        </body>
        </html>
        """

        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        pdf_file.seek(0)
        return pdf_file if not pisa_status.err else None

    @staticmethod
    def export_autoevaluacion_grupal(autoevaluacion: Autoevaluacion, grupo: Grupo):
        pass