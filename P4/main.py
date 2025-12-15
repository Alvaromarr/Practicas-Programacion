# main.py
from matriz import CMatFloat, leer_int, leer_float, crear_menu

def construir_matriz_igual_dimensiones(base: CMatFloat) -> CMatFloat:
    """
    Construye y devuelve una segunda matriz con las mismas dimensiones que 'base'
    y solicita la introducción de datos.
    """
    if not base or not base.Existe():
        raise RuntimeError("La matriz base no existe")
    m2 = CMatFloat()
    m2.CrearMatriz2D(base._m_nFilas, base._m_nColumnas)
    print("Introduce los valores de la segunda matriz:")
    m2.Introducir()
    return m2

def main():
    matriz_actual = CMatFloat()

    opciones_principales = [
        "Construir matriz 1D",
        "Construir matriz 2D",
        "Introducir matriz",
        "Mostrar matriz",
        "Operaciones con matrices",
        "Terminar",
    ]

    opciones_operaciones = [
        "Sumar matrices",
        "Restar matrices",
        "Volver al menú principal",
    ]

    while True:
        print("\n--- Menú principal ---")
        opcion = crear_menu(opciones_principales)

        if opcion == 1:
            n = leer_int("Número de elementos (>=1): ")
            if n <= 0:
                print("Debe ser >= 1")
                continue
            matriz_actual.CrearMatriz1D(n)
            print("Matriz 1D creada.")
        elif opcion == 2:
            f = leer_int("Número de filas (>=1): ")
            c = leer_int("Número de columnas (>=1): ")
            if f <= 0 or c <= 0:
                print("Filas y columnas deben ser >= 1")
                continue
            matriz_actual.CrearMatriz2D(f, c)
            print("Matriz 2D creada.")
        elif opcion == 3:
            if not matriz_actual.Existe():
                print("Primero crea una matriz.")
                continue
            print("Introduce los valores de la matriz actual:")
            matriz_actual.Introducir()
            print("Datos introducidos.")
        elif opcion == 4:
            matriz_actual.Mostrar()
        elif opcion == 5:
            if not matriz_actual.Existe():
                print("Primero crea e introduce la matriz actual.")
                continue
            while True:
                print("\n--- Operaciones con matrices ---")
                subop = crear_menu(opciones_operaciones)
                if subop == 1:
                    try:
                        m2 = construir_matriz_igual_dimensiones(matriz_actual)
                        res = matriz_actual.SumarMatrices(m2)
                        print("Resultado de la suma:")
                        # Mostrar resultado formateado
                        if res.shape[0] == 1:
                            fila = "  ".join(f"{x:.6g}" for x in res[0, :])
                            print(f"[ {fila} ]")
                        else:
                            for i in range(res.shape[0]):
                                fila = "  ".join(f"{x:.6g}" for x in res[i, :])
                                print(f"[ {fila} ]")
                    except Exception as e:
                        print(f"Error: {e}")
                elif subop == 2:
                    try:
                        m2 = construir_matriz_igual_dimensiones(matriz_actual)
                        res = matriz_actual.RestarMatrices(m2)
                        print("Resultado de la resta:")
                        if res.shape[0] == 1:
                            fila = "  ".join(f"{x:.6g}" for x in res[0, :])
                            print(f"[ {fila} ]")
                        else:
                            for i in range(res.shape[0]):
                                fila = "  ".join(f"{x:.6g}" for x in res[i, :])
                                print(f"[ {fila} ]")
                    except Exception as e:
                        print(f"Error: {e}")
                elif subop == 3:
                    break
        elif opcion == 6:
            print("Terminando...")
            break

if __name__ == "__main__":
    main()
