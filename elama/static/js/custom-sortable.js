function customSortable({tbody, modelName, csrfToken, endpoint}) {
    new Sortable(tbody, {
        animation: 200, // Velocidad de la animacion
        handle: '.handle', // El elemento arrastrable es el que tiene la clase handle
        // Función para cambiar el orden
        onEnd: async () => {
            // Creamos un array vacío cada vez que se mueva una fila
            const orden = [];
            tbody.querySelectorAll('tr').forEach(tr => {
                orden.push(tr.dataset.id); // Añade el id de cada fila al array
            });
            try {
                // Enviar el nuevo orden al backend
                const response = await fetch(endpoint, {
                    method: 'POST', headers: {
                        'Content-Type': 'application/json', 'X-CSRFToken': csrfToken // Token de django para evitar problemas
                    }, body: JSON.stringify({[modelName]: orden}) // mandamos los steps en orden
                })

                const data = await response.json();

                // Lanzamos error si la respuesta da error
                if (!response.ok) {
                    throw new Error(`Error al actualizar orden: ${data?.message}`);
                }


            } catch {
                const toastMessage = new Toast({
                    message: 'Hubo un error al actualizar el orden',
                    type: 'danger',
                });
                setTimeout(() => {
                    toastMessage.toastContainerEl.remove();
                }, 5000);
            }
        }
    });
}