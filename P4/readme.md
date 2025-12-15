Pregunta: ¿Qué estructura debería tener la clase CMatFloat con numpy para crear matrices 1D/2D, introducir y mostrar datos, verificar existencia y hacer suma/resta con otra matriz?​
LLM utilizada: Grok.​
¿Respuesta correcta? Sí.​
Mini-resumen: La propuesta encaja con la práctica: usar np.ndarray internamente, crear con np.zeros en 1D como 1×n y en 2D como f×c, validar dimensiones antes de operar y exponer métodos claros (CrearMatriz1D, CrearMatriz2D, Introducir, Mostrar, Existe, SumarMatrices y RestarMatrices) que mantienen el estado consistente y evitan errores de forma.​

Pregunta: ¿Cómo conviene implementar leer_int, leer_float y crear_menu para que sean reutilizables y robustos en próximas prácticas?​
LLM utilizada: Grok.​
¿Respuesta correcta? Sí.​
Mini-resumen: Recomienda bucles con try/except que repitan hasta entrada válida, normalizar coma a punto en decimales y un menú numerado que no permita salir del rango 1..N, lo que reduce fallos de usuario y facilita reusar estas funciones en otros ejercicios sin duplicar lógica.​

Pregunta: Estoy bloqueado y me frustra que al sumar matrices falle; (enunciado con sentimiento)​
LLM utilizada: Grok.​
¿Respuesta correcta? Sí.​
Mini-resumen: Aconseja comprobar que ambas matrices existen, que sus shapes coinciden exactamente y que los datos son float, además de imprimir las dimensiones antes de operar; con esos chequeos, la mayoría de errores se detectan en segundos y se corrigen creando la segunda matriz con las mismas dimensiones que la primera.​

Pregunta: Genera un main mínimo funcional con el menú y submenú exactos de la práctica, sin explicaciones, para ejecutarlo ya (enunciado imperativo).​
LLM utilizada: Grok.​
¿Respuesta correcta? Parcial.​
Mini-resumen: Entrega un flujo que corre y refleja las 6 opciones del menú principal y las 3 del submenú, pero con validaciones algo justas; es un buen punto de partida, aunque conviene reforzar mensajes de error y guardas para no introducir ni operar si la matriz no está creada.​

Pregunta: ¿Por qué aparece “No module named 'numpy'” al ejecutar esta práctica y cómo lo soluciono sin liarme con entornos?​
LLM utilizada: Grok.​
¿Respuesta correcta? Sí.​
Mini-resumen: El intérprete activo no ve numpy porque no está instalado en ese Python o se está usando otro entorno distinto; la solución es instalar numpy en el mismo intérprete que ejecuta el script y verificar con un import y la ruta de sys.executable para alinear instalación y ejecución.​

Pregunta: ¿Cómo debería formatear Mostrar para que un vector 1D se vea en una línea y una 2D por filas, y qué hacer si aún no existe la matriz?​
LLM utilizada: Grok.​
¿Respuesta correcta? Sí.​
Mini-resumen: Para 1D basta imprimir la única fila con valores formateados y separados, y para 2D recorrer fila a fila con un join y precisión fija; si la matriz no existe, Mostrar debe avisar al usuario en lugar de fallar o imprimir valores nulos.​

Pregunta: ¿Qué validaciones mínimas debe hacer Introducir al leer decimales por consola y cómo integrarlo de forma limpia con leer_float?​
LLM utilizada: Grok.​
¿Respuesta correcta? Sí.​
Mini-resumen: Introducir debe rechazar operar si la matriz no existe, iterar por índices pidiendo un float por posición y delegar en leer_float para reintentos y normalización; opcionalmente, aceptar inyección de una función lectora para pruebas y así desacoplar la lectura de la lógica de la clase.