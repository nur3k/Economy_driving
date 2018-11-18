import car
import light
from kivy.app import App


class TestApp(App):
    def build(self):
        return 0


if __name__ == '__main__':

    Trace = []
    BMW = car.MyCar(0)
    JP2 = light.Light(10, 5, (200, 30), 'Jp2')
    Trace.append(JP2)

    Smikolaja = light.Light(15, 10, (300, 30), "SM")
    Trace.append(Smikolaja)

    Trace[0].start()
    Trace[1].start()
    TestApp().run()





