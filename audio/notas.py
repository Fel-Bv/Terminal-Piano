#!/usr/bin/env python3

import simpleaudio as sa
import numpy as np

def obtener_frecuencia_nota(nota: str) -> float:
    notas = [
        'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1',
        'G1', 'G#1', 'A1', 'A#1', 'B1',
        'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2',
        'G2', 'G#2', 'A2', 'A#2', 'B2',
        'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3',
        'G3', 'G#3', 'A3', 'A#3', 'B3',
        'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4',
        'G4', 'G#4', 'A4', 'A#4', 'B4',
        'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5',
        'G5', 'G#5', 'A5', 'A#5', 'B5',
        'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6',
        'G6', 'G#6', 'A6', 'A#6', 'B6',
    ]
    notas = {
        notas[i]: round(440 * 1.059463094359 ** (-45 + i), 5)
            for i in range(len(notas))
    }
    frecuencia = 0

    if len(nota) == 1:
        nota += '4'

    if not frecuencia:
        frecuencia = notas[nota]

    return frecuencia

def obtener_nota(frecuencia: float, segundos: float, nota_por_segundo: int):
    tupla = np.linspace(0, segundos, round(segundos * nota_por_segundo), False)
    # Genera una onda sinusoidal con la frecuencia de la nota:
    return np.sin(frecuencia * tupla * 2 * np.pi)

def obtener_audio_nota(nota, volumen: int = 100):
    audio = nota * (2 ** (volumen / 100 * 15) - 1) / np.max(np.abs(nota))
    # Convierte a 16-bit:
    audio = audio.astype(np.int16)

    return audio

def reproducir_audio(audio, nota_por_segundo: int) -> None:
    play_obj = sa.play_buffer(audio, 1, 2, nota_por_segundo)
    play_obj.wait_done()

def reproducir_nota(nota: str, segundos: float, nota_por_segundo: int = 44100, volumen: int = 100):
    frecuencia = obtener_frecuencia_nota(nota.strip().upper())
    nota = obtener_nota(frecuencia, segundos, nota_por_segundo)
    audio = obtener_audio_nota(nota, volumen)

    reproducir_audio(audio, nota_por_segundo)

def main(segundos: float = 1, nota_por_segundo: int = 44100) -> None:
    notas = input('Nota(s) (Si son varias notas, escribelas separadas por coma): ').strip().split(',')

    for nota in notas:
        reproducir_nota(nota, segundos, nota_por_segundo)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
