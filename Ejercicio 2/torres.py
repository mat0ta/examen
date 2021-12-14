import random
import time

class JuegoTorres():
    def __init__(self):
        self.cuadros = []
        self.torres1 = 0
        self.torres2 = 0
        self.asignacion = 0

    def crearCuadros(self):
        for i in range(3):
            self.cuadros.append(([' ']*3))


    def printearCuadros(self):
        for j in range(3):
            print(self.cuadros[j])
    
    def crearFichas(self):
           while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            while fichas_1 < 3 and self.asignacion == 0:
                if self.cuadros[x][y] == ' ':
                    self.cuadros[x][y] = '♜'
                    fichas_1 = fichas_1 + 1
                elif self.cuadros[x][y] == '♜':
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
            self.asignacion = 1
            while fichas_2 < 3 and self.asignacion == 1:
                if self.cuadros[x][y] == ' ':
                    self.cuadros[x][y] = '♖'
                    fichas_2 = fichas_2 + 1
                elif self.cuadros[x][y] == '♖' or self.cuadros[x][y] == '♜':
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
            self.asignacion = 2
            return