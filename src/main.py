import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest

key = ''

class HeadunitWidget(Widget):
    time = ObjectProperty(None)
    date = ObjectProperty(None)
    screen_resolution = StringProperty('')
    temp = StringProperty('')

    def update(self, dt):
        self.time = time.strftime('%H:%M')
        self.date = time.strftime('%A, %d %B')
        self.screen_resolution = 'Screen: ' + str(Window.size)

    def got_weather(self, request, data):
        self.temp = str(data['main']['temp'])


class HeadunitApp(App):

    def build(self):
        app = HeadunitWidget()

        # url = 'http://api.openweathermap.org/data/2.5/weather?id=2192362&units=metric&appid=' + key
        # req = UrlRequest(url, on_success=app.got_weather)

        Clock.schedule_interval(app.update, 1.0 / 60.0)
        return app


if __name__ == '__main__':
    HeadunitApp().run()
