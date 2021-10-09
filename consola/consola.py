from consola.colores import colores
from shutil import get_terminal_size
import tty
import sys
import os

class Consola:
    @property
    def tamaño(self) -> int:
        tamaño_terminal = get_terminal_size()
        return tamaño_terminal.columns

    @property
    def lineas(self) -> int:
        tamaño_terminal = get_terminal_size()
        return tamaño_terminal.lines

    def limpiar(self) -> None:
        os.system('clear 2>/dev/null || cls 2>/dev/null')

    def leer_caracter(self) -> str:
        caracter = ''
        tty.setcbreak(sys.stdin)

        try: caracter = sys.stdin.read(1)
        except KeyboardInterrupt: self.salir()

        return caracter

    def centrar_texto(self, texto: str) -> None:
        if len(texto) < self.tamaño:
            espacios = ' ' * ((self.tamaño - len(texto)) // 2)
            texto = espacios + texto + espacios
        return texto

    def esconder_cursor(self) -> None:
        print('\x1b[?25l', end='')

    def mostrar_cursor(self) -> None:
        print('\x1b[?25h', end='')

    def salir(self):
        print(f'\b\b  \n{colores.verde}Saliendo...{colores.default}')
        self.mostrar_cursor()
        # tty.setraw(sys.stdin)
        sys.exit(0)

consola = Consola()
