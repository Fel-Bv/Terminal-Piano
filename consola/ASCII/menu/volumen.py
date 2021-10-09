from consola.colores import colores
from consola.consola import consola

color = colores['fondo negro'] + colores.blanco
opciones = ['+', '-', 'S']
volumen = (
    # Columnas: 20
    # Filas: 5
    ' +------------------+ \n'
    ' |%s| \n'
    ' | [+]          [-] | \n'
    ' |          [S]alir | \n'
    ' +------------------+ \n'
)

def imprimir_menu_volumen(volumen_actual: int = 100, opcion: str = ''):
    opcion = opcion.upper()

    lineas = (consola.lineas - 6) // 2
    print('\n' * lineas, end='')

    menu = volumen % f'Volumen: {volumen_actual}'.center(18, ' ')
    if opcion in opciones:
        menu = menu.replace(
            f'[{opcion}]',
            f'{colores["fondo blanco"] + colores.negro}[{opcion}]{color}',
        )

    espacios_para_centrar = ' ' * ((consola.tamaño - 22) // 2)
    for linea in menu.split('\n'):
        print(espacios_para_centrar, end=color)
        print(linea + colores.default)

    print()
