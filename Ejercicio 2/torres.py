import random
import time

class JuegoTorres():
    def __init__(self):
        self.cuadros = []
        self.torres1 = 0
        self.torres2 = 0
        self.asignacion = 0
        self.movimientos_1 = 0
        self.movimientos_2 = 0

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
            while self.torres1 < 3 and self.asignacion == 0:
                if self.cuadros[x][y] == ' ':
                    self.cuadros[x][y] = '♜'
                    self.torres1 = self.torres1 + 1
                elif self.cuadros[x][y] == '♜':
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
            self.asignacion = 1
            while self.torres2 < 3 and self.asignacion == 1:
                if self.cuadros[x][y] == ' ':
                    self.cuadros[x][y] = '♖'
                    self.torres2 = self.torres2 + 1
                elif self.cuadros[x][y] == '♖' or self.cuadros[x][y] == '♜':
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
            self.asignacion = 2
            return
    def jugador1(self):
            for x in range(0, 3):
                for y in range(0, 3):
                    global moved
                    moved = False
                    if self.cuadros[x][y] == '♜':
                        global xtemp
                        xtemp = x
                        xtemp = xtemp + 1
                        if xtemp < 3 and xtemp > -1 and self.cuadros[xtemp][y] == ' ':
                            self.cuadros[xtemp][y] = '♜'
                            self.cuadros[x][y] = ' '
                            print('Ficha movida de ' + str(x) + ',' +
                                str(y) + ' a ' + str(xtemp) + ',' + str(y))
                            self.movimientos_1 += 1
                            j.printearCuadros()
                            time.sleep(2)
                            break
                        else:
                            xtemp = x - 1
                            if xtemp < 3 and xtemp > -1 and self.cuadros[xtemp][y] == ' ':
                                self.cuadros[xtemp][y] = '♜'
                                self.cuadros[x][y] = ' '
                                print('Ficha movida de ' + str(x) + ',' +
                                    str(y) + ' a ' + str(xtemp) + ',' + str(y))
                                self.movimientos_1 += 1
                                j.printearCuadros()
                                time.sleep(2)
                                break
            return self.movimientos_1

    def jugador2(self):
            for x in range(0, 3):
                for y in range(0, 3):
                    global moved
                    moved = False
                    if self.cuadros[x][y] == '♖':
                        global xtemp
                        xtemp = x
                        xtemp = xtemp + 1
                        if xtemp < 3 and xtemp > -1 and self.cuadros[xtemp][y] == ' ':
                            self.cuadros[xtemp][y] = '♖'
                            self.cuadros[x][y] = ' '
                            print('Ficha movida de ' + str(x) + ',' +
                                str(y) + ' a ' + str(xtemp) + ',' + str(y))
                            self.movimientos_2 += 1
                            j.printearCuadros()
                            time.sleep(2)
                            break
                        else:
                            xtemp = x - 1
                            if xtemp < 3 and xtemp > -1 and self.cuadros[xtemp][y] == ' ':
                                self.cuadros[xtemp][y] = '♖'
                                self.cuadros[x][y] = ' '
                                print('Ficha movida de ' + str(x) + ',' +
                                    str(y) + ' a ' + str(xtemp) + ',' + str(y))
                                self.movimientos_2 += 1
                                j.printearCuadros()
                                time.sleep(2)
                                break
            return self.movimientos_2


j = JuegoTorres()
j.crearCuadros()
j.crearFichas()
j.printearCuadros()
moves = 0
empieza = random.randint(0, 1)
if empieza == 0:
    print('Empieza el jugador 1')
    while j.jugador1() > 0 and j.jugador2() > 0 and moves < 10:
        j.jugador1()
        time.sleep(1)
        j.jugador2()
        time.sleep(1)
        moves += 1
else:
    print('Empieza el jugador 2')
    while j.jugador1() > 0 and j.jugador2() > 0 and moves < 10:
        j.jugador2()
        time.sleep(2)
        j.jugador1()
        time.sleep(2)
        moves += 1