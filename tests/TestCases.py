import main
import pytest


def test_overspeed():
    tmpclass = main.Light(10, 40, (1200, 120), 'Zachodnia')
    tmpcar = main.MyCar(30)
    assert tmpcar.speed_kmh >= 60


def test_calc_speed_needed():
    tmpclass = main.Light(10, 40, (1200, 120), 'Zachodnia')
    tmpcar = main.MyCar(30)
    tmpclass.calculate_speed_needed(300, 60)
