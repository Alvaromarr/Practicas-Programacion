# --- Pregunta 1 (Herencia y Encapsulación) ---

Pregunta: En la clase base Publicacion, ¿cómo deben definirse los atributos (titulo, autor, anio) y los decoradores @property para que las clases derivadas (Libro, Revista) puedan acceder y manipular los datos internamente, cumpliendo con la solicitud de encapsulación y uso de decoradores?
LLM utilizada: Grok.
¿Respuesta correcta? Sí.
Mini-resumen: Propone declarar los atributos como protegidos (usando un solo guion bajo, por ejemplo, self._titulo). Luego, crear el getter con @property y el setter con @<atributo>.setter, utilizando el mismo nombre del atributo (ej., titulo) para el acceso público. Esto permite la herencia y el acceso directo/controlado por las clases derivadas sin romper la encapsulación para el mundo exterior.

# --- Pregunta 2 (Polimorfismo) ---

Pregunta: ¿Qué requisito de diseño es esencial para asegurar que, al iterar sobre una lista heterogénea de objetos (Publicacion, Libro, Revista) en la opción 2 del menú, el sistema muestre correctamente la descripción detallada de cada objeto, incluyendo sus datos específicos, y cómo se implementa esto en las clases?
LLM utilizada: Grok.
¿Respuesta correcta? Sí.
Mini-resumen: El requisito esencial es el **Polimorfismo**. Esto se logra definiendo el método Descripcion() en la clase base Publicacion y redefiniéndolo (sobrescribiéndolo) en cada clase derivada (Libro y Revista). De esta forma, al llamar publicacion.Descripcion() sobre cualquier objeto de la lista, Python invocará automáticamente la versión específica de ese objeto, ya sea Libro o Revista.

# --- Pregunta 3 (Excepciones Personalizadas) ---

Pregunta: ¿Cuál es el propósito de crear la jerarquía de excepciones ErrorBiblioteca (base) y ErrorArchivo (derivada), y cómo se utiliza ErrorArchivo específicamente en las funciones de guardar y cargar publicaciones (utils.py)?
LLM utilizada: Grok.
¿Respuesta correcta? Sí.
Mini-resumen: El propósito es proporcionar un manejo de errores especializado y legible para el sistema de biblioteca. ErrorBiblioteca es la base para errores de validación genéricos (ej., año no positivo), mientras que ErrorArchivo hereda de ella y se usa para errores relacionados con la manipulación de ficheros. En utils.py, las funciones de guardar y cargar deben capturar excepciones estándar de E/S (como FileNotFoundError, IOError, EOFError) y relanzarlas como instancias de ErrorArchivo, permitiendo al main.py mostrar un mensaje de error específico al usuario en las opciones 3 y 4.

# --- Pregunta 4 (Validación de Datos con Excepciones) ---

Pregunta: Al implementar la lógica de validación para titulo o anio en el método __init__ de Publicacion, ¿cómo debe usarse ErrorBiblioteca para que el sistema muestre el mensaje de error apropiado cuando el usuario intenta añadir datos no válidos en la opción 1?
LLM utilizada: Grok.
¿Respuesta correcta? Sí.
Mini-resumen: Dentro del constructor __init__ de Publicacion, se deben incluir verificaciones condicionales (ej., si el titulo está vacío o si el anio no es un entero positivo). Si la condición no se cumple, se debe lanzar explícitamente una instancia de la excepción personalizada ErrorBiblioteca, incluyendo un mensaje descriptivo (ej., raise ErrorBiblioteca("El año debe ser un entero positivo.")). El programa principal (main.py) debe encerrar el código de creación de publicaciones en un bloque try/except ErrorBiblioteca para capturar y mostrar este mensaje al usuario.

# --- Pregunta 5 (Persistencia de Datos - Cargar) ---

Pregunta: ¿Qué mecanismos deben implementar las funciones de carga en utils.py (Opción 4) para manejar y diferenciar entre un fichero que **no existe**, un fichero que está **vacío**, o un fichero que tiene un **formato incorrecto**, y qué excepción personalizada se debe lanzar en cada caso?
LLM utilizada: Grok.
¿Respuesta correcta? Sí.
Mini-resumen: La función de carga debe usar try...except para capturar tres tipos de errores estándar durante la manipulación de ficheros:
1.  **Fichero no existe:** Capturar FileNotFoundError.
2.  **Fichero vacío:** Capturar EOFError (End Of File Error), que a menudo ocurre cuando pickle.load() intenta leer un archivo vacío.
3.  **Formato incorrecto:** Capturar pickle.UnpicklingError o IOError si el contenido no es un objeto serializado válido.
En todos los casos, la función debe lanzar una instancia de la excepción personalizada ErrorArchivo, incluyendo un mensaje que describa el error específico (ej., "El fichero no existe" o "El fichero tiene un formato incorrecto").

# --- Pregunta 6 (Diseño de la Clase Revista) ---

Pregunta: Describe cómo debe implementarse el constructor __init__ de la clase Revista para cumplir con los requisitos de la clase base Publicacion y a la vez validar su atributo adicional num_edicion usando la excepción personalizada ErrorBiblioteca.
LLM utilizada: Grok.
¿Respuesta correcta? Sí.
Mini-resumen: El constructor __init__ de Revista debe:
1.  Aceptar los parámetros de Publicacion (titulo, autor, anio) y el específico (num_edicion).
2.  Invocar el constructor de la clase base usando super().__init__(titulo, autor, anio) para inicializar y validar los atributos heredados.
3.  Validar el atributo num_edicion (debe ser un entero positivo). Si la validación falla, lanzar ErrorBiblioteca con un mensaje claro.
4.  Asignar el valor de num_edicion a un atributo protegido interno (self._num_edicion) si la validación es exitosa.

# --- Pregunta 7 (Manejo de Ficheros - Guardar) ---

Pregunta: ¿Qué módulo de Python es más adecuado para guardar los objetos Publicacion de forma eficiente y cómo debe la función de guardar (utils.py, Opción 3) manejar los errores de acceso al fichero, según lo estipulado por ErrorArchivo?
LLM utilizada: Grok.
¿Respuesta correcta? Sí.
Mini-resumen: El módulo más adecuado para guardar objetos de Python es **pickle**, ya que serializa y deserializa la estructura completa de los objetos, preservando su tipo (Libro o Revista). La función guardar_publicaciones debe usar pickle.dump() dentro de un bloque try...except. Debe capturar errores genéricos de entrada/salida como IOError o OSError que indican problemas de permiso o acceso al disco. Si se captura un error estándar, la función debe lanzar la excepción personalizada ErrorArchivo con un mensaje descriptivo para indicar un fallo al guardar el fichero.