import random
import time

class JuegoTorres():
    def __init__(self):
        self.cuadros = []
        self.torres1 = 0
        self.torres2 = 0
        self.asignacion = 0

    def crearTablero(self):
        for i in range(3):
            self.cuadros.append(([' ']*3))


    def printearTablero(self):
        for j in range(3):
            print(self.cuadros[j])