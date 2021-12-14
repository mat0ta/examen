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
    # def stuart(self):
    #     start = 0
    #     while True:
    #         if self.string_1.upper() == self.string:
    #             return self.puntuacion_1
    #         else:
    #             num = int(random.randint(0, len(self.string_1)))
    #             if not m.checkLetra(self.string[start:(num+1)]):
    #                 self.string_1 = self.string[start:(num+1)]
    #                 if self.string_1 not in self.strings_1:
    #                     self.string_1 = self.string[start:(num+1)]
    #                     self.strings_1.append(self.string_1)
    #                     self.puntuacion_1 += self.string.count(self.string_1)
    #                     print(self.string.count(self.string_1), self.string_1, self.puntuacion_1)
    def stuart(self):
        start = 0
        end = 1
        while True:
            if not m.checkLetra(self.string[start:end]):
                print(self.string[start:end])
                if end < len(self.string):
                    end += 1
                else:
                    start += 1
            else:
                return


m = minion_game()
print(m.stuart())