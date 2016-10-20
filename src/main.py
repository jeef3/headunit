import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class HeadunitWidget(Widget):
    time = ObjectProperty(None)
    date = ObjectProperty(None)

    def update(self, dt):
        self.time = time.strftime('%H:%M')
        self.date = time.strftime('%A, %d %B')


class HeadunitApp(App):
    def build(self):
        app = HeadunitWidget()
        Clock.schedule_interval(app.update, 1.0 / 60.0)
        return app

if __name__ == '__main__':
    HeadunitApp().run()

