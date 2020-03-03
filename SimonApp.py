from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import sys
from kivy.lang import Builder
import sr
# Load kv file
Builder.load_file('simon.kv')

class MainMenu(Screen):
    #sr.voice_input()
    pass
class LevelMenu(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass
# Create a screen manager
sm = ScreenManager()
sm.add_widget(MainMenu(name='menu'))
sm.add_widget(LevelMenu(name='level'))
class MainApplication(App):
    def build(self):
        return sm
main = MainApplication()
if __name__ == '__main__':
    MainApplication().run()
