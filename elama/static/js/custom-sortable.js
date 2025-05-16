/**
 * Inicializa un sistema de ordenación drag-and-drop para filas de una tabla HTML.
 *
 * @param {Object} options - Opciones de configuración.
 * @param {HTMLElement} options.tbody - El elemento <tbody> de la tabla cuyas filas se pueden ordenar.
 * @param {string} options.modelName - Nombre del modelo que se enviará al backend (clave del JSON).
 * @param {string} options.csrfToken - Token CSRF para proteger la petición POST en Django.
 * @param {string} options.endpoint - URL del endpoint donde se enviará el nuevo orden.
 *
 * Funcionamiento:
 * - Usa la librería Sortable para habilitar drag-and-drop en las filas.
 * - Solo las filas con clase ".handle" son arrastrables.
 * - Al soltar una fila (evento onEnd), se genera un array con el orden actual de IDs.
 * - Envía el nuevo orden al backend vía fetch con método POST y encabezados necesarios.
 * - Maneja errores mostrando un toast de alerta en caso de fallo.
 */
function customSortable({tbody, modelName, csrfToken, endpoint}) {
    new Sortable(tbody, {
        animation: 200, // Velocidad de la animación al mover filas (ms)
        handle: '.handle', // Solo elementos con esta clase son arrastrables

        // Evento que se ejecuta al terminar de arrastrar y soltar una fila
        onEnd: async () => {
            // Array para guardar el orden actual de IDs de filas
            const orden = [];
            // Recorre todas las filas <tr> en el tbody y extrae el id (data-id)
            tbody.querySelectorAll('tr').forEach(tr => {
                orden.push(tr.dataset.id);
            });

            try {
                // Envía el nuevo orden al backend en formato JSON
                const response = await fetch(endpoint, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken // Token para protección CSRF en Django
                    },
                    body: JSON.stringify({[modelName]: orden}) // Envia objeto con clave modelName y valor el array orden
                });

                const data = await response.json();

                // Si la respuesta no es exitosa lanza un error con el mensaje recibido
                if (!response.ok) {
                    throw new Error(`Error al actualizar orden: ${data?.message}`);
                }

            } catch {
                // Si ocurre un error muestra una notificación tipo toast de error
                const toastMessage = new Toast({
                    message: 'Hubo un error al actualizar el orden',
                    type: 'danger',
                });
                // Elimina el toast tras 5 segundos
                setTimeout(() => {
                    toastMessage.toastContainerEl.remove();
                }, 5000);
            }
        }
    });
}
