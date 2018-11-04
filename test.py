import sys
import datetime
import logging
import time

green_s = list(range(0, 20))+list(range(30, 40))+list(range(50, 60))
red_s = list(range(20, 30))+list(range(40, 50))


cycles = {
    'green': green_s,
    'red': red_s
}


def green_or_red(cycle):
    if datetime.datetime.today().second in cycle['green']:
        light = 'green'
        remained_time = calculate_remaining_time(cycle['green'])
    else:
        light = 'red'
        remained_time = calculate_remaining_time(cycle['red'])
    return light, remained_time


lista = [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]


def calculate_remaining_time(lista):
    if datetime.datetime.today().second in lista:
        start = lista.index(datetime.datetime.today().second)
    else:


    # for i in lista:
    #     if lista.index(datetime.datetime.today().second) in lista:
    #         if datetime.datetime.today().second+1 != i+1:
    #             tmp = i
    #
    # remaining_time = tmp - datetime.datetime.today().second
    print(start)
    return start


while True:
    print(green_or_red(cycles), datetime.datetime.today().second )
