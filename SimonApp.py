from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
import sys
from kivy.lang import Builder

# Load kv file
Builder.load_file('simon.kv')

class MainMenu(BoxLayout):
    pass
    
class MainApplication(App):
    def build(self):
        return MainMenu()
        
if __name__ == '__main__':
    MainApplication().run()
