import sys
import datetime
import logging
import time
import threading
from multiprocessing import Process
import multiprocessing


class Light(object):
    def __init__(self, green_s, red_s, position_x, position_y, lights_name):
        # cycles
        self.light = 'red'
        self.green_s = green_s  # green cycle in seconds
        self.red_s = red_s  # red cycle in seconds
        self.position_x, self.position_y = position_x, position_y
        self.lights_name = lights_name
        self.green_time = 0
        self.red_time = self.red_s
        # thread = threading.Thread(target=self.cycle_simulation)
        # thread.daemon = True
        # thread.start()
        #Process(target=self.cycle_simulation()).start()
        multiprocessing.Process(target=self.cycle_simulation).start()

    def cycle_simulation(self):
        print('aaa3')
        while True:
            while self.red_time > 0:
                print('aaa2')
                self.light = 'red'
                self.red_time -= 1
                time.sleep(1)
                print('aaa222')
                if self.red_time == 0:
                    self.green_time = self.green_s
                return self.light, self.green_time, self.red_time
            while self.green_time > 0:
                self.light = 'green'
                self.green_time -= 1
                time.sleep(1)
                if self.green_time == 0:
                    self.red_time = self.red_s
                print('aaa1')
                return self.light, self.green_time, self.red_time
            print('aaa655')

    def green_or_red(self):
        if self.light == 'green':
            return self.green_time, self.red_time
        if self.light == 'red':
            return self.red_time, self.green_time

    def print_remaining_time(self):
        print('Light is:', self.green_or_red()[0], 'On distance [m]:',
              self.position_x, 'Remained time [s]:', self.green_or_red()[1])

    def calculate_speed_needed(self, distance_to_light):
        speed_ms = int(distance_to_light / self.green_or_red())
        speed_km = int(distance_to_light / self.green_or_red() * 3.6)
        print('\n If you want to go on green in {} \n'
              'then yours speed should be: {} m/s = {} km/h'.format(self.lights_name, speed_ms, speed_km))

    def calculate_distance_to_light(self, position_x):
        distance = self.position_x - position_x
        return distance


class MyCar:
    def __init__(self, position_x):
        self.position_x = position_x

    def get_gps_position(self):
        # symulacja zmiany pozycji x, trzeba bedzie dodać zczytywanie z GPSa
        self.position_x += 1
        time.sleep(1)
        return self.position_x

    def show_position(self):
        self.position_x = self.get_gps_position()
        return self.position_x



#SMMikolaja = Light(15, 10, (40, 50), "SM")

if __name__ == '__main__':
#     #JP2.calculate_speed_needed(JP2.calculate_distance_to_light(BMW.show_position()))
#     #SMMikolaja.calculate_speed_needed(SMMikolaja.calculate_distance_to_light(BMW.show_position()))

    JP2 = Light(40, 10, 10, 10, 'Jp2')
    while True:

    # p1 = multiprocessing.Process(target=JP2)
    # #p2 = multiprocessing.Process(target=JP2.cycle_simulation)
    # p1.start()

