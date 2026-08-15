# main.py
# Estructura del proyecto:
# "main.py: constituye el punto de arranque. Debe mostrar el menú, solicitar información mediante consola, crear los objetos necesarios y utilizar los métodos proporcionados por el servicio."
# Restricción de arquitectura: main.py NO administra directamente las colecciones del servicio (self._productos / self._clientes); toda búsqueda, actualización o eliminación se
# solicita mediante los métodos públicos de Restaurante.
#
# ESTRUCTURAS DE DATOS SOLICITADAS
# * TUPLE -> OPCIONES_MENU y SEPARADORES_MENU: información "quemada" que no debe modificarse en tiempo de ejecución (los datos del menú están fijos).
# * DICT  -> `acciones` dentro de main(): relaciona cada opción del menú (clave) con la función que debe ejecutarse (valor).
# Se importa el módulo 're' para la validación de correos electrónicos mediante expresiones regulares.

import os
os.system("cls")  # Limpiar la consola
import re
from typing import Callable

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# TUPLA (tuple): Utilice una tupla para representar información que deba mantenerse estable durante la ejecución, por ejemplo las opciones disponibles del menú principal.
# OPCIONES_MENU es una tupla de tuplas (numero, descripcion). Son datos "quemados" definidos por el programador: quien usa el programa puede
# ELEGIR una opción escribiendo su número, pero el contenido del menú en sí (cuántas opciones hay y qué texto muestran) NO se puede agregar,
# eliminar ni modificar mientras el programa está en ejecución, porque una tupla es inmutable.

OPCIONES_MENU: tuple[tuple[str, str], ...] = (
    ("1", "Registrar producto"),
    ("2", "Registrar bebida"),
    ("3", "Buscar producto"),
    ("4", "Actualizar producto"),
    ("5", "Eliminar producto"),
    ("6", "Listar productos"),
    ("7", "Registrar cliente"),
    ("8", "Listar clientes"),
    ("9", "Mostrar categorías"),
    ("0", "Salir"),
)

# TUPLA (tuple): igual que OPCIONES_MENU, esta tupla guarda datos fijos (los números de opción después de los cuales se imprime una línea
# separadora) que tampoco deben modificarse en tiempo de ejecución.

SEPARADORES_MENU: tuple[str, ...] = ("2", "6", "8")

def mostrar_menu() -> None:
    """
    Imprime el menú recorriendo la TUPLA OPCIONES_MENU con un for, en lugar de repetir múltiples print() sueltos por cada opción.
    """
    print("\n==================================================")
    print("|        SISTEMA DE RESTAURANTE VACA & VACO      |")
    print("==================================================")
    print()
    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")
        if numero in SEPARADORES_MENU:
            print("-" * 50)
    print()


def validar_campo_vacio(valor: str, nombre_campo: str) -> bool:
    # Aplicar validaciones y manejo de excepciones cuando corresponda para evitar que entradas incorrectas detengan el programa.
    if not valor:
        print(f"Error: El campo '{nombre_campo}' es obligatorio.")
        return False
    return True


def _solicitar_precio() -> float:
    # Validación con manejo de excepción (ValueError) para que un precio inválido no detenga el programa.
    while True:
        precio_raw = input("Precio: ").strip()
        if not validar_campo_vacio(precio_raw, "Precio"):
            continue
        try:
            precio = float(precio_raw)
            if precio <= 0:
                print("Error: El precio debe ser un valor mayor a cero.")
                continue
            return precio
        except ValueError:
            print("Error: El precio debe ser un número válido.")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- REGISTRO DE PRODUCTO ---")

    # Solicitar los datos mediante input() y crear los objetos a partir de la información ingresada, evitando valores
    # quemados en el registro de productos (a diferencia del menú, que sí es información fija representada con tuple).
    while True:
        codigo = input("Código: ").strip()
        if validar_campo_vacio(codigo, "Código"):
            break

    while True:
        nombre = input("Nombre: ").strip()
        if validar_campo_vacio(nombre, "Nombre"):
            break

    while True:
        categoria = input(
            "Categoría (ej: sopa, plato fuerte, entrada, porciones, ensalada): "
        ).strip()
        if validar_campo_vacio(categoria, "Categoría"):
            break

    precio = _solicitar_precio()

    # Creación del objeto Producto a partir de los datos ingresados y delegación al servicio Restaurante
    # (main.py no administra la lista de productos directamente).
    producto = Producto(codigo, nombre, categoria, precio)
    print(restaurante.registrar_producto(producto))

def registrar_bebida(restaurante: Restaurante) -> None:
    print("\n--- REGISTRO DE BEBIDA ---")

    while True:
        codigo = input("Código: ").strip()
        if validar_campo_vacio(codigo, "Código"):
            break

    while True:
        nombre = input("Nombre: ").strip()
        if validar_campo_vacio(nombre, "Nombre"):
            break

    while True:
        categoria = input(
            "Categoría (ej: gaseosa, jugo natural, bebida caliente): "
        ).strip()
        if validar_campo_vacio(categoria, "Categoría"):
            break

    precio = _solicitar_precio()

    while True:
        tamano = input("Tamaño (ej: 100ml, 500ml, Grande): ").strip()
        if validar_campo_vacio(tamano, "Tamaño"):
            break

    # Instanciación correcta de la clase heredada Bebida con paso de parámetros dinámicos ingresados por consola.
    bebida = Bebida(codigo, nombre, categoria, precio, tamano)
    print(restaurante.registrar_producto(bebida))

def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- BÚSQUEDA DE PRODUCTO ---")

    while True:
        codigo = input("Código del producto a buscar: ").strip()
        if validar_campo_vacio(codigo, "Código"):
            break

    # Rrestricción de arquitectura: main.py NO recorre la lista interna del servicio; delega la búsqueda al método buscar_producto_por_codigo() de Restaurante.
    producto = restaurante.buscar_producto_por_codigo(codigo)
    if producto is None:
        print(f"No se encontró ningún producto con el código {codigo}.")
        return

    print("Producto encontrado:")
    print(producto.mostrar_informacion())

def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- ACTUALIZACIÓN DE PRODUCTO ---")

    while True:
        codigo = input("Código del producto a actualizar: ").strip()
        if validar_campo_vacio(codigo, "Código"):
            break

    if restaurante.buscar_producto_por_codigo(codigo) is None:
        print(f"Error: No existe un producto con el código {codigo}.")
        return

    print("Deje el campo vacío si no desea modificarlo.")
    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()
    precio_raw = input("Nuevo precio: ").strip()

    precio: float | None = None
    if precio_raw:
        try:
            precio = float(precio_raw)
            if precio <= 0:
                print("Error: El precio debe ser un valor mayor a cero.")
                return
        except ValueError:
            print("Error: El precio debe ser un número válido.")
            return

    # Restricción de arquitectura: la actualización real del producto ocurre dentro de Restaurante.actualizar_producto,
    # no accediendo directamente a la lista interna del servicio.
    mensaje = restaurante.actualizar_producto(
        codigo,
        nombre=nombre or None,
        categoria=categoria or None,
        precio=precio,
    )
    print(mensaje)

def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- ELIMINACIÓN DE PRODUCTO ---")

    while True:
        codigo = input("Código del producto a eliminar: ").strip()
        if validar_campo_vacio(codigo, "Código"):
            break

    print(restaurante.eliminar_producto(codigo))

def registrar_cliente(restaurante: Restaurante) -> None:
    print("\n--- REGISTRO DE CLIENTE ---")

    # Validación de formato (10 dígitos numéricos) para evitar que una identificación mal escrita detenga el programa o
    # ensucie la colección de clientes.
    while True:
        identificacion = input("Cédula de identidad: ").strip()
        if not validar_campo_vacio(identificacion, "Identificación"):
            continue
        if not (identificacion.isdigit() and len(identificacion) == 10):
            print(
                "Error: La identificación (cédula) debe contener exactamente "
                "10 dígitos numéricos."
            )
            continue
        break

    while True:
        nombre = input("Nombre: ").strip()
        if validar_campo_vacio(nombre, "Nombre"):
            break

    while True:
        correo = input("Correo (ej: pepe@hotmail.com): ").strip()
        if not validar_campo_vacio(correo, "Correo"):
            continue
        patron_correo = r"^[\w.-]+@[\w.-]+\.\w+$"
        if not re.match(patron_correo, correo):
            print("Error: El formato del correo electrónico no es válido.")
            continue
        break

    # Creación del objeto Cliente a partir de datos ingresados por consola y delegación al servicio Restaurante.
    cliente = Cliente(identificacion, nombre, correo)
    print(restaurante.registrar_cliente(cliente))

def mostrar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("\nNo existen productos o bebidas registrados.")
        return

    print("\n=== PRODUCTOS REGISTRADOS ===")
    for info in productos:
        print(info)

def mostrar_clientes(restaurante: Restaurante) -> None:
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("\nNo existen clientes registrados.")
        return

    print("\n=== CLIENTES REGISTRADOS ===")
    for info in clientes:
        print(info)

def mostrar_categorias(restaurante: Restaurante) -> None:
    # El servicio retorna un CONJUNTO (set) de categorías únicas; aquí solo se ordena con sorted() para presentarlo de forma legible,
    # sin alterar su naturaleza de valores sin duplicados.
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("\nNo existen categorías registradas todavía.")
        return

    print("\n=== CATEGORÍAS ÚNICAS REGISTRADAS ===")
    for categoria in sorted(categorias):
        print(f"- {categoria}")

def main() -> None:
    # Restricción de arquitectura): "main.py no administra colecciones directamente." Toda la lógica interna de
    # almacenamiento (listas y conjunto de categorías) está delegada a la instancia de Restaurante.
    restaurante = Restaurante()

    # DICCIONARIO (dict):
    # Utilice un diccionario cuando exista una relación clara de clave -> valor. Preferiblemente puede asociar las opciones del menú con las funciones correspondientes.
    # La clave es el número de opción escrito por consola (coincide con el primer valor de cada tupla en OPCIONES_MENU); el valor es la
    # función que ejecuta esa acción. Esto reemplaza una larga cadena de if/elif por una búsqueda directa en el diccionario.
    
    acciones: dict[str, Callable[[Restaurante], None]] = {
        "1": registrar_producto,
        "2": registrar_bebida,
        "3": buscar_producto,
        "4": actualizar_producto,
        "5": eliminar_producto,
        "6": mostrar_productos,
        "7": registrar_cliente,
        "8": mostrar_clientes,
        "9": mostrar_categorias,
    }

    # Implementar un menú interactivo ejecutado desde main.py, manteniendo el programa en ejecución hasta que se seleccione la opción de salir.
    while True:
        mostrar_menu()
        opcion = input("Por favor Seleccione una opcion -> : ").strip()

        if opcion == "0":
            print("\nHas finalizado correctamente.")
            print()
            break

        # USO DEL DICCIONARIO: dict.get() busca la función asociada a la opción elegida; si la clave no existe, se informa un error sin detener el programa.
        accion = acciones.get(opcion)
        if accion is None:
            print("\nError: Seleccione una opción válida del menú.")
            continue

        accion(restaurante)


if __name__ == "__main__":
    main()


# RHAM!
