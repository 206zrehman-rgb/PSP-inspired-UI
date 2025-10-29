from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


class Pictures(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text="Above are images of what inspired this UI", pos_hint={'center_x': .5, 'center_y': .3}, font_size=50)
        self.add_widget(label)
        
        #add content to boxlayout
        self.layout = BoxLayout(orientation="horizontal", pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.9, .14))

        img1 = Image(source='images/psp.PNG', size_hint_x= .4)
        self.layout.add_widget(img1)

        img2 = Image(source='images/pspgo.jpeg', size_hint_x= .4)
        self.layout.add_widget(img2)

        img3 = Image(source='images/psvita.jpeg', size_hint_x= .4)
        self.layout.add_widget(img3)

        img4 = Image(source='images/ps3.jpeg', size_hint_x= .4)
        self.layout.add_widget(img4)  

        #add boxlayout to the screen when class is called
        self.add_widget(self.layout)

