from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import numpy as np


class HongKongApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.spacing = 50
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.75)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.window.add_widget(Image(source = 'playing-cards.png'))
        

        self.buttonContainer = BoxLayout(orientation = 'vertical')
        self.buttonContainer.spacing = 10

        # adding the two buttons to the boxlayout
        self.buttonNewGame = Button(
                text="NEW GAME",
                size_hint = (1, 0.5),
                bold = True,
                background_color = np.array([59, 102, 193, 256])/256
                )
        self.buttonNewGame.bind(on_press=self.callback_newgame)
        self.buttonContainer.add_widget(self.buttonNewGame)

        self.buttonResume = Button(
                text="RESUME PREVIOUS GAME",
                size_hint = (1, 0.5),
                bold = True,
                background_color = np.array([59, 102, 193, 256])/256 
                )
        self.buttonContainer.add_widget(self.buttonResume)

        # adding the boxlayout to the gridlayout
        self.window.add_widget(self.buttonContainer)

        return self.window
    
    def callback_newgame(self, intance):
        pass


if __name__ == '__main__':
    HongKongApp().run()
