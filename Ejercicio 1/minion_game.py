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
            num += 1
            if self.string_1.upper() == self.string:
                start += 1
                while m.checkLetra(self.string[start:]):
                    start += 1
                    print('Doner')
                print('Done', start)
                num = start


m = minion_game()
print(m.stuart())