# El "Hola Mundo" más over-engineered posible sin perder completamente la dignidad

from dataclasses import dataclass
from enum import Enum
from typing import Protocol
import logging
import time


class Idioma(Enum):
    ESPANOL = "es"


@dataclass(frozen=True)
class Mensaje:
    texto: str
    idioma: Idioma


class Renderizador(Protocol):
    def renderizar(self, mensaje: Mensaje) -> str:
        ...


class RenderizadorConsola:
    def renderizar(self, mensaje: Mensaje) -> str:
        return f"[{mensaje.idioma.value.upper()}] >>> {mensaje.texto}"


class ValidadorMensaje:
    @staticmethod
    def validar(mensaje: Mensaje) -> None:
        if not mensaje.texto:
            raise ValueError("El mensaje no puede estar vacío.")


class ServicioSaludo:
    def __init__(self, renderizador: Renderizador):
        self.renderizador = renderizador

    def ejecutar(self, mensaje: Mensaje) -> str:
        ValidadorMensaje.validar(mensaje)
        return self.renderizador.renderizar(mensaje)


class Aplicacion:
    def __init__(self):
        self.servicio = ServicioSaludo(RenderizadorConsola())

    def correr(self):
        logging.info("Inicializando sistema enterprise de saludo...")
        time.sleep(0.5)

        mensaje = Mensaje(
            texto="¿Qué fue mardito?",
            idioma=Idioma.ESPANOL
        )

        salida = self.servicio.ejecutar(mensaje)
        print(salida)

        logging.info("Proceso finalizado correctamente.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = Aplicacion()
    app.correr()