# Examen Fundamentos de Programación
 
---

Este repositorio corresponde al Exámen de la asignatura de Programación.

El link para el repositorio es el siguiente: [Examen](https://github.com/mat0ta/examen/)

El link de mi perfil de GitHub es el siguiente: [mat0ta](https://github.com/mat0ta/)

---

En la carpeta [Ejercicio 1](https://github.com/mat0ta/examen/tree/main/Ejercicio%201) se puede encontrar el archivo [minion_game.py](https://github.com/mat0ta/examen/blob/main/Ejercicio%201/minion_game.py) el cual corresponde a la primera actividad del Examen.

El código empleado para dicha actividad es el siguiente:

```
import random
import time

class minion_game():
    def __init__(self) -> None:
        self.string = 'BANANA'
        self.puntuacion_1 = 0
        self.string_1 = ' '
        self.strings_1 = []
        self.puntuacion_2 = 0
        self.string_2 = ' '
        self.strings_2 = []
    def checkLetra(self, letra):
        if letra[:1].lower() in ('a', 'e', 'i', 'o', 'u'):
            return True
        else:
            return False
    def stuart(self):
        start = 0
        num = 1
        while True:
            if not m.checkLetra(self.string[start:num]):
                self.string_1 = self.string[start:num]
                if self.string_1 not in self.strings_1:
                    self.string_1 = self.string[start:num]
                    self.strings_1.append(self.string_1)
                    if self.string_1 != '':
                        self.puntuacion_1 += self.string.count(self.string_1)
                    print(self.string.count(self.string_1), self.string_1, self.puntuacion_1)
                    if self.puntuacion_1 == 12:
                        print(m.kevin())
                        return print('Stuard ha conseguido ' + str(self.puntuacion_1) + ' puntos.')
            num += 1
            if self.string_1.upper() == self.string:
                start += 1
                while m.checkLetra(self.string[start:]):
                    start += 1
                num = start
    
    def kevin(self):
        start2 = 1
        num2 = 2
        while True:
            if m.checkLetra(self.string[start2:num2]):
                self.string_2 = self.string[start2:num2]
                if self.string_2 not in self.strings_1:
                    self.string_2 = self.string[start2:num2]
                    self.strings_2.append(self.string_1)
                    if self.string_2 != '':
                        self.puntuacion_2 += self.string.count(self.string_2)
                    print(self.string.count(self.string_2), self.string_2, self.puntuacion_2)
                    if self.puntuacion_2 == 9:
                        if self.puntuacion_1 > self.puntuacion_2:
                            print('¡El ganador es Stuard!')
                        else:
                            print('¡El ganador es Kevin!')
                        return print('Kevin ha conseguido ' + str(self.puntuacion_2) + ' puntos.')
            num2 += 1
            if self.string_2.upper() == self.string:
                start2 += 1
                while not m.checkLetra(self.string[start2:]):
                    start2 += 1
                num2 = start2


m = minion_game()
print(m.stuart())
```

---

A continuación encontramos la carpeta [Ejercicio 2](https://github.com/mat0ta/examen/tree/main/Ejercicio%202) se puede encontrar el archivo [torres.py](https://github.com/mat0ta/examen/blob/main/Ejercicio%202/torres.py) el cual corresponde a la segunda actividad del Examen.

El código empleado para dicha actividad es el siguiente:

```
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
```
