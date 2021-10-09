from consola.colores import colores
from consola.consola import consola

opciones = ['V', 'R', 'S']
texto_opciones = consola.centrar_texto('[V]: Volúmen  [R]: Registro  [S]: Salir')
color = colores['fondo blanco'] + colores.negro
menu = (
    color +
    consola.centrar_texto('Menú (Mayúsculas)') +
    texto_opciones +
    colores.default
)

def imprimir_menu(opcion_seleccionada: str = '') -> None:
    if opcion_seleccionada:
        opcion_seleccionada = opcion_seleccionada.upper()

        if not opcion_seleccionada in opciones: return

        print(menu.replace(
            texto_opciones,
            texto_opciones.replace(
                f'[{opcion_seleccionada}]',
                f'{colores["fondo negro"] + colores.blanco}[{opcion_seleccionada}]{color}'
            )
        ))
        return
    print(menu)
