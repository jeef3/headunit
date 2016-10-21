import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window

class HeadunitWidget(Widget):
    time = ObjectProperty(None)
    date = ObjectProperty(None)
    screen_resolution = StringProperty('');

    def update(self, dt):
        self.time = time.strftime('%H:%M')
        self.date = time.strftime('%A, %d %B')
        self.screen_resolution = 'Screen: ' + str(Window.size)


class HeadunitApp(App):
    def build(self):
        app = HeadunitWidget()
        Clock.schedule_interval(app.update, 1.0 / 60.0)
        return app

if __name__ == '__main__':
    HeadunitApp().run()

