"""
modelos/bebida.py
Extiende el catálogo de productos del restaurante (Producto -> Bebida) sin modificar la lógica del servicio Restaurante,
tal como lo permite el principio OCP (Principio Abierto/Cerrado del diseño SOLID) mencionado en modelos/producto.py.
"""

from modelos.producto import Producto

class Bebida(Producto):
    """
    Clase hija de Producto que incorpora información específica de una bebida.
    Aplicación estricta de herencia (Bebida ES-UN Producto).
    PRINCIPIO LSP: Se puede usar un objeto Bebida en cualquier lugar donde se espere un Producto (por ejemplo, dentro de la misma lista de productos del servicio Restaurante).
    """

    def __init__(
        self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str
    ) -> None:
        # Reutilización del constructor de la clase base mediante super(), en lugar de repetir la asignación de atributos ya definidos en Producto.
        super().__init__(codigo, nombre, categoria, precio)
        # Incorporación de un atributo específico ( el tamaño) propio de la clase hija, manteniendo el encapsulamiento con atributo protegido y anotaciones de tipo.
        self._tamano = tamano

    @property
    def tamano(self) -> str:
        return self._tamano

    @tamano.setter
    def tamano(self, nuevo_tamano: str) -> None:
        self._tamano = nuevo_tamano

    def mostrar_informacion(self) -> str:
        """
        Sobrescribe el método aplicando POLIMORFISMO puro. Retorna la información especializada incluyendo el atributo propio de la clase hija (tamaño), sin que
        servicios/restaurante.py necesite preguntar isinstance() para saber qué tipo de producto está mostrando.
        """
        return (
            f"[Bebida] Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f} | "
            f"Tamaño: {self.tamano}"
        )


