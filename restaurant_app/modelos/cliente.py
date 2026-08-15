# modelos/cliente.py
# Estructura del proyecto):
# "Implementar la clase cliente en modelos/cliente.py" -> en el proyecto se implementa como Cliente, entidad general que representa a una persona registrada en el sistema del restaurante.
# "Cliente deberá manejar información general como identificación, nombre y correo" -> Cliente maneja exactamente esos tres atributos.
# "No implementar todavía jerarquías avanzadas de clientes, empleados o administradores" -> Cliente se mantiene como una única clase general, sin subclases.

class Cliente:
    """
    Representa a un cliente registrado en el restaurante.
    PRINCIPIO SRP (Responsabilidad Única): Su única responsabilidad es modelar y exponer los datos propios del cliente (identificación,
    nombre y correo). No conoce nada sobre el menú, el registro de productos ni la interacción por consola.
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        # Anotaciones de tipos de datos en el constructor y encapsulamiento mediante atributos protegidos.
        self._identificacion = identificacion
        self._nombre = nombre
        self._correo = correo

    # Propiedades (@property) para exponer la información de forma controlada, sin permitir su modificación directa desde fuera de la clase.
    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    def mostrar_informacion(self) -> str:
        return (
            f"Cédula: {self.identificacion} | Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )


