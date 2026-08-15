# servicios/restaurante.py
# Estructura del proyecto:
# "servicios/restaurante.py: contiene la clase Restaurante, encargada de administrar las colecciones, registros, búsquedas,
# actualizaciones, eliminaciones y demás reglas necesarias del sistema."
# Restricción de arquitectura: esta clase NO interactúa con la consola (no usa input() ni print()); toda la interacción por consola queda delegada a main.py.
# ESTRUCTURAS DE DATOS: 
# * LIST -> self._productos y self._clientes: colecciones dinámicas de objetos, administradas íntegramente dentro de este servicio.
# * SET  -> obtener_categorias_unicas(): conjunto que evita duplicidad, aplicado a las categorías de comidas y bebidas registradas.

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """
    Servicio encargado de administrar las colecciones de productos y clientes, junto con las operaciones de registro, búsqueda, actualización, eliminación y listado del sistema. 
    PRINCIPIO SRP: Maneja exclusivamente la lógica de almacenamiento y validación en memoria, cumpliendo con la restricción de NO interactuar con la consola (sin inputs ni prints).
    """

    def __init__(self) -> None:
        # LISTA (list):
        # "Listas para administrar colecciones dinámicas de objetos. El servicio deberá mantener principalmente una lista de productos y una lista de usuarios."
        # self._productos guarda de manera conjunta Producto y su subclase Bebida (gracias al polimorfismo), evitando crear una lista independiente solo para bebidas.
        # self._clientes guarda objetos de la clase Cliente, sin subclases (restricción: "No implementar todavía jerarquías avanzadas de clientes, empleados o administradores").
        # Ambas listas son privadas: main.py nunca las recorre ni las modifica directamente, solo a través de los métodos públicos de esta clase (restricción: "Evitar que main.py modifique
        # directamente las listas internas del servicio").
        
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    # PRODUCTOS

    def registrar_producto(self, producto: Producto) -> str:
        """
        Registro de productos y Evitar códigos de productos duplicados.
        Uso de LISTA: agrega el nuevo producto mediante list.append().
        """
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return f"Error: Ya existe un producto con el código {producto.codigo}."

        self._productos.append(producto)
        return f'El producto "{producto.nombre}" fue registrado exitosamente.'

    def buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
        """
        Implementar la búsqueda de productos, utilizando un criterio coherente como su código.
        Uso de LISTA: recorre self._productos con un for para localizar el elemento buscado.
        """
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
    ) -> str:
        """
        Implementar la actualización de productos. 
        Localiza el producto dentro de la LISTA self._productos (a través de buscar_producto_por_codigo) y modifica sus atributos mediante los setters expuestos por Producto.
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return f"Error: No existe un producto con el código {codigo}."

        if nombre:
            producto.nombre = nombre
        if categoria:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio

        return f'El producto "{producto.codigo}" fue actualizado exitosamente.'

    def eliminar_producto(self, codigo: str) -> str:
        """
        Implementar la eliminación de productos.
        Uso de LISTA: elimina el elemento localizado mediante list.remove().
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return f"Error: No existe un producto con el código {codigo}."

        self._productos.remove(producto)
        return f'El producto "{codigo}" fue eliminado exitosamente.'

    def listar_productos(self) -> list[str]:
        """
        Implementar el listado de productos.
        Uso de LISTA: recorre self._productos con comprensión de lista.
        PRINCIPIO LSP & POLIMORFISMO: invoca mostrar_informacion() de forma transparente para Productos y Bebidas. 
        No se utilizan condiciones repetidas (como isinstance) para determinar el tipo de objeto.
        """
        return [producto.mostrar_informacion() for producto in self._productos]

    def obtener_categorias_unicas(self) -> set[str]:
        """
        CONJUNTO (set): Utilice un conjunto para obtener información que deba mostrarse sin elementos duplicados. Por ejemplo, obtener y
        presentar las categorías únicas de los productos registrados."

        Recorre la LISTA self._productos (productos y bebidas registrados) y construye un CONJUNTO con sus categorías. Como el set no admite valores repetidos, cada categoría de comida o
        bebida aparece una única vez sin importar cuántos productos la compartan (evita duplicidad).
        """
        categorias: set[str] = set()
        for producto in self._productos:
            categorias.add(producto.categoria)
        return categorias

    # CLIENTES

    def registrar_cliente(self, cliente: Cliente) -> str:
        """
        Permitir el registro y listado de usuarios y Evitar identificaciones de usuarios duplicadas.
        Uso de LISTA: agrega el nuevo cliente mediante list.append().
        """
        if self._buscar_cliente_por_identificacion(cliente.identificacion) is not None:
            return (
                f"Error: Ya existe un cliente con la identificación "
                f"{cliente.identificacion}."
            )

        self._clientes.append(cliente)
        return f'El cliente "{cliente.nombre}" fue registrado exitosamente.'

    def listar_clientes(self) -> list[str]:
        """
        Permitir el registro y listado de usuarios.
        Uso de LISTA: recorre self._clientes con comprensión de lista.
        """
        return [cliente.mostrar_informacion() for cliente in self._clientes]

    def _buscar_cliente_por_identificacion(self, identificacion: str) -> Cliente | None:
        # Uso de anotaciones de tipos (type hints) en métodos privados. Uso de LISTA: recorre self._clientes con un for para validar identificaciones duplicadas.
        for cliente in self._clientes:
            if cliente.identificacion == identificacion:
                return cliente
        return None

