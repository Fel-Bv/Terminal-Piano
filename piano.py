#!/usr/bin/env python3

from consola.ASCII.menu.menu import opciones as opciones_menu
from consola.ASCII.menu.menu import imprimir_menu
from consola.ASCII.teclado import imprimir_teclado
from consola.ASCII.teclado import obtener_teclas
from consola.ASCII.titulo import imprimir_titulo
from hilos.hilo_notas import HiloReproducirNota
from consola.consola import consola
import os

opcion_menu = ''

def reproducir_nota(nota: str = 'C4') -> None:
    from menu.volumen import volumen_actual

    hilo = HiloReproducirNota(nota=nota, volumen=volumen_actual)
    hilo.setDaemon(True)
    hilo.start()

def imprimir_interfaz() -> None:
    global opcion_menu

    if opcion_menu:
        from menu.registro import iniciar_menu_registro
        from menu.volumen import iniciar_menu_volumen

        {
            'R': iniciar_menu_registro,
            'V': iniciar_menu_volumen,
            'S': consola.salir,
        }[opcion_menu]()

        opcion_menu = ''

    consola.limpiar()
    imprimir_titulo()
    imprimir_teclado()
    imprimir_menu(opcion_menu)

def main() -> None:
    global opcion_menu

    consola.esconder_cursor()
    imprimir_interfaz()

    while True:
        caracter = consola.leer_caracter()

        if caracter in obtener_teclas().keys():
            break

        if caracter in opciones_menu:
            opcion_menu = caracter
            break

        if caracter in '+-':
            from menu.volumen import subir_volumen, bajar_volumen

            {
                '+': subir_volumen,
                '-': bajar_volumen
            }[caracter]()

    if caracter in obtener_teclas().keys():
        reproducir_nota(obtener_teclas()[caracter])

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        consola.salir()
