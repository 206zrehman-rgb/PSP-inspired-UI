import time
from kivy.clock import Clock
from kivy.uix.label import Label

class digitalClock(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 200  
        self.color = (42,97,161,1)
        self.update()
        Clock.schedule_interval(self.update, 1) #update every second
     
    #get the time in hours, minutes and seconds
    def update(self, *args):
        self.text = time.strftime("%H:%M:%S")

