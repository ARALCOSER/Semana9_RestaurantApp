# modelos/producto.py
# Estructura del proyecto):
# "Implementar o conservar la clase Producto en modelos/producto.py".
# "Producto deberá manejar información coherente como código, nombre, categoría y precio."

class Producto:
    """
    Clase base que representa un producto general del restaurante.
    Define los atributos obligatorios de Producto (código, nombre, categoría y precio) y expone métodos para acceder y modificar dichos atributos de forma controlada.
    PRINCIPIO SRP (Responsabilidad Única): Su única responsabilidad es modelar y exponer los datos propios del producto. No conoce nada sobre el registro de productos ni la interacción por consola.
    PRINCIPIO OCP (Abierto/Cerrado): Permite extender el catálogo a nuevos tipos de productos (como Bebida, postres, sopas, etc.) mediante
    herencia, sin modificar la lógica ya existente del servicio Restaurante.
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        # Utilizar anotaciones de tipos de datos en constructores, métodos y funciones" -> parámetros y retorno anotados con type hints (str, float, None).
        # Encapsulamiento mediante atributos protegidos (prefijo "_") e identificadores descriptivos (evita nombres genéricos como x, dato u objeto).
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio

    # Uso de propiedades (@property) para el acceso seguro y controlado a la información del producto, en lugar de exponer directamente los atributos protegidos.
    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        # Permite que servicios/restaurante.py actualice el nombre del producto (requisito: "Implementar la actualización de productos") sin exponer directamente el atributo protegido.
        self._nombre = nuevo_nombre

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str) -> None:
        self._categoria = nueva_categoria

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        self._precio = nuevo_precio

    def mostrar_informacion(self) -> str:
        """
        Define el comportamiento común para presentar la información de cualquier producto.
        PRINCIPIO LSP (Sustitución de Liskov): Cualquier clase hija (por ejemplo Bebida) puede sustituir a Producto aquí sin alterar el comportamiento esperado por quien llama al método.
        """
        return (
            f"[Producto] Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )


