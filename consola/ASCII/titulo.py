from consola.colores import colores
from consola.consola import consola

titulo = (
    colores['fondo blanco'] +
    colores.negro +
    consola.centrar_texto('- Piano -') +
    colores.default
)

def imprimir_titulo():
    print(titulo)
