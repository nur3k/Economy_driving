from . import light
from . import car


def test_overspeed():
    tmpclass = light.Light(10, 40, (1200, 120), 'Zachodnia')
    tmpcar = car.MyCar(30)
    assert tmpcar.speed_kmh >= 60


def test_calc_speed_needed():
    tmpclass = light.Light(10, 40, (1200, 120), 'Zachodnia')
    #tmpcar = Car.MyCar(30)
    tmpclass.calculate_speed_needed(300, 60)


def test_calculate_distance_to_light():
    tmpclass = light.Light(10, 40, (1200, 120), 'Zachodnia')
    tmpclass.calculate_distance_to_light(30)
    tmpclass.print_remaining_time()


def test_pass_lights():
    tmpclass = light.Light(10, 40, (1200, 120), 'Zachodnia')
    tmpcar = car.MyCar(1150)
    tmpcar.pass_lights(tmpclass)
