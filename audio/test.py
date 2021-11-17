#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from grabar_archivo import grabar
from melodia import hacer_melodia
from acorde import hacer_acorde
from notas import obtener_audio_nota
import numpy as np

BPM = 120

def main() -> None:
    acorde = hacer_acorde([
        {
            'nota': 'A2',
            'bpm': BPM,
            'duracion': 1,
        },
        {
            'nota': 'C4',
            'bpm': BPM,
            'duracion': 1,
        },
        {
            'nota': 'E4',
            'bpm': BPM,
            'duracion': 1,
        },
    ])
    melodia = hacer_melodia([
        {
            'nota': 'C4',
            'bpm': BPM,
            'duracion': .75,
        },
        {
            'nota': 'E4',
            'bpm': BPM,
            'duracion': .25,
        },
    ])

    audio = obtener_audio_nota(acorde, volumen=75)
    audio = np.array(audio.tolist() + obtener_audio_nota(melodia, volumen=65).tolist())

    acorde = hacer_acorde([
        {
            'nota': 'D3',
            'bpm': BPM,
            'duracion': 1,
        },
        {
            'nota': 'F#4',
            'bpm': BPM,
            'duracion': 1,
        },
        {
            'nota': 'A4',
            'bpm': BPM,
            'duracion': 1,
        },
    ])
    melodia = hacer_melodia([
        {
            'nota': 'C4',
            'bpm': BPM,
            'duracion': .75,
        },
        {
            'nota': 'E4',
            'bpm': BPM,
            'duracion': .25,
        },
    ])

    audio = np.array(audio.tolist() + obtener_audio_nota(acorde, volumen=55).tolist())
    audio = np.array(audio.tolist() + obtener_audio_nota(melodia, volumen=45).tolist())

    grabar('test.wav', audio)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\b\b  \nSaliendo...')
