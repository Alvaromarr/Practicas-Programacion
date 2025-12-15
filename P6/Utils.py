
def leer_opcion(min_op, max_op, mensaje="Opción: "):
    while True:
        try:
            op = int(input(mensaje))
            if min_op <= op <= max_op:
                return op
            print(f"Introduce un número entre {min_op} y {max_op}")
        except ValueError:
            print("Debes introducir un número entero")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes introducir un número entero")

def leer_cadena(mensaje):
    while True:
        cad = input(mensaje).strip()
        if cad:
            return cad
        print("La cadena no puede estar vacía")
