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