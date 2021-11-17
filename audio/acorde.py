import numpy as np
from notas import *

def hacer_acorde(notas: list, nota_por_segundo: int = 44100) -> np.array:
    frecuencia = obtener_frecuencia_nota(notas[0]['nota'])
    acorde = obtener_nota(
        frecuencia,
        60 / notas[0]['bpm'] * notas[0]['duracion'],
        nota_por_segundo
    )

    for nota in notas[1:]:
        frecuencia = obtener_frecuencia_nota(nota['nota'])
        nota = obtener_nota(
            frecuencia,
            60 / nota['bpm'] * nota['duracion'],
            nota_por_segundo
        )
        acorde += nota

    return acorde
