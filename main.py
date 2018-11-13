import time
import threading


class Light(threading.Thread):
    def __init__(self, green_s, red_s, position_x_y, lights_name):
        super(Light, self).__init__()
        self.green_s, self.red_s = green_s, red_s  # cycles in seconds
        self.position_x_y = position_x_y
        self.lights_name = lights_name
        self.light = 'red'
        self.green_time = 0
        self.red_time = self.red_s
        self.running = False
        self.is_light_passed = 1

    def run(self):
        self.running = True
        self.cycle_simulation()

    def cycle_simulation(self):
        while self.running:
            while self.red_time > 0:
                self.light = 'red'
                self.red_time -= 1
                time.sleep(1)
                if self.red_time == 0:
                    self.green_time = self.green_s
                #yield self.light, self.green_time, self.red_time

            while self.green_time > 0:
                self.light = 'green'
                self.green_time -= 1
                time.sleep(1)
                if self.green_time == 0:
                    self.red_time = self.red_s
                #yield self.light, self.green_time, self.red_time

    # def green_or_red(self):
    #     if self.light == 'green':
    #         return self.green_time, self.green_time
    #     if self.light == 'red':
    #         return self.red_time, self.red_time

    def print_remaining_time(self):
        if self.light == 'green':
            print('Light is:', self.light, '\n Time remaining:', self.green_time)
        else:
            print('Light is:', self.light, '\n Time remaining:', self.red_time)

    def calculate_speed_needed(self, distance_to_light, authorized_speed):
        try:
            if distance_to_light >= 0:
                speed_ms = int(distance_to_light / self.red_time)
                speed_km = int(distance_to_light / self.red_time * 3.6)
                print('\n If you want to go on green in {} \n'
                      'then yours speed should be: {} m/s = {} km/h'.
                      format(self.lights_name, speed_ms, speed_km))
                if speed_km > authorized_speed:
                    print('You have to overspeed to get on green. Dont hurry, yours speed:',
                          speed_km, '\n authorized_speed: ', authorized_speed)
            else:
                print('\n You passed the light')
                self.is_light_passed = 0

        except ZeroDivisionError:
            print('\n You passed the light')
            self.is_light_passed = 0

    def calculate_distance_to_light(self, position_x):
        distance = self.position_x_y[0] - position_x
        return distance


class MyCar:
    def __init__(self, position_x):
        self.position_x = position_x
        self.speed_kmh = 60

    def get_gps_position(self):
        # symulacja zmiany pozycji x, trzeba bedzie dodać zczytywanie z GPSa
        self.position_x += 30
        time.sleep(1)
        return self.position_x

    def get_speed_position(self):
        return self.speed_kmh

    def show_position(self):
        self.position_x = self.get_gps_position()
        return self.position_x


if __name__ == '__main__':

    BMW = MyCar(10)
    JP2 = Light(10, 5, (2000, 30), 'Jp2')
    JP2.start()

    Smikolaja = Light(15, 10, (300, 30), "SM")
    Smikolaja.start()

    while True:
        while JP2.is_light_passed != 0:
            try:
                JP2.calculate_speed_needed(
                    JP2.calculate_distance_to_light(
                        BMW.show_position()), BMW.get_speed_position())
                if JP2.is_light_passed == 0:
                    del JP2
                    break
            except NameError:
                pass

        while Smikolaja.is_light_passed != 0:
            Smikolaja.calculate_speed_needed(
                Smikolaja.calculate_distance_to_light(
                    BMW.show_position()), BMW.get_speed_position())
            if Smikolaja.is_light_passed == 0:
                del Smikolaja
                break
