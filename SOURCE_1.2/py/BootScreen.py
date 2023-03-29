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
import io

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
        try:
            uc.storFolder = str(os.path.join(os.path.dirname(sys._MEIPASS),"pyg_data"))
        except:
            uc.storFolder = str(os.path.join(os.getcwd(),"pyg_data"))

        if uc.dlDone == False:
            print(uc.storFolder)
            uc.dlDone = True
            try:

                gitRootReq = urllib.request.Request(uc.gitRoot, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"})
                self.app.title = uc.langDict['loading_String'][uc.langSelect] + gitRootReq.selector.split('/')[-1]
                gitRootRes = urllib.request.urlopen(gitRootReq)
                self.gitRootdl = json.loads(gitRootRes.read())
                uc.gitRoot = self.gitRootdl[uc.gitRootDiscr]
                
                quindexReq = urllib.request.Request(f"{uc.gitRoot}/quindex.json", headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"})
                self.app.title = uc.langDict['loading_String'][uc.langSelect] + quindexReq.selector.split('/')[-1]
                quindexResponse = urllib.request.urlopen(quindexReq)
                self.quindex = json.loads(quindexResponse.read())
                
                if not os.path.exists(uc.storFolder):
                    os.mkdir(uc.storFolder)

                if os.path.exists(os.path.join(uc.storFolder, ".qdx")):
                    os.remove(os.path.join(uc.storFolder, ".qdx"))
                wget.download(f"{uc.gitRoot}/quindex.json", os.path.join(uc.storFolder, ".qdx"))
                
                for fil in self.quindex:
                    print("\n", fil, self.quindex[fil])
                    self.app.title = uc.langDict['loading_String'][uc.langSelect] + self.quindex[fil] + ".json"
                    try:
                        if os.path.exists(os.path.join(uc.storFolder, f"{self.quindex[fil]}.json")):
                            os.remove(os.path.join(uc.storFolder, f"{self.quindex[fil]}.json"))
                        wget.download(f"{uc.gitRoot}/{self.quindex[fil]}.json", os.path.join(uc.storFolder, f"{self.quindex[fil]}.json"))
                        self.ids.jlist.add_widget(OneLineListItem(text=f"{fil}", on_release= lambda x, item=self.quindex[fil]: self.startgame(item)))
                    except:
                        Snackbar(text=f"{uc.langDict['failToLoad_Snack'][uc.langSelect]}: {uc.gitRoot}/{self.quindex[fil]}.json").open()
                print("")
            except:
                try:
                    if not os.path.exists(uc.storFolder):
                        Snackbar(text=uc.langDict["failOnLoad_Snack"][uc.langSelect]).open()
                        self.ids.labeltextup.text = uc.langDict["failOnLoad_Label"][uc.langSelect]
                        self.ids.timerCheck.disabled = True
                        self.ids.timerText.disabled = True
                        Clock.schedule_interval(self.app.stop, 25)
                    else:

                        with io.open(os.path.join(f"{uc.storFolder}\\.qdx"), "r", encoding='utf8') as qdx_json:
                            self.qdxj = json.load(qdx_json)
                            qdx_json.close()

                        for file in self.qdxj:
                            print(file, "/",self.qdxj[file])
                            self.ids.jlist.add_widget(OneLineListItem(text=f"{file}", on_release= lambda x, item=self.qdxj[file]: self.startgame(item)))

                        Snackbar(text=uc.langDict["noInternet_Snack"][uc.langSelect]).open()
                except:
                    Snackbar(text=uc.langDict["failOnLoad_Snack"][uc.langSelect]).open()
                
                
                
        BootScreen.playBoot(self, True)
        self.app.title = uc.langDict["mainMenu_Title"][uc.langSelect]
        self.ids.hmk.hint_text = uc.langDict["questionCount_Selector"][uc.langSelect]
        self.ids.infobutton.text = uc.langDict["about_DiaTitle"][uc.langSelect]
        self.ids.labeltextup.text = uc.langDict["intro_Label"][uc.langSelect]

    def on_enter(self):
        pass
            
        

    def startgame(self, askMo):
        if self.ids.hmk.text != "":
            hmk_temp = abs(int(self.ids.hmk.text))
            if hmk_temp != 0:
                uc.howMany2Ask = abs(int(self.ids.hmk.text))
        uc.jFile = askMo
        uc.timerFlag = self.ids.timerCheck.active
        self.sound.stop()
        self.app.change_screen("ContestScreen")
    




    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title=uc.langDict["about_DiaTitle"][uc.langSelect],
                text=uc.langDict["about_DiaText"][uc.langSelect],
            buttons = [MDFlatButton(text=uc.langDict["about_DiaButton"][uc.langSelect], on_release=lambda x: webbrowser.open("https://video.twimg.com/ext_tw_video/1543723003439104001/pu/vid/1280x720/A2zprLn4d2Lk_dXs.mp4"))])
        self.dialog.open()