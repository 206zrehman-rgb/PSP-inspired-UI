from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

class Music(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #save music files
        self.Sound = SoundLoader.load("music/itBegins.mp3")
        self.Sound2 = SoundLoader.load("music/track2.mp3")

        #gif specific for this sub menu
        gif = Image(
            source='images/music.gif',
            anim_delay = 0.05,
            allow_stretch=True,
            keep_ratio=False
            )
        
        self.add_widget(gif)

        #instructions on how to access the buttons
        instructionLabel = Label(text= "mouse click for button use", pos_hint={'center_x' : .8, 'center_y': .9})
        self.add_widget(instructionLabel)


        #first boxlayout for track 1
        self.layout = BoxLayout(orientation="horizontal", pos_hint={'center_x': .3, 'center_y': .5}, size_hint=(.8, .12))

        label = Label(text = "Track 1", size_hint_x = .4, color=(42,97,161,1), font_size=50,font_name="Roboto-Bold.ttf")
        self.layout.add_widget(label)

        playbtn1 = Button(text="play", size_hint_x=.3)
        #when button is pressed play function called
        playbtn1.bind(on_press=self.play_music)
        self.layout.add_widget(playbtn1)

        pausebtn1 = Button(text="pause", size_hint_x=.3)
        #when button pressed pause function called
        pausebtn1.bind(on_press=self.pause_music)
        self.layout.add_widget(pausebtn1)

        self.add_widget(self.layout)



        #second boxlayout for track 2
        self.layout2 = BoxLayout(orientation="horizontal", pos_hint={'center_x': .3, 'center_y': .3}, size_hint=(.8, .12))

        label2 = Label(text = "Track 2", size_hint_x = .4, color=(42,97,161,1),font_size=50,font_name="Roboto-Bold.ttf")
        self.layout2.add_widget(label2)

        playbtn2 = Button(text="play", size_hint_x=.3)
        #when button is pressed play function called
        playbtn2.bind(on_press=self.play_music2)
        self.layout2.add_widget(playbtn2)

        pausebtn2 = Button(text="pause", size_hint_x=.3)
        #when button pressed pause function called
        pausebtn2.bind(on_press=self.pause_music2)
        self.layout2.add_widget(pausebtn2)

        self.add_widget(self.layout2)



    #if called play music
    def play_music(self, instance):
        if self.Sound:
            self.Sound.play()
    
    #if called pause music
    def pause_music(self, instance):
        if self.Sound:
            self.Sound.stop()
    
    #if selected play music
    def play_music2(self, instance):
        if self.Sound2:
            self.Sound2.play()
            
    #if called pause music
    def pause_music2(self, instance):
        if self.Sound2:
            self.Sound2.stop()
