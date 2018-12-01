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
        self.authorized_speed = 40

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

            while self.green_time > 0:
                self.light = 'green'
                self.green_time -= 1
                time.sleep(1)
                if self.green_time == 0:
                    self.red_time = self.red_s
