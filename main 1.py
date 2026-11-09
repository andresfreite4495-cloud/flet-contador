"""Contador interactivo con Flet (programación orientada a objetos).

Ejecutar con:  flet run main.py   (o)   python main.py
"""

import flet as ft


class ContadorModelo:
    """Responsabilidad: guardar el estado del contador y su lógica.

    No sabe nada de la interfaz gráfica: solo maneja números.
    """

    def __init__(self, valor_inicial: int = 0):
        self.valor = valor_inicial

    def incrementar(self) -> None:
        self.valor += 1

    def reiniciar(self) -> None:
        self.valor = 0


@ft.control
class ContadorVista(ft.Column):
    """Responsabilidad: construir los componentes visuales y responder a los eventos.

    Es un control personalizado (compuesto) que hereda de ft.Column.
    """

    def init(self):
        # Estado (objeto del modelo)
        self.modelo = ContadorModelo()

        # Componentes gráficos
        self.texto = ft.Text(value=str(self.modelo.valor), size=64, weight=ft.FontWeight.BOLD)
        self.boton_sumar = ft.Button(
            content="Sumar +1", icon=ft.Icons.ADD, on_click=self.al_hacer_clic_sumar
        )
        self.boton_reiniciar = ft.Button(
            content="Reiniciar", icon=ft.Icons.REFRESH, on_click=self.al_hacer_clic_reiniciar
        )

        # Organización de los componentes dentro de la columna
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Text("Contador interactivo", size=22),
            self.texto,
            ft.Row(
                [self.boton_sumar, self.boton_reiniciar],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]

    # ---- Manejadores de eventos (se ejecutan cuando el usuario hace clic) ----
    def al_hacer_clic_sumar(self, e):
        self.modelo.incrementar()
        self.actualizar_texto()

    def al_hacer_clic_reiniciar(self, e):
        self.modelo.reiniciar()
        self.actualizar_texto()

    def actualizar_texto(self) -> None:
        """Refleja el valor del modelo en la interfaz."""
        self.texto.value = str(self.modelo.valor)
        self.update()  # envía el cambio a la pantalla


def main(page: ft.Page):
    """Crea la ventana principal y agrega el contador."""
    page.title = "Contador con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ContadorVista())


ft.run(main)
