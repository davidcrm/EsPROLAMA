from io import BytesIO
from weasyprint import HTML
from elama.models import Autoevaluacion


class PdfService:
    @staticmethod
    def export_autoevaluacion(autoevaluacion: Autoevaluacion):
        html_string = """
        <html>
        <head><style>h1 { color: red; }</style></head>
        <body>
            <h1>Hola mundo</h1>
            <p>Este es un <b>PDF</b> generado desde HTML.</p>
        </body>
        </html>
        """

        pdf_file = BytesIO()
        HTML(string=html_string).write_pdf(pdf_file)
        pdf_file.seek(0)
        return pdf_file
