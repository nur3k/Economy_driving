import car
import light
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


class Intro(GridLayout):
    def __init__(self, **kwargs):
        super(Intro, self).__init__(**kwargs)

    def show_position(self):
        print('Blyat') 


class TestApp(App):
    def build(self):
        Builder.load_file("intro.kv")
        return Intro()


if __name__ == '__main__':

    Trace = []
    BMW = car.MyCar(0)
    JP2 = light.Light(10, 5, (200, 30), 'Jp2')
    Trace.append(JP2)

    Smikolaja = light.Light(15, 10, (400, 30), "SM")
    Trace.append(Smikolaja)

    Trace[0].start()
    Trace[1].start()
    TestApp().run()

    #TestApp.show_time(Trace[0])
        #print('trace0', Trace[0].green_time, Trace[0].red_time)
        #print('trace1', Trace[1].green_time, Trace[1].red_time)
        #os.system('cls')

    #BMW.pass_lights(Trace[0])
    #BMW.pass_lights(Trace[1])




