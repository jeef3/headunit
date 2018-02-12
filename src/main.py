import time
import bluetooth

from kivy.app import App
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage
from kivy.network.urlrequest import UrlRequest
from kivy.metrics import dp
from kivy.uix.stacklayout import StackLayout

Window.size = (720, 480)

key = 'cbb50b1f23a2230b10ccf6a3d8504fb0'

class BtConnection(Widget):
    connected = ObjectProperty(None)


class TimeAndDate(Widget):
    time = ObjectProperty(None)
    date = ObjectProperty(None)
    greeting = StringProperty('صباح الخير')
    scale = NumericProperty(1)

    def update(self, dt):
        self.time = time.strftime('%H:%M')
        self.date = time.strftime('%A, %d %B %Y')


class HeadunitWidget(Widget):
    anim = 0
    greeting = StringProperty('صباح الخير')
    lang = StringProperty('ar')
    is_greeting_visible = BooleanProperty(False)

    def update(self, dt):
        self.time_and_date.update(dt)

    def toggle(self, dt):
        if (self.is_greeting_visible):
            self.hide_greeting()
            self.is_greeting_visible = False
        else:
            self.show_greeting()
            self.is_greeting_visible = True


    def hide_greeting(self):
        if (self.anim):
            self.anim.cancel(self.time_and_date)

        self.anim = Animation(scale=1, duration=0.3, t='in_out_cubic')
        self.anim &= Animation(y=0, duration=0.3, t='in_out_cubic')
        self.anim.start(self.time_and_date)

    def show_greeting(self):
        if (self.anim):
            self.anim.cancel(self.time_and_date)

        self.anim = Animation(scale=0.6, duration=0.3, t='in_out_cubic')
        self.anim &= Animation(y=dp(150), duration=0.3, t='in_out_cubic')
        self.anim.start(self.time_and_date)


class HeadunitApp(App):

    def build(self):
        app = HeadunitWidget()

        Clock.schedule_interval(app.update, 1.0 / 60.0)
        Clock.schedule_once(app.toggle)
        Clock.schedule_once(app.toggle, 10)

        return app


if __name__ == '__main__':
    HeadunitApp().run()
