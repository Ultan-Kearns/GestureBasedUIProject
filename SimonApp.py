import os
os.environ['KIVY_MODULES_DIR'] = 'sr'
from kivy.app import App
from kivy.clock import Clock
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
    pass
class LevelMenu(Screen):
    pass
class DifficultyMenu(Screen):
    pass
class CreditsMenu(Screen):
    pass
class GameMenu(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass
# Create a screen manager - docs reference https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
# Need to add voice commands for each button - we can do this by returning value from sr script and have conditional statements

sm = ScreenManager()
sm.add_widget(MainMenu(name='mainmenu'))
sm.add_widget(GameMenu(name='game'))
sm.add_widget(LevelMenu(name='level'))
sm.add_widget(DifficultyMenu(name='difficulty'))
sm.add_widget(CreditsMenu(name='credits'))
def VoiceControls(dx):
    while(1):
        # can perform game events in here such as switching windows and game commands
        voiceCommand = sr.voice_input()
        while(not voiceCommand):
            voiceCommand = sr.voice_input()
        #include options for switching game menus in here may separate into functions
        if("quit" in voiceCommand or "exit" in voiceCommand or "close" in voiceCommand):
            sys.exit()
        else:
            #if user tries saying something that is not in commands
            print("Not a command valid commands are: ")
            voiceCommand = sr.voice_input()

Clock.schedule_once(VoiceControls, 1)
class MainApplication(App):
    def build(self):
        return sm
if __name__ == '__main__':
    MainApplication().run()
    #will need sr to run in paralell with gui
