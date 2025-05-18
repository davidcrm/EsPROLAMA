/**
 * Crea una función que limita la frecuencia con la que se ejecuta el callback.
 * 
 * La función resultante esperará a que hayan pasado `wait` milisegundos sin 
 * nuevas llamadas antes de ejecutar `callback`. Si se llama repetidamente antes 
 * de ese tiempo, se reinicia el temporizador.
 *
 * Esto es útil para evitar ejecuciones excesivas de funciones costosas, como 
 * eventos de scroll o escritura en inputs.
 *
 * @param {Function} callback - Función a ejecutar tras el retraso.
 * @param {number} wait - Tiempo de espera en milisegundos.
 * @returns {Function} - Nueva función "debounced" que controla la ejecución.
 */
function debounce(callback, wait) {
  let timerId;
  return (...args) => {
    clearTimeout(timerId); // Cancela la ejecución pendiente si la hay
    timerId = setTimeout(() => {
      callback(...args); // Ejecuta callback tras esperar el tiempo especificado
    }, wait);
  };
}
