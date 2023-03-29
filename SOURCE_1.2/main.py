# encoding=utf8
from __future__ import unicode_literals
import os
import os.path
os.environ["KIVY_NO_CONSOLELOG"] = "1"
import sys
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar
from py.BootScreen import BootScreen
from py.ContestScreen import ContestScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.audio import SoundLoader
import py.uselesscoconut as uc
from kivy.config import Config
from kivy.uix.screenmanager import NoTransition
from kivy.core.window import Window

Window.minimum_height = 650
Window.minimum_width = 960

class MainAPP(MDApp):
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.list_screen = {
            BootScreen: ("BootScreen", uc.langDict["mainMenu_Title"][uc.langSelect]),  
            ContestScreen: ("ContestScreen", uc.langDict["questions_Title"][uc.langSelect])
}

    def build(self,dt=1):   
        self.title = uc.langDict["downloadingQuestions_String"][uc.langSelect]
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"
        try:
            self.root = Builder.load_file(os.path.join(sys._MEIPASS, "kv\\screenManager.kv"))
        except:
            self.root = Builder.load_file("kv\\screenManager.kv")

    def on_start(self):
        for screen, details in self.list_screen.items():
            screen_id,text = details
            try:
                Builder.load_file(os.path.join(sys._MEIPASS, f"kv\\{screen_id}.kv"))
            except:
                Builder.load_file(f"kv\\{screen_id}.kv")
            self.root.ids.screen_manager.add_widget(screen(name=screen_id))
            Window.size = (960, 650)


    def change_screen(self, screen_id):
        self.root.ids.screen_manager.transition = NoTransition()
        self.root.ids.screen_manager.current = screen_id



if __name__ == "__main__":
    MainAPP().run()
