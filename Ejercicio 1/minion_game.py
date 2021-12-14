import random
import time

class minion_game():
    def __init__(self) -> None:
        self.string = 'BANANA'
        self.puntuacion_1 = 0
        self.puntuacion_2 = 0
    def checkLetra(self, letra):
        if letra[:1].lower() in ('a', 'e', 'i', 'o', 'u'):
            return True
        else:
            return False

m = minion_game()
print(m.checkLetra('qacoakwnwan'))