from consola.colores import colores
from consola.consola import consola
from menu.registro import registros_actuales

color_default = colores.default + colores.negro

teclado_grande = (
    # Filas: 10
    #   C   C#  D  D#   E   F   F#  G  G#  A  A#   B
    '|    |   |  |   |    |    |   |  |   |  |   |    |    |   |  |   |    |    |   |  |   |  |   |    |\n'
    '|    |   |  |   |    |    |   |  |   |  |   |    |    |   |  |   |    |    |   |  |   |  |   |    |\n'
    '|    |   |  |   |    |    |   |  |   |  |   |    |    |   |  |   |    |    |   |  |   |  |   |    |\n'
    '|    | 2 |  | 3 |    |    | 5 |  | 6 |  | 7 |    |    | 9 |  | 0 |    |    | s |  | d |  | f |    |\n'
    '|    |___|  |___|    |    |___|  |___|  |___|    |    |___|  |___|    |    |___|  |___|  |___|    |\n'
    '|      |      |      |      |      |      |      |      |      |      |      |      |      |      |\n'
    '|      |      |      |      |      |      |      |      |      |      |      |      |      |      |\n'
    '|      |      |      |      |      |      |      |      |      |      |      |      |      |      |\n'
    '|  q   |  w   |  e   |  r   |  t   |  y   |  u   |  i   |  o   |  p   |  z   |  x   |  c   |  v   |\n'
    '|______|______|______|______|______|______|______|______|______|______|______|______|______|______|\n'
)
teclado_pequeño = (
    # Filas: 10
    #   C   C#  D  D#   E   F   F#  G  G#  A  A#   B
    '|    |   |  |   |    |    |   |  |   |  |   |    |\n'
    '|    |   |  |   |    |    |   |  |   |  |   |    |\n'
    '|    |   |  |   |    |    |   |  |   |  |   |    |\n'
    '|    | 2 |  | 3 |    |    | 5 |  | 6 |  | 7 |    |\n'
    '|    |___|  |___|    |    |___|  |___|  |___|    |\n'
    '|      |      |      |      |      |      |      |\n'
    '|      |      |      |      |      |      |      |\n'
    '|      |      |      |      |      |      |      |\n'
    '|  q   |  w   |  e   |  r   |  t   |  y   |  u   |\n'
    '|______|______|______|______|______|______|______|\n'
)

if len(teclado_grande[:teclado_grande.index('\n')]) < consola.tamaño:
    teclado = teclado_grande
else:
    teclado = teclado_pequeño

def obtener_teclas():
    return {
        'q': f'C{registros_actuales[0]}', '2': f'C#{registros_actuales[0]}',
        'w': f'D{registros_actuales[0]}', '3': f'D#{registros_actuales[0]}',
        'e': f'E{registros_actuales[0]}',
        'r': f'F{registros_actuales[0]}', '5': f'F#{registros_actuales[0]}',
        't': f'G{registros_actuales[0]}', '6': f'G#{registros_actuales[0]}',
        'y': f'A{registros_actuales[0]}', '7': f'A#{registros_actuales[0]}',
        'u': f'B{registros_actuales[0]}',
        'i': f'C{registros_actuales[1]}', '9': f'C#{registros_actuales[1]}',
        'o': f'D{registros_actuales[1]}', '0': f'D#{registros_actuales[1]}',
        'p': f'E{registros_actuales[1]}',
        'z': f'F{registros_actuales[1]}', 's': f'F#{registros_actuales[1]}',
        'x': f'G{registros_actuales[1]}', 'd': f'G#{registros_actuales[1]}',
        'c': f'A{registros_actuales[1]}', 'f': f'A#{registros_actuales[1]}',
        'v': f'B{registros_actuales[1]}',
    }

def imprimir_teclado():
    print(colores.negro)

    columnas_teclado = len(teclado[:teclado.index('\n')])
    espacios_para_centrar = ' ' * ((consola.tamaño - columnas_teclado) // 2) if columnas_teclado < consola.tamaño else ''
    espacios_definidos = False
    color_tecla = 'blanco'
    espacios = 0
    print(espacios_para_centrar, end='')
    for indice, caracter in enumerate(teclado):
        if caracter == '|':
            espacios_definidos = False
            print(colores['fondo blanco'] + colores.negro, caracter, sep='', end='')
            continue

        if caracter == '\n':
            print(color_default)
            print(espacios_para_centrar, end='')
            continue

        if not espacios_definidos:
            try:
                espacios = len(teclado[indice : indice + teclado[indice:].index('|')])
                espacios_definidos = True
            except ValueError: continue

        color_tecla = 'negro' if espacios == 3 else 'blanco'

        print(colores[f'fondo {color_tecla}'], caracter, end='', sep='')
    print()
