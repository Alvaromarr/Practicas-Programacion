from functools import wraps
from typing import Any, Callable

def operation_logger(func: Callable) -> Callable:
    """
    Decorador que registra la operación ejecutada, sus argumentos y el resultado.

    Registra en consola el nombre de la operación, los argumentos posicionales
    y de palabra clave, y el resultado devuelto. Si ocurre ZeroDivisionError,
    lo registra y devuelve None.

    Parameters
    ----------
    func : Callable
        Función que ejecuta la operación matemática (e.g., math_operation).

    Returns
    -------
    Callable
        Envoltorio que añade el registro alrededor de la ejecución.
    """
    @wraps(func)
    def wrapper(operation: Callable, *args: Any, **kwargs: Any) -> Any:
        """
        Envoltorio del decorador que realiza el registro y captura errores.

        Parameters
        ----------
        operation : Callable
            Función u operación a ejecutar (normalmente una lambda).
        *args : Any
            Argumentos posicionales de la operación.
        **kwargs : Any
            Argumentos nombrados de la operación.

        Returns
        -------
        Any
            Resultado de la operación, o None si se produjo ZeroDivisionError.
        """
        op_name = getattr(operation, "__name__", str(operation))
        try:
            result = func(operation, *args, **kwargs)
            print(f"[LOG] op={op_name} args={args} kwargs={kwargs} -> result={result}")
            return result
        except ZeroDivisionError:
            print(f"[LOG] op={op_name} args={args} kwargs={kwargs} -> error=ZeroDivisionError")
            return None
    return wrapper

# Lambdas básicas
add: Callable[..., float] = lambda *xs: sum(xs)
subtract: Callable[[float, float], float] = lambda a, b: a - b
multiply: Callable[..., float] = lambda *xs: _prod(xs)  # type: ignore[name-defined]
divide: Callable[[float, float], float] = lambda a, b: a / b  # ZeroDivisionError si b=0

def _prod(xs: Any) -> float:
    """
    Calcula el producto de una colección de valores numéricos.

    Parameters
    ----------
    xs : Iterable[float]
        Secuencia de números a multiplicar.

    Returns
    -------
    float
        Producto acumulado de todos los elementos.
    """
    acc: float = 1.0
    for x in xs:
        acc *= x
    return acc

@operation_logger
def math_operation(operation: Callable, *args: Any, **kwargs: Any) -> Any:
    """
    Ejecuta una operación matemática pasada como función con sus argumentos.

    La función está decorada para registrar entradas y salidas, y manejar la
    división por cero en operaciones que la involucren.

    Parameters
    ----------
    operation : Callable
        Función u objeto invocable que implementa la operación matemática.
    *args : Any
        Argumentos posicionales para la operación.
    **kwargs : Any
        Argumentos nombrados para la operación.

    Returns
    -------
    Any
        Resultado devuelto por la operación.
    """
    return operation(*args, **kwargs)

if __name__ == "__main__":
    # Pruebas requeridas
    math_operation(add, 5, 3)
    math_operation(subtract, 10, 4)
    math_operation(multiply, 2, 6)
    math_operation(divide, 15, 3)
    math_operation(divide, 10, 0)  # Manejo división por cero
    math_operation(add, 1, 2, 3, 4, 5)
