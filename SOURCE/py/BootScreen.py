# Importar librerías
import os
import sys
import glob
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.audio import SoundLoader
from kivymd.uix.list import OneLineListItem
import time
import py.uselesscoconut as uc
import wget
import urllib.request
import json
from kivy.clock import Clock
import webbrowser

class BootScreen(Screen):
    dialog = None
    def __init__(self, **kwargs):
        super().__init__()  
        self.app = MDApp.get_running_app()

    def playBoot(self, play, *args, **kwargs):
        #pass
        
        if play == True:
            try:
                self.sound = SoundLoader.load(os.path.join(sys._MEIPASS, "res\\zStart.ogg"))
            except:
                self.sound = SoundLoader.load("res\\zStart.ogg")
            self.sound.loop = False
            self.sound.play()
        else:
            self.sound.stop()
            self.sound.unload()


    def on_pre_enter(self):
        pass

    def on_enter(self):

        
        if uc.dlDone == False:
            uc.dlDone = True
            try:
                gitRootReq = urllib.request.Request(uc.gitRoot, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"})
                self.app.title = f"Cargando {gitRootReq.selector.split('/')[-1]}"
                gitRootRes = urllib.request.urlopen(gitRootReq)
                self.gitRootdl = json.loads(gitRootRes.read())
                uc.gitRoot = self.gitRootdl["pkyzzer"]
                
                quindexReq = urllib.request.Request(f"{uc.gitRoot}/quindex.json", headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"})
                self.app.title = f"Cargando {quindexReq.selector.split('/')[-1]}"
                quindexResponse = urllib.request.urlopen(quindexReq)
                self.quindex = json.loads(quindexResponse.read())
                
                for fil in self.quindex:
                    print("\n", fil, self.quindex[fil])
                    self.app.title = f"Cargando {self.quindex[fil]}.json"
                    try:
                        wget.download(f"{uc.gitRoot}/{self.quindex[fil]}.json", os.path.join(sys._MEIPASS, f"res\\qche\\{self.quindex[fil]}.json"))
                        self.ids.jlist.add_widget(OneLineListItem(text=f"{fil}", on_release= lambda x, item=self.quindex[fil]: self.startgame(item)))
                    except:
                        try:
                            wget.download(f"{uc.gitRoot}/{self.quindex[fil]}.json", f"res\\qche\\{self.quindex[fil]}.json")
                            self.ids.jlist.add_widget(OneLineListItem(text=f"{fil}", on_release= lambda x, item=self.quindex[fil]: self.startgame(item)))
                        except:
                            Snackbar(text=f"Error al cargar: {uc.gitRoot}/{self.quindex[fil]}.json").open()
                print("")
            except:
                try:
                    Snackbar(text=f"Error al cargar {quindexReq.full_url}").open()
                except:
                    Snackbar(text="Error de carga.").open()
                self.ids.labeltextmid.text = "Problema al descargar datos."
                self.ids.labeltextdn.text = "No se puede continuar. \n\n - Revisa la conexión a Internet \n - Permite el acceso a github.com y githubusercontent.com en caso de estar bloqueados."
                self.ids.timerCheck.disabled = True
                self.ids.timerText.disabled = True
                Clock.schedule_interval(self.app.stop, 25)
                
                
        BootScreen.playBoot(self, True)
        self.app.title = "Inicio"
            
        

    def startgame(self, askMo):
        uc.jFile = askMo
        uc.timerFlag = self.ids.timerCheck.active
        self.sound.stop()
        self.app.change_screen("ContestScreen")
    




    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Información software",
                text="""Originalmente creado para simular exámenes tipo test. Finalmente ha derivado en ser un clon NO OFICIAL de:
                
Inspirado en Zeitgeist, un trivia semanal temático de preguntas y respuestas.
Música compuesta por Vivid Muzik, extraída de los streams de Twitch.
Efectos de sonido extraídos de los streams de Twitch.
Interference, Zeitgeist  ©  2010-2023 Centrifuge Ltd.
Twitch: twitch.tv/interference

Escrito en Python3 con Visual Studio Code.

Otros softwares de terceros:
GitHub  ©  2008-2022 GitHub, Inc.
Kivy / KivyMD  ©  2010-2022 Andrés Rodríguez, Kivy Team and others.
PyInstaller  ©  2005-2022 Giovanni Bajo, PyInstaller Team.
Wget  ©  1996-2021 Free Software Foundation, Inc.

Agradecimientos a:
- Interference por el juego original.
- Martín por enseñar a crear GUIs para Python.
- Mi inmensa paciencia.

k.""",
            buttons = [MDFlatButton(text="Ver cuando empezó a ser \n un simulador de exámenes tipo test", on_release=lambda x: webbrowser.open("https://video.twimg.com/ext_tw_video/1543723003439104001/pu/vid/1280x720/A2zprLn4d2Lk_dXs.mp4"))])
        self.dialog.open()