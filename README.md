# ✨Restaurante App

**🌟Estudiante:** Ramiro Alcoser A.

Proyecto académico en Python para practicar Programación Orientada a Objetos y estructuras de datos.

La aplicación administra productos (incluyendo bebidas) y clientes en memoria. No utiliza bases de datos, archivos de persistencia, interfaces gráficas ni librerías externas.

## 🎯Descripción del sistema

El sistema representa la administración básica de un restaurante: permite registrar productos y bebidas, buscarlos, actualizarlos, eliminarlos y listarlos; permite además registrar y listar clientes, y mostrar las
categorías únicas de los productos registrados. Toda la información se administra en memoria mientras el programa se encuentra en ejecución.

## 🔥Estructura del proyecto

```text
restaurante_app/
|
|-- modelos/
|   |-- __init__.py
|   |-- producto.py
|   |-- bebida.py
|   `-- cliente.py
|
|-- servicios/
|   |-- __init__.py
|   `-- restaurante.py
|
|-- main.py
`-- README.md
```

## 🚀Ejecución

Desde la carpeta `restaurante_app`, ejecutar:

```bash
python main.py
```

## ✅Responsabilidades

- `modelos/producto.py`: contiene la clase `Producto`, entidad base que representa un producto del restaurante (código, nombre, categoría y
  precio).
- `modelos/bebida.py`: contiene la clase `Bebida`, que hereda de
  `Producto` y agrega el atributo `tamano`. Aplica herencia y
  polimorfismo (sobrescribe `mostrar_informacion()`).
- `modelos/cliente.py`: contiene la clase `Cliente`, entidad general que
  representa a una persona registrada en el sistema (identificación,
  nombre y correo).
- `servicios/restaurante.py`: contiene la clase `Restaurante`, encargada
  de administrar las colecciones de productos y clientes, y de las
  operaciones de registro, búsqueda, actualización, eliminación y
  listado. No interactúa con la consola (sin `input()` ni `print()`).
- `main.py`: contiene el menú de consola, la interacción por consola
  y la coordinación de las llamadas al servicio `Restaurante`.

## 📚Uso justificado de las estructuras de datos

El proyecto utiliza `list`, `tuple`, `dict` y `set` en lugares donde cada
estructura cumple una responsabilidad concreta dentro del sistema. No se
reemplazan las clases `Producto`, `Bebida` y `Cliente` por diccionarios,
porque esas entidades siguen siendo objetos con atributos, propiedades y
comportamiento propio.

### 📖list: colecciones de productos y clientes

Se utiliza en `servicios/restaurante.py`, dentro de la clase
`Restaurante`:

```python
self._productos: list[Producto] = []
self._clientes: list[Cliente] = []
```

La lista es apropiada porque el restaurante necesita administrar una
cantidad variable de objetos del mismo "tipo base" (`Producto`, incluida
su subclase `Bebida`) y de `Cliente`. Durante la ejecución pueden
registrarse, buscarse, actualizarse, eliminarse y listarse.

Motivo principal: una lista permite guardar una cantidad variable de
objetos, recorrerlos y modificarlos fácilmente.

Operaciones utilizadas:

- `append()` para registrar productos y clientes.
- `remove()` para eliminar productos.
- `for` para recorrer las listas al buscar, listar productos/clientes y
  al construir el conjunto de categorías.

No se usa `tuple` para productos o clientes porque esas colecciones sí
cambian durante la ejecución (se agregan, actualizan y eliminan
elementos). No se usa `set` porque los objetos deben mantenerse como
registros completos, con posibilidad de repetirse en algunos atributos
(por ejemplo, dos productos distintos pueden compartir la misma
categoría) y no interesa aquí la unicidad del objeto en sí.

### 📘tuple: opciones fijas del menú

Se utiliza en `main.py`:

```python
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
```

La tupla es apropiada porque las opciones del menú principal son datos
definidos por el programador ("quemados"). Quien usa el programa puede
elegir una opción, pero no debe agregar, eliminar ni modificar las
opciones mientras el programa se ejecuta.

Motivo principal: una tupla representa una colección estable, pensada
para no cambiar durante la ejecución.

También ayuda a evitar repetir muchos `print()` sueltos en
`mostrar_menu()`. El menú se imprime recorriendo la tupla:

```python
for numero, descripcion in OPCIONES_MENU:
    print(f"{numero}. {descripcion}")
```

No se usa `list` porque no se necesita modificar la colección de
opciones durante la ejecución.

### 📕dict: relación entre claves y valores

Se utiliza en `main.py`, dentro de `main()`, para relacionar cada opción
elegida por quien usa el programa con la función que debe ejecutarse:

```python
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
```

La clave es el número de opción escrito por consola, por ejemplo
`"1"`. El valor es la función que realiza la acción correspondiente, por
ejemplo `registrar_producto`.

Motivo principal: un diccionario permite ubicar directamente qué acción
corresponde a una opción, en lugar de encadenar múltiples `if`/`elif`.

No se usa una lista porque aquí interesa una relación directa clave ->
valor (número de opción -> función), no una simple secuencia de
elementos.

### ✍️set: categorías sin duplicados

Se utiliza en `servicios/restaurante.py`, en el método
`obtener_categorias_unicas()`:

```python
categorias: set[str] = set()
for producto in self._productos:
    categorias.add(producto.categoria)
return categorias
```

El conjunto es apropiado porque su característica principal es evitar
elementos duplicados. Si existen varios productos de la categoría
`sopa`, esa categoría se guarda y se muestra una sola vez.

Motivo principal: se necesita obtener valores únicos, no repetir
categorías.

No se usa una lista porque una lista permitiría duplicados. Por ejemplo,
podría terminar mostrando:

```text
sopa
sopa
ensalada
sopa
```

Con `set`, el resultado queda más limpio:

```text
sopa
ensalada
```

## 📊Menú principal

El programa permite:

1. Registrar producto
2. Registrar bebida
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Listar productos
7. Registrar cliente
8. Listar clientes
9. Mostrar categorías
0. Salir

## 🔄Reflexión sobre la elección de estructuras de datos

Elegir la estructura de datos adecuada no es un detalle menor: cada
estructura resuelve un tipo de problema distinto y usar la incorrecta
introduce errores o complejidad innecesaria. En este proyecto, usar una
lista para los productos permite que la colección crezca, se modifique y
se recorra libremente; usar una tupla para el menú deja claro que esas
opciones no deben cambiar en tiempo de ejecución, protegiendo al programa
de modificaciones accidentales; usar un diccionario para relacionar cada
opción con su función evita una larga cadena de condicionales y hace más
mantenible el despacho de acciones; y usar un conjunto para las
categorías garantiza unicidad sin tener que programar manualmente la
verificación de duplicados. En definitiva, elegir bien la estructura de
datos hace que el código exprese con mayor claridad la intención del
programador y reduce la posibilidad de errores.
