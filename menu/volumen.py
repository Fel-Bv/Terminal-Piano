from consola.ASCII.menu.volumen import imprimir_menu_volumen
from consola.ASCII.titulo import imprimir_titulo
from consola.consola import consola

volumen_actual = 75
opcion = ''

def bajar_volumen():
    global volumen_actual

    volumen_actual -= 1 if volumen_actual > 0 else 0

def subir_volumen():
    global volumen_actual

    volumen_actual += 1 if volumen_actual < 100 else 0

def iniciar_menu_volumen():
    global volumen_actual
    global opcion

    while True:
        consola.limpiar()
        imprimir_titulo()
        imprimir_menu_volumen(volumen_actual, opcion)
        opcion = consola.leer_caracter()

        if opcion == '+':
            subir_volumen()
        elif opcion == '-':
            bajar_volumen()
        elif opcion == 'S':
            break
