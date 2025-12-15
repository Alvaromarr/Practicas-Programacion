Pregunta: ¿Qué elementos clave debe tener el decorador operation_logger para registrar correctamente la operación, sus entradas y el resultado, incluyendo el manejo explícito de errores como la división por cero?​​
LLM utilizada: Grok.​​
¿Respuesta correcta? Sí.​​
Mini-resumen: Plantea un decorador que envuelva a la función, capture el nombre de la operación, imprima argumentos posicionales y nombrados, ejecute dentro de un bloque try/except y, en caso de ZeroDivisionError, registre el fallo y devuelva un valor neutro o None en lugar de romper todo el flujo del programa.​​

Pregunta: ¿Cómo deberían definirse las lambdas de suma, resta, multiplicación y división para que funcionen tanto con múltiples argumentos como con la validación previa que hace math_operation?​​
LLM utilizada: Grok.​​
¿Respuesta correcta? Sí.​​
Mini-resumen: Sugiere usar lambdas que acepten *args en suma y multiplicación para operar sobre todos los elementos, mantener firmas simples con dos parámetros en resta y división, y delegar los chequeos de cantidad de argumentos en math_operation o en validaciones internas, equilibrando flexibilidad y claridad de uso.​​

Pregunta: ¿Qué responsabilidad concreta debe tener math_operation al combinar el decorador, la función lambda recibida y los *args/**kwargs para que el sistema sea extensible a nuevas operaciones?​​
LLM utilizada: Grok.​​
¿Respuesta correcta? Sí.​​
Mini-resumen: Indica que math_operation solo debe encargarse de invocar la operación con los argumentos dados y devolver su resultado, dejando el registro al decorador y la lógica matemática a la lambda, lo que permite añadir funciones nuevas sin tocar el flujo principal.​​

Pregunta: ¿Cómo conviene diseñar la clase Book usando atributos privados y @property para controlar el estado “prestado” sin exponer directamente los campos internos?​​
LLM utilizada: Grok.​​
¿Respuesta correcta? Sí.​​
Mini-resumen: Propone almacenar título, autor, ISBN y estado como atributos privados con guion bajo doble, exponer getters y setters con @property para validar cambios y garantizar que el flag de préstamo solo se modifique mediante estos accesores controlados, manteniendo la encapsulación limpia.​​

Pregunta: ¿Qué operaciones mínimas debe ofrecer la clase Library para gestionar libros y usuarios y cómo debería coordinar internamente los métodos de préstamo y devolución?​​
LLM utilizada: Grok.​​
¿Respuesta correcta? Sí.​​
Mini-resumen: Señala que la biblioteca debe permitir agregar y eliminar libros, registrar usuarios, buscar por título, autor o ISBN y, al prestar o devolver, verificar existencia de usuario y libro, revisar si el libro está libre u ocupado y sincronizar siempre el estado del libro con la lista de préstamos del usuario.​​

Pregunta: ¿De qué forma puede la clase User almacenar y mostrar sus libros prestados para que __str__ genere una descripción legible sin acoplarse a detalles de Library?​​
LLM utilizada: Grok.​​
¿Respuesta correcta? Sí.​​
Mini-resumen: Recomienda que User mantenga una lista privada de objetos Book, proporcione métodos para añadir y eliminar préstamos y en __str__ forme una cadena con los títulos o un mensaje “Sin libros”, manteniendo así su propia representación sin depender de cómo la biblioteca gestiona las colecciones globales.​​

Pregunta: ¿Cómo debería integrarse utils.py con main.py para crear un menú robusto que use leer_int, crear_menu y generar_id sin duplicar lógica de validación en cada opción?​​
LLM utilizada: Grok.​​
¿Respuesta correcta? Sí.​​
Mini-resumen: Plantea que main delegue toda la lectura y validación numérica en utils, llame a crear_menu para mostrar las opciones y obtener una elección segura, y use generar_id al registrar usuarios, de forma que el bucle principal solo orqueste llamadas a funciones de biblioteca sin reimplementar comprobaciones de entrada.​