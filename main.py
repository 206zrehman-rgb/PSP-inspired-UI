from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition, SlideTransition
from music import Music
from clock import digitalClock
from pictures import Pictures
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import json


class startScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self.on_key_down)
    
        with open("data.json", "r") as f:
            jsonBackground = json.load(f)

        jsonBackground1 = jsonBackground["bgName"]

        with self.canvas.before:
            self.ids.startbg.source = jsonBackground1
    
    def on_key_down(self, window, key, scancode, codepoint, modifier):
        if key == 32:  # space
            self.Toggle_Home()
    

    def Toggle_Home(self):
        self.manager.current = "home"



class clockscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        

        self.clock = digitalClock()
        self.add_widget(self.clock)
    
    def clock_bg(self):
        with open("data.json", "r") as f:
            jsonBackground = json.load(f)

        jsonBackground1 = jsonBackground["bgName"]

        with self.canvas.before:
            self.ids.clockbg.source = jsonBackground1

    def on_pre_enter(self):
        self.clock_bg()


class home(Screen):

    box1_bg_color = ListProperty([0, 0, 1, 1])
    box2_bg_color = ListProperty([0, 0, 1, 1])
    box3_bg_color = ListProperty([0, 0, 1, 1])
    box4_bg_color = ListProperty([0, 0, 1, 1])

    bg_color = ListProperty([0,0,1,1])



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self.on_key_down)
        self.boxID = 0
        self.customiseWidgets = 0

        with open("data.json", "r") as f:
            jsonBackground = json.load(f)

        jsonBackground1 = jsonBackground["bgName"]

        with self.canvas.before:
            self.ids.bg.source = jsonBackground1

        
        self.music = Music()
        self.pictures = Pictures()
        self.clock = digitalClock()


    #background/ customisation section
        self.layout = BoxLayout(orientation="horizontal", pos_hint={'center_x': .3, 'center_y':.55}, size_hint=(.8,.12))
        self.layout2 = BoxLayout(orientation="horizontal", pos_hint={'center_x': .3, 'center_y':.40}, size_hint=(.8,.12))
        self.layout3 = BoxLayout(orientation="horizontal", pos_hint={'center_x': .3, 'center_y':.25}, size_hint=(.8,.12))
        self.instructionLabel = Label(text="mouse click for button use", pos_hint={'center_x': .8, 'center_y':.9})

        # wallpaper 1
        if not self.layout.parent:
            
            option1 = Label(text="background 1", color=(42,97,161,1),font_size=40,font_name="Roboto-Bold.ttf")
            self.layout.add_widget(option1)
            button1 = Button(text="select")
            button1.bind(on_press=self.background)
            self.layout.add_widget(button1)

        # wallpaper 2
        if not self.layout2.parent:

            option2 = Label(text="background 2", color=(42,97,161,1), font_size=40,font_name="Roboto-Bold.ttf")
            self.layout2.add_widget(option2)

            button2 = Button(text="select")
            button2.bind(on_press=self.background2)
            self.layout2.add_widget(button2)

        #wallpaper 3
        if not self.layout3.parent:

            option3 = Label(text="background 3", color=(42,97,161,1), font_size=40,font_name="Roboto-Bold.ttf")
            self.layout3.add_widget(option3)
            button3 = Button(text="select")
            button3.bind(on_press=self.background3)
            self.layout3.add_widget(button3)
    

    #saving background choice to json
    def background(self, *args):
        with self.canvas.before:
            self.ids.bg.source = 'images/bg1.JPG'
        self.bind(size=self.bg_size, pos= self.bg_size)
        background_data={
            "bgName" : self.ids.bg.source
        }

        with open("data.json", "w") as f:
            json.dump(background_data,f)

    #saving background choice to json
    def background2(self, *args):
        with self.canvas.before:
            self.ids.bg.source = 'images/bg2.jpg'
        self.bind(size=self.bg_size, pos=self.bg_size)
        
        background_data={
            "bgName" : self.ids.bg.source
        }

        with open("data.json", "w") as f:
            json.dump(background_data,f)

   #saving background choice to json
    def background3(self, *args):
        with self.canvas.before:
            self.ids.bg.source = 'images/bg3.gif'
        self.bind(size=self.bg_size, pos=self.bg_size)
        background_data={
            "bgName" : self.ids.bg.source
        }

        with open("data.json", "w") as f:
            json.dump(background_data,f)
        
    
    #ensuring the background works in screen resizing
    def bg_size(self, size, pos):
            self.ids.bg.size= self.size
            self.ids.bg.pos= self.pos
    
   



    # clock screen method
    def get_clock(self):
        self.manager.transition = SlideTransition(direction='down')
        self.manager.current = "clockscreen"
        

    #changing the color of the option tab
    def on_key_down(self, window, key, scancode, codepoint, modifier):
        if key == 276:  
            self.boxID = max(0, self.boxID - 1)
            self.Toggle_SubMenu()

        elif key == 275:  
            self.boxID = min(3, self.boxID + 1)
            self.Toggle_SubMenu()

            
        self.highlight_label()


    def highlight_label(self):
        self.ids.box1.color = (1,1,1,1)
        self.ids.box2.color = (1,1,1,1)
        self.ids.box3.color = (1,1,1,1)
        self.ids.box4.color = (1,1,1,1)
        if self.boxID == 0:
            self.box2_bg_color = (0, 0, 1, 1)
            self.box3_bg_color = (0, 0, 1, 1)
            self.box4_bg_color = (0, 0, 1, 1)

            self.ids.box1.color = (1,0,0,1)
            self.ids.box4.size_hint = [.1, .1]
            self.ids.box2.size_hint = [.1, .1]
            self.ids.box3.size_hint = [.1, .1]
            self.ids.box1.size_hint = [.11, .13]
            self.box1_bg_color = (161, 89, 126, 0.8)

        elif self.boxID== 1:
            self.box1_bg_color = (0, 0, 1, 1)
            self.box3_bg_color = (0, 0, 1, 1)
            self.box4_bg_color = (0, 0, 1, 1)
            self.ids.box2.color = (1,0,0,1)
            self.ids.box1.size_hint = [.1, .1]
            self.ids.box4.size_hint = [.1, .1]
            self.ids.box3.size_hint = [.1, .1]
            self.ids.box2.size_hint = [.11, .13]
            self.box2_bg_color = (161, 89, 126, 0.8)


        elif self.boxID== 2:

            self.box1_bg_color = (0, 0, 1, 1)
            self.box2_bg_color = (0, 0, 1, 1)
            self.box4_bg_color = (0, 0, 1, 1)

            self.box2_bg_color = (0, 0, 1, 1)

            self.ids.box3.color = (1,0,0,1)
            self.ids.box1.size_hint = [.1, .1]
            self.ids.box2.size_hint = [.1, .1]
            self.ids.box4.size_hint = [.1, .1]
            self.ids.box3.size_hint = [.11, .13]

            self.box3_bg_color = (161, 89, 126, 0.8)

        else:
            self.box1_bg_color = (0, 0, 1, 1)
            self.box2_bg_color = (0, 0, 1, 1)
            self.box3_bg_color = (0, 0, 1, 1)
            self.ids.box4.color = (1,0,0,1)
            self.ids.box1.size_hint = [.1, .1]
            self.ids.box2.size_hint = [.1, .1]
            self.ids.box3.size_hint = [.1, .1]
            self.ids.box4.size_hint = [.11, .13]
            self.box4_bg_color = (161, 89, 126, 0.8)

        
    #when a tab is selected a sub menu appears
    def Toggle_SubMenu(self):
        if self.boxID == 0:
            if self.layout:
                self.remove_widget(self.layout)
            if self.layout2:
                self.remove_widget(self.layout2)
            if self.layout3:
                self.remove_widget(self.layout3)
            if self.layout:
                self.remove_widget(self.instructionLabel)
            if self.music.parent:
                self.remove_widget(self.music)
            if self.pictures.parent:
                self.remove_widget(self.pictures)
            self.add_widget(self.pictures)
            

        if self.boxID == 1:
            if self.layout:
                self.remove_widget(self.layout)
            if self.layout2:
                self.remove_widget(self.layout2)
            if self.layout3:
                self.remove_widget(self.layout3)
            if self.layout:
                self.remove_widget(self.instructionLabel)
            if self.pictures.parent:
                self.remove_widget(self.pictures)
            if self.music.parent:
                self.remove_widget(self.music)
            self.add_widget(self.music)


        if self.boxID == 2:
            if self.layout:
                self.remove_widget(self.layout)
            if self.layout2:
                self.remove_widget(self.layout2)
            if self.layout3:
                self.remove_widget(self.layout3)
            if self.layout:
                self.remove_widget(self.instructionLabel)
            
            if self.pictures.parent:
                self.remove_widget(self.pictures)
            if self.music.parent:
                self.remove_widget(self.music)
     
            self.add_widget(self.layout)
            self.add_widget(self.layout2)
            self.add_widget(self.layout3)
            self.add_widget(self.instructionLabel)

        if self.boxID == 3:
            if self.layout:
                self.remove_widget(self.layout)
                self.x= 1
            if self.layout2:
                self.remove_widget(self.layout2)
            if self.layout3:
                self.remove_widget(self.layout3)
            if self.layout:
                self.remove_widget(self.instructionLabel)
            if self.music.parent:
                self.remove_widget(self.music)
            if self.pictures.parent:
                self.remove_widget(self.pictures)
            self.get_clock()
    
class MyMainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(startScreen(name="start"))
        sm.add_widget(home(name="home"))
        sm.add_widget(clockscreen(name="clockscreen"))
        sm.transition = SwapTransition()
        return sm

    
if __name__ == '__main__':
    MyMainApp().run()