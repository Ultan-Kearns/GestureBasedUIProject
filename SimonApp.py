from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
#https://docs.python.org/2/library/threading.html info about threading
from threading import Thread
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
sm.add_widget(DifficultyMenu(name='difficulty'))
sm.add_widget(CreditsMenu(name='credits'))
def GameLogic():
    #here we will define logic of the game and how it will function maybe get squares to light up
    print("IN game logic")
def GameControls():
    global sm
    #call thread to start game logic here
    while(1):
        # need someway to loop these but since call back is loop it'll break the app
        # maybe unschedule event then new event
        voiceCommand = sr.voice_input()
        while(not voiceCommand):
                voiceCommand = sr.voice_input()
        if("red" in voiceCommand.lower()):
            print("red")
        elif("blue" in voiceCommand.lower()):
            print("blue")
        elif("yellow" in voiceCommand.lower()):
            print("yellow")
        elif("green" in voiceCommand.lower()):
            print("green")
        elif("quit" in voiceCommand.lower() or "exit" in voiceCommand.lower() or "close" in voiceCommand.lower()):
            sm.current="mainmenu"
            #restart thread
            main = Thread(target=Main)
            main.setDaemon(True)
            main.start()
            break
        else:
            print("Could not understand command - valid commands are red,green,blue & yellow")
            voiceCommand = sr.voice_input()
    print("Exiting game")
# may add screen to ask user if they want to use voice commands
def Main():
    # can perform game events in here such as switching windows and game commands
    # infinite loop for voice commands may be issue
    while(1):
        voiceCommand = sr.voice_input()
        while(not voiceCommand):
            voiceCommand = sr.voice_input()
        #include options for switching game menus in here may separate into functions
        if("quit" in voiceCommand.lower() or "exit" in voiceCommand.lower() or "close" in voiceCommand.lower()):
            sys.exit()
            break
        elif("play" in voiceCommand.lower() or "start" in voiceCommand.lower() or "game" in voiceCommand.lower()):
            sm.current = 'game'
            #need to find way to stop threads
            game = Thread(target = GameControls)
            game.setDaemon(True)
            game.start()
            break
        elif("developers" in voiceCommand.lower() or "credits" in voiceCommand.lower()):
            sm.current = 'credits'
        elif('back' in voiceCommand.lower() or 'main menu' in voiceCommand.lower()):
            sm.current =  'mainmenu'
        elif('level' in voiceCommand.lower() or 'change' in voiceCommand.lower() or 'difficulty' in voiceCommand):
            sm.current =  'difficulty'
        else:
            #if user tries saying something that is not in commands
            print("Not a command valid commands are: ")
    print("Exiting main")
main = Thread(target=Main)
main.setDaemon(True)
main.start()
class MainApplication(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MainApplication().run()
    #will need sr to run in paralell with gui
