Mi Proyecto API REST
Este es un proyecto de API RESTful desarrollado con Django y Django REST Framework. A continuación, se detallan las convenciones REST y la arquitectura utilizadas.

Reglas REST
Esta API se adhiere a los principios REST clave para garantizar un diseño consistente, predecible y escalable.

1. Stateless (Sin Estado)
Cada petición que el cliente hace al servidor debe contener toda la información necesaria para que el servidor la entienda y la procese. El servidor no guarda ningún estado o sesión del cliente entre peticiones. Esto significa que la autenticación, por ejemplo, debe enviarse en cada solicitud (como un token). Esto simplifica el diseño del servidor y mejora la escalabilidad, ya que cualquier servidor puede manejar cualquier petición.

2. JSON como Formato de Intercambio
Toda la comunicación entre el cliente y el servidor se realiza utilizando el formato JSON (JavaScript Object Notation). El cliente debe especificar en las cabeceras de la petición que está enviando JSON (Content-Type: application/json), y el servidor siempre responderá con este mismo formato. JSON es ligero, legible por humanos y fácil de procesar por las máquinas.

3. Versionado en la Ruta
Para gestionar los cambios en la API a lo largo del tiempo sin romper la compatibilidad con clientes antiguos, se utiliza el versionado directamente en la URL. Todas las rutas de la API están prefijadas con /api/v1/. Si en el futuro se introduce un cambio significativo que no es compatible con la versión anterior, se crearía una nueva versión, como /api/v2/.

4. Idempotencia
La idempotencia garantiza que realizar la misma petición varias veces produce el mismo resultado que hacerla una sola vez. En esta API:

GET: Realizar una petición GET múltiples veces para obtener un recurso siempre devolverá el mismo dato sin cambiar el estado del servidor.

PATCH / PUT: Si envías una actualización a un recurso (por ejemplo, cambiar el nombre de un producto) una o varias veces, el estado final del recurso será el mismo después de la primera petición. El resultado no cambia con las repeticiones.

DELETE: Eliminar un recurso una vez lo borrará. Las siguientes peticiones para eliminar el mismo recurso simplemente confirmarán que ya no existe (ej. error 404), pero el estado del sistema (el recurso borrado) no cambiará.

Diagrama de Arquitectura

[Cliente (curl/SPA)]
        |
      HTTP/JSON
        |
[ API /api/v1 (DRF ViewSets/URLs) ]
        |
[ Logica/Serializer (validacion) ]
        |
[ Modelo Django (ORM) ]
        |
[ DB SQLite (local) ]


Cliente (curl/SPA): Es la capa de presentación que consume la API, como una aplicación web (React, Vue) o una herramienta como curl.

API /api/v1 (DRF ViewSets/URLs): Define las rutas (endpoints) y controla qué peticiones HTTP (GET, POST, etc.) se aceptan.

Lógica/Serializers (validación): Transforma los datos de la base de datos a JSON y viceversa, aplicando reglas de validación.

Modelo Django (ORM): Representa la estructura de las tablas de la base de datos como clases de Python, facilitando las operaciones.

DB SQLite (local): Es el motor de base de datos donde se almacenan y persisten todos los datos de la aplicación.
