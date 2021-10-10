from consola.colores import colores
from consola.consola import consola

color = colores['fondo negro'] + colores.blanco
opciones = ['J', 'L', 'S']
octava = (
    # Columnas: 22
    # Filas: 8
    ' +--------------------+ \n'
    ' |       Octavas      | \n'
    ' |                    | \n'
    ' | [1][2][3][4][5][6] | \n'
    ' |                    | \n'
    ' | [J] <-      -> [L] | \n'
    ' |           [S]salir | \n'
    ' +--------------------+ \n'
)

def imprimir_menu_octavas(octavas_actuales: tuple = (4, 5), opcion: str = ''):
    opcion = opcion.upper()

    lineas = (consola.lineas - 9) // 2
    print('\n' * lineas, end='')

    menu = octava
    for octava_ in [1, 2, 3, 4, 5, 6]:
        if not octava_ in octavas_actuales:
            menu = menu.replace(
                f'[{octava_}]',
                f'{colores.negro}[{octava_}]{color}',
            )

    if opcion in opciones:
        menu = menu.replace(
            f'[{opcion}]',
            f'{colores["fondo blanco"] + colores.negro}[{opcion}]{color}',
        )

    espacios_para_centrar = ' ' * ((consola.tamaño - 24) // 2)
    for linea in menu.split('\n'):
        print(espacios_para_centrar, end=color)
        print(linea + colores.default)

    print()
