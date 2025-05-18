import json

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_POST

from elama.models import Estrategia, Principio, Descriptor


@staff_member_required
@require_POST  # asegura que solo aceptemos peticiones POST.
def actualizar_orden(request: HttpRequest):
    """
    Vista que actualiza el orden (campo `step`) de objetos Estrategia, Principio o Descriptor
    según un array de IDs recibido vía POST en formato JSON.

    Solo permite peticiones POST y usuarios staff autenticados.

    El JSON recibido debe tener una clave correspondiente a uno de los modelos
    ('estrategias', 'principios' o 'descriptores') y un array de IDs en el orden deseado.
    Primero pone todos los `step` a null y luego reasigna valores secuenciales.

    Args:
        request (HttpRequest): Objeto HttpRequest que contiene el cuerpo JSON
        con las claves y el nuevo orden de los IDs.

    Returns:
        JsonResponse: Respuesta con estado 'ok' si se procesó correctamente,
        o 'invalid method' con código 405 si no se recibió una clave válida.
    """
    # Parseamos el cuerpo de la petición de JSON a diccionario de Python
    data = json.loads(request.body)

    # Diccionario que mapea las claves recibidas en el JSON con los modelos de Django
    modelos = {
        'estrategias': Estrategia,
        'principios': Principio,
        'descriptores': Descriptor
    }

    # Bandera para verificar si se procesó alguna clave correctamente
    procesado = False

    # Recorremos cada clave del diccionario y su modelo asociado
    for clave, modelo in modelos.items():
        # Comprobamos si esa clave está en los datos recibidos
        if clave in data:

            # Primero, pone los `step` a `null` para todos los objetos
            for objeto_id in data[clave]:
                objeto = modelo.objects.get(id=objeto_id)
                objeto.step = None  # Poner step a null
                objeto.save()

            # Luego, reasigna los `step` en el nuevo orden
            for i, objeto_id in enumerate(data[clave]):
                objeto = modelo.objects.get(id=objeto_id)
                objeto.step = i  # Establece el nuevo valor de step
                objeto.save()  # Guarda el cambio

            # Indicamos que se procesó la clave
            procesado = True
            break  # Solo procesamos una clave a la vez

    # Si no se procesó ninguna clave, devolvemos un error
    if not procesado:
        return JsonResponse({'status': 'invalid method'}, status=405)

    # Si fue bien, devolvemos una respuesta de éxito
    return JsonResponse({'status': 'ok'})
