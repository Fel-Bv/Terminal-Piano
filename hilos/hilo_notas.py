from audio.notas import reproducir_nota
from threading import Thread

class HiloReproducirNota(Thread):
    def __init__(self, group = None, target = None, name = None,
            args = (), kwargs = None,
            nota: str = 'C4', segundos: float = 1, volumen: int = 100, *,
            daemon = None
        ) -> None:
        super().__init__(
            group = group, target = target, daemon = daemon, name = name,
            args = args, kwargs = kwargs
        )

        self.segundos = segundos
        self.volumen = volumen
        self.nota = nota

    def run(self):
        reproducir_nota(self.nota, self.segundos, volumen=self.volumen)
