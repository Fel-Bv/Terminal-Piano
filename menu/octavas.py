from consola.ASCII.menu.octavas import imprimir_menu_octavas
from consola.ASCII.titulo import imprimir_titulo
from consola.consola import consola

octavas_actuales = [4, 5]
opcion = ''

def subir_octavas():
    global octavas_actuales

    if octavas_actuales[1] < 6:
        octavas_actuales[1] += 1
        octavas_actuales[0] += 1

def bajar_octavas():
    global octavas_actuales

    if octavas_actuales[0] > 1:
        octavas_actuales[1] -= 1
        octavas_actuales[0] -= 1

def iniciar_menu_octavas():
    global octavas_actuales
    global opcion

    while True:
        consola.limpiar()
        imprimir_titulo()
        imprimir_menu_octavas(octavas_actuales, opcion)
        opcion = consola.leer_caracter()

        if opcion in '+L':
            subir_octavas()
        elif opcion in '-J':
            bajar_octavas()
        elif opcion == 'S':
            break

