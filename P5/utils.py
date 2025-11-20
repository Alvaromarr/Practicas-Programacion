from typing import Any, Dict, List, Optional, Type
from uuid import uuid4

def generar_id8() -> str:
    """
    Genera un ID único aleatorio de 8 caracteres basado en UUID v4.

    Returns
    -------
    str
        Identificador de 8 caracteres hexadecimales, sin guiones.
    """
    return str(uuid4()).replace("-", "")[:8]

def leer_int(prompt: str, annotation: Optional[Type[int]] = int) -> int:
    """
    Lee un entero desde entrada estándar validando la anotación de tipo.

    Parameters
    ----------
    prompt : str
        Mensaje a mostrar al usuario.
    annotation : Optional[Type[int]]
        Anotación esperada; si no es int, se lanza TypeError.

    Returns
    -------
    int
        Valor entero convertido desde la entrada.

    Raises
    ------
    TypeError
        Si la anotación no es int.
    ValueError
        Si la entrada no puede convertirse a int.
    """
    valor = input(prompt)
    if annotation is not None and annotation is not int:
        raise TypeError("Se esperaba tipo int en anotación")
    try:
        return int(valor)
    except ValueError:
        raise ValueError("Entrada no convertible a int")

def leer_float(prompt: str, annotation: Optional[Type[float]] = float) -> float:
    """
    Lee un flotante desde entrada estándar validando la anotación de tipo.

    Parameters
    ----------
    prompt : str
        Mensaje a mostrar al usuario.
    annotation : Optional[Type[float]]
        Anotación esperada; si no es float, se lanza TypeError.

    Returns
    -------
    float
        Valor flotante convertido desde la entrada.

    Raises
    ------
    TypeError
        Si la anotación no es float.
    ValueError
        Si la entrada no puede convertirse a float.
    """
    valor = input(prompt)
    if annotation is not None and annotation is not float:
        raise TypeError("Se esperaba tipo float en anotación")
    try:
        return float(valor)
    except ValueError:
        raise ValueError("Entrada no convertible a float")

def crear_menu(titulo: str, opciones: List[str]) -> int:
    """
    Crea un menú textual numerado y devuelve la opción seleccionada.

    Parameters
    ----------
    titulo : str
        Título visible del menú.
    opciones : List[str]
        Lista de etiquetas de opciones. Debe ser una lista de cadenas.

    Returns
    -------
    int
        Número de opción seleccionada en el rango [0, len(opciones)].

    Raises
    ------
    TypeError
        Si opciones no es una lista de cadenas.
    """
    if not isinstance(opciones, list) or not all(isinstance(o, str) for o in opciones):
        raise TypeError("opciones debe ser List[str]")
    print(f"\n=== {titulo} ===")
    for i, op in enumerate(opciones, 1):
        print(f"{i}. {op}")
    print("0. Salir")
    while True:
        sel = input("Seleccione opción: ")
        if sel.isdigit():
            n = int(sel)
            if 0 <= n <= len(opciones):
                return n
        print("Opción inválida. Intente de nuevo.")

def validar_lista(valor: Any, subtype: Type = str) -> List[Any]:
    """
    Valida que el valor sea una lista cuyos elementos son del subtipo indicado.

    Parameters
    ----------
    valor : Any
        Valor a comprobar.
    subtype : Type
        Tipo esperado de los elementos de la lista.

    Returns
    -------
    List[Any]
        La misma lista si pasa la validación.

    Raises
    ------
    TypeError
        Si el valor no es una lista o sus elementos no son del tipo esperado.
    """
    if not isinstance(valor, list) or not all(isinstance(x, subtype) for x in valor):
        raise TypeError("Se esperaba List del subtipo indicado")
    return valor

def validar_dict(valor: Any, key_t: Type = str, val_t: Type = Any) -> Dict[Any, Any]:
    """
    Valida que el valor sea un diccionario con tipos de clave y valor esperados.

    Parameters
    ----------
    valor : Any
        Valor a comprobar.
    key_t : Type
        Tipo esperado para las claves.
    val_t : Type
        Tipo esperado para los valores. Si es Any, no se valida el tipo del valor.

    Returns
    -------
    Dict[Any, Any]
        El mismo diccionario si pasa la validación.

    Raises
    ------
    TypeError
        Si el valor no es dict o alguna clave/valor no coincide con los tipos.
    """
    if not isinstance(valor, dict):
        raise TypeError("Se esperaba Dict")
    for k, v in valor.items():
        if not isinstance(k, key_t) or (val_t is not Any and not isinstance(v, val_t)):
            raise TypeError("Tipos en Dict no coinciden")
    return valor
