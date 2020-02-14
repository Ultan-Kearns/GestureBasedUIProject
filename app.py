from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import sys

import speech_recognition as sr


class MainMenu(GridLayout):
    def __init__(self,**kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 1
        self. rows = 4
        self.add_widget(Label(text= "WELCOME TO SIMON! - THIS GAME WILL TEST YOUR MEMORY"))
        self.startgame = (Button(text='Start Game'))
        self.startgame.bind(on_press=self.start);
        self.add_widget(self.startgame)
        self.options = (Button(text='Options'))
        self.options.bind(on_press=self.option)
        self.add_widget(self.options)
        self.endgame = (Button(text='Quit Game'))
        self.endgame.bind(on_press=self.exit)
        self.add_widget(self.endgame)
    def start(self,instance):
        print("This should start game")
    def option(self, instance):
        print("This should load option")
    def exit(self,instance):
        sys.exit()
class Menu(App):
    def build(self):
        return MainMenu();
if __name__ == '__main__':
    Menu().run()
