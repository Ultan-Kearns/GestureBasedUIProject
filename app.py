from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
class MainMenu(GridLayout):
    def __init__(self,**kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 1
        self. rows = 4
        self.add_widget(Label(text= "WELCOME TO SIMON! - THIS GAME WILL TEST YOUR MEMORY"))
        self.add_widget(Button(text='Start Game '))
        self.add_widget(Button(text='Options'))
        self.add_widget(Button(text='Quit Game'))

class Menu(App):
    def build(self):
        return MainMenu();
if __name__ == '__main__':
    Menu().run()
