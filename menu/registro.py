from consola.ASCII.menu.registro import imprimir_menu_registro
from consola.ASCII.titulo import imprimir_titulo
from consola.consola import consola

registros_actuales = [4, 5]
opcion = ''

def subir_registros():
    global registros_actuales

    if registros_actuales[1] < 6:
        registros_actuales[1] += 1
        registros_actuales[0] += 1

def bajar_registros():
    global registros_actuales

    if registros_actuales[0] > 1:
        registros_actuales[1] -= 1
        registros_actuales[0] -= 1

def iniciar_menu_registro():
    global registros_actuales
    global opcion

    while True:
        consola.limpiar()
        imprimir_titulo()
        imprimir_menu_registro(registros_actuales, opcion)
        opcion = consola.leer_caracter()

        if opcion in '+L':
            subir_registros()
        elif opcion in '-J':
            bajar_registros()
        elif opcion == 'S':
            break

