import threading
import time


class Auto:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)


class Swiatlo:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)


def aufasd(asd):
    asd.printname()


janusz = Auto('janusz')
kazimieerz = Swiatlo('kazimierz')

aufasd(kazimieerz)