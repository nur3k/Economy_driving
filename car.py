import time


class MyCar:
    def __init__(self, position_x):
        self.position_x = position_x
        self.speed_kmh = 60

    def get_gps_position(self):
        # symulacja zmiany pozycji x, trzeba bedzie dodać zczytywanie z GPSa
        self.position_x += 10
        time.sleep(1)
        return self.position_x

    def get_speed_position(self):
        return self.speed_kmh

    def show_position(self):
        self.position_x = self.get_gps_position()
        return self.position_x

    def pass_lights(self, light_obj):
        try:
            while light_obj.is_light_passed != 0:
                self.calculate_speed_needed(light_obj)
                if light_obj.is_light_passed == 0:
                    del light_obj
        except NameError:
            pass

    def calculate_speed_needed(self, light_obj):
        try:
            distance_to_light = self.calculate_distance_to_light(light_obj)
            if distance_to_light >= 0:
                speed_ms = int(distance_to_light / light_obj.green_time)
                speed_km = int(distance_to_light / light_obj.green_time * 3.6)
                print('\n If you want to go on green at {} crossroad\n'
                      'then yours speed should be: {} m/s = {} km/h'.
                      format(light_obj.lights_name, speed_ms, speed_km))
                print('Dist to light:', distance_to_light,
                      'Remained time:', light_obj.green_time)
                if speed_km > light_obj.authorized_speed:
                    print("You have to overspeed to get on green. Dont hurry."
                          "\n Authorized_speed: ", light_obj.authorized_speed)
            else:
                print('\n You passed the light')
                light_obj.is_light_passed = 0
        except ZeroDivisionError:
            print('Red light on:', light_obj.lights_name, light_obj.red_time)

    def calculate_distance_to_light(self, light_obj):
        distance = light_obj.position_x_y[0] - self.show_position()
        return distance
