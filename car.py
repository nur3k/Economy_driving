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

    def pass_lights(self, evidence):
        try:
            while evidence.is_light_passed != 0:
                evidence.calculate_speed_needed(
                    evidence.calculate_distance_to_light(
                        self.show_position()), self.get_speed_position())
                if evidence.is_light_passed == 0:
                    del evidence
        except NameError:
            pass
