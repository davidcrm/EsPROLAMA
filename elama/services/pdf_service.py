from io import BytesIO
from xhtml2pdf import pisa
from elama.models import Autoevaluacion, Estrategia


class PdfService:
    @staticmethod
    def export_autoevaluacion(autoevaluacion: Autoevaluacion):
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

        for estrategia in estrategias:
            html_string += f"""
                <h2>{estrategia.titulo}</h2>
                <ul>
            """
            for principio in estrategia.principio_set.all():
                html_string += f"""
                    <li><h3>{principio.titulo}</h3></li>
                    <ul>
                """
                for descriptor in principio.descriptor_set.all():
                    titulo = descriptor.titulo.rstrip()
                    if titulo.endswith('.'):
                        puntos = titulo[:-1].count('.')
                    else:
                        puntos = titulo.count('.')
                    padding_left = 8 if puntos > 2 else 0

                    volcado = descriptor.volcado_set.filter(autoevaluacion_id=autoevaluacion.id).first()
                    html_string += f"""
                        <li style="padding-left: {padding_left * puntos}px;">
                            {descriptor.titulo}  {f" &#10132; <strong>{volcado.valoracion}</strong>" if volcado else ''}
                        </li>
                    """
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
