import wavio as wav
import numpy as np

def grabar(archivo: str, audio: np.array, nota_por_segundo: int = 44100) -> bool:
    try:
        wav.write(archivo, audio, nota_por_segundo, sampwidth=2)
    except BaseException as error:
        print(error)

        return False

    return True