class Colores:
    @staticmethod
    def obtener(color: str, lugar: str = 'fuente', extra: str = ''):
        colores = {
            'negro': 0,
            'rojo': 1,
            'verde': 2,
            'amarillo': 3,
            'azul': 4,
            'morado': 5,
            'cian': 6,
            'blanco': 7,
            None: 7,
        }
        lugares = {
            'fondo': 40,
            'fuente': 30,
            None: 30
        }
        extras = {
            'plano': 0,
            'negrita': 1,
            'subrayado': 4,
            '': 1,
            None: 1,
        }
        
        if color == 'default': return '\x1b[0m'

        try:
            extra = extras[extra]
            color = colores[color] + lugares[lugar]
            return f'\x1b[{extra};{color}m'
        except KeyError:
            return '\x1b[0m'

    def __getitem__(self, atributo):
        atributos = atributo.split(' ')
        color = lugar = extra = None

        if len(atributos) > 2: lugar, color, extra = atributos
        elif len(atributos) == 2: lugar, color = atributos
        else: color = atributos[0]

        return Colores.obtener(color, lugar, extra)

    def __getattribute__(self, atributo):
        return Colores.obtener(atributo)

colores = Colores()
