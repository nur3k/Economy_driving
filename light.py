import time
import threading


class Light(threading.Thread):
    def __init__(self, green_s, red_s, position_x_y_tuple, lights_name):
        super(Light, self).__init__()
        self.green_s, self.red_s = green_s, red_s  # cycles in seconds
        self.position_x_y = position_x_y_tuple
        self.lights_name = lights_name
        self.light = 'red'
        self.green_time = self.green_s
        self.red_time = 0
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
                speed_ms = int(distance_to_light / self.green_time)
                speed_km = int(distance_to_light / self.green_time * 3.6)
                print('\n If you want to go on green at {} crossroad\n'
                      'then yours speed should be: {} m/s = {} km/h'.
                      format(self.lights_name, speed_ms, speed_km))
                print('Dist to light:', distance_to_light,
                      'Remained time:', self.green_time)
                if speed_km > authorized_speed:
                    print("You have to overspeed to get on green. Dont hurry."
                          "\n Authorized_speed: ", authorized_speed)
            else:
                print('\n You passed the light')
                self.is_light_passed = 0
        except ZeroDivisionError:
            print('Red light on:', self.lights_name, self.red_time)

    def calculate_distance_to_light(self, position_x):
        distance = self.position_x_y[0] - position_x
        return distance
