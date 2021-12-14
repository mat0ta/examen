import random
import time

cuadros = []
torres1 = 0
torres2 = 0
asignacion = 0

def crearTablero():
    for i in range(3):
        cuadros.append(([' ']*3))


def printearTablero():
    for j in range(3):
        print(cuadros[j])