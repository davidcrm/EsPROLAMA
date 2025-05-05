import json

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_POST

from elama.models import Estrategia, Principio, Descriptor


@staff_member_required
@require_POST  # asegura que solo aceptemos peticiones POST.
def actualizar_orden(request: HttpRequest):
    # Parseamos el cuerpo de la petición desde JSON a diccionario de Python
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
            # Si está, recorremos la lista de IDs recibidos en esa clave
            for i, objeto_id in enumerate(data[clave]):
                try:
                    # Buscamos el objeto por su ID
                    objeto = modelo.objects.get(id=objeto_id)
                    # Actualizamos su campo 'step' con el valor de la iteración actual (posición en la tabla)
                    objeto.step = i
                    # Guardamos los cambios
                    objeto.save()
                except modelo.DoesNotExist:
                    # En caso de que no se encuentre el objeto, devolvemos error
                    return JsonResponse({'status': 'error'}, status=404)

            # Indicamos que se procesó la clave
            procesado = True
            break  # Solo procesamos una clave a la vez

    # Si no se procesó ninguna clave, devolvemos un error
    if not procesado:
        return JsonResponse({'status': 'invalid method'}, status=405)

    # Si fue bien, devolvemos una respuesta de éxito
    return JsonResponse({'status': 'ok'})