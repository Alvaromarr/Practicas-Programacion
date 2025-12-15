from RegistroDiario import RegistroDiario
from Empleado import Empleado
from Cliente import Cliente
from Time import Time
from Utils import leer_opcion, leer_entero, leer_cadena

def leer_hora_nacimiento():
    h = leer_entero("Hora de nacimiento (0-23): ")
    m = leer_entero("Minuto de nacimiento (0-59): ")
    s = leer_entero("Segundo de nacimiento (0-59): ")
    return Time(h, m, s)

def introducir_empleado(registro):
    nombre = leer_cadena("Nombre: ")
    edad = leer_entero("Edad: ")
    nacio = leer_hora_nacimiento()
    categoria = leer_cadena("Categoría: ")
    antig = leer_entero("Años de antigüedad: ")
    emp = Empleado(nombre, edad, nacio, categoria, antig)
    registro.agregar_persona(emp)

def introducir_cliente(registro):
    nombre = leer_cadena("Nombre: ")
    edad = leer_entero("Edad: ")
    nacio = leer_hora_nacimiento()
    dni = leer_cadena("DNI: ")
    cli = Cliente(nombre, edad, nacio, dni)
    registro.agregar_persona(cli)

def buscar_por_nombre_edad(registro):
    nombre = leer_cadena("Nombre a buscar: ")
    edad = leer_entero("Edad: ")
    encontrado = False
    for p in registro._personas:
        if p.nombre == nombre and p.edad == edad:
            encontrado = True
            if isinstance(p, Empleado):
                print("Se ha encontrado un empleado:")
            else:
                print("Se ha encontrado un cliente:")
            p.visualizar()
            print("-" * 30)
    if not encontrado:
        print("No se ha encontrado la persona.")

def visualizar_por_indice(registro):
    if not registro._personas:
        print("Registro vacío")
        return
    max_idx = len(registro._personas) - 1
    idx = leer_entero(f"Índice (0 - {max_idx}): ")
    if 0 <= idx <= max_idx:
        persona = registro[idx]
        persona.visualizar()
    else:
        print("Índice fuera de rango")

def combinar_registros(registro):
    otro = RegistroDiario()
    print("Introduce datos para el segundo registro (2 personas):")
    for i in range(2):
        print(f"Persona {i+1} del otro registro")
        tipo = leer_opcion(1, 2, "1. Empleado  2. Cliente: ")
        if tipo == 1:
            introducir_empleado(otro)
        else:
            introducir_cliente(otro)
    combinado = registro + otro
    print("Registro combinado:")
    combinado.visualizar_registro()
    return combinado

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Introducir empleado")
    print("2. Introducir cliente")
    print("3. Buscar por nombre (y edad)")
    print("4. Mostrar registro diario")
    print("5. Mostrar empleados")
    print("6. Visualizar persona por índice")
    print("7. Combinar registros diarios")
    print("8. Salir")

def main():
    registro = RegistroDiario()
    while True:
        mostrar_menu()
        op = leer_opcion(1, 8)
        if op == 1:
            introducir_empleado(registro)
        elif op == 2:
            introducir_cliente(registro)
        elif op == 3:
            buscar_por_nombre_edad(registro)
        elif op == 4:
            registro.visualizar_registro()
        elif op == 5:
            registro.visualizar_empleados()
        elif op == 6:
            visualizar_por_indice(registro)
        elif op == 7:
            registro = combinar_registros(registro)
        elif op == 8:
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()