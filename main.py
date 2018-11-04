import sys
import datetime
import logging
import time


class Light:
    def __init__(self, green_s, red_s, position_tuple, lights_name):
        # cycles
        self.light = 'red'
        self.green_s = green_s  # green cycle in seconds
        self.red_s = red_s  # red cycle in seconds
        self.position_x, self.position_y = position_tuple
        self.count_time = 0  # second when cycle start
        self.remained_time = 1

        # nie ogarnia na razie całego cyklu
        self.cycles = {
            'green': green_s,
            'red': red_s
        }

        self.lights_name = lights_name

    def green_or_red(self):
        if datetime.datetime.today().second in self.cycles['green']:
            self.light = 'green'
            self.remained_time = self.calculate_remaining_time(self.cycles['green'])
        else:
            self.light = 'red'
            # czas wisany na sztywno (trzeba to wyliczyc)
            self.remained_time = self.calculate_remaining_time(self.cycles['red'])
        return self.light, self.remained_time

    def calculate_remaining_time(self, dict):
        remaining_time = 1
        return remaining_time

    def print_remaining_time(self):
        print('Light is:', self.green_or_red()[0], 'On distance [m]:',
              self.position_x, 'Remained time [s]:', self.green_or_red()[1])

    def calculate_speed_needed(self, distance_to_light):
        speed_ms = int(distance_to_light / self.remained_time)
        speed_km = int(distance_to_light / self.remained_time * 3.6)
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


# Def Car with position
BMW = MyCar(5)
JP2 = Light(list(range(0, 20)) + list(range(30, 40)) + list(range(50, 60)),
            list(range(20, 30)) + list(range(40, 50)), (40, 50), 'JP2')

SMMikolaja = Light(list(range(30, 40)),
                   list(range(0, 30)) + list(range(40, 60)), (40, 50), "SM")

while True:
    JP2.calculate_speed_needed(JP2.calculate_distance_to_light(BMW.show_position()))
    SMMikolaja.calculate_speed_needed(SMMikolaja.calculate_distance_to_light(BMW.show_position()))
