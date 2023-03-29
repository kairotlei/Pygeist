# Importar librerías

from re import A
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineIconListItem
from kivy.core.audio import SoundLoader
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.clock import Clock
import random
import time
import os.path
import json
import io
import sys
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import py.uselesscoconut as uc

startTime = int(time.time())
toSkip = []
RED = 0.70,0.00,0.00,1
GREEN = 0.07,0.40,0.00,1
class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class ContestScreen(Screen):
    selectedQuestion = {}
    askCount = 0
    failCt = 0
    aue = True
    trueCt = 0
    canInteract = True
    runf = True
    autoFlag = False
    reason = ""
    def __init__(self, **kwargs):
        super().__init__()
        self.app = MDApp.get_running_app()
        
    def on_pre_enter(self, *args):
        try:
            try:
                with io.open(os.path.join(sys._MEIPASS, f"{uc.storFolder}\\{uc.jFile}.json"), "r", encoding='utf8') as file_json:
                    self.questions = json.load(file_json)
                    file_json.close()
            except:
                with io.open(f"{uc.storFolder}\\{uc.jFile}.json", "r", encoding='utf8') as file_json:
                    self.questions = json.load(file_json)
                    file_json.close()
        except:
            self.reason = uc.langDict["CS_coudlntLoadFile_String"][uc.langSelect]
            return


        self.app.title = uc.langDict["questions_Title"][uc.langSelect]
        try:
            self.bgm = os.path.join(sys._MEIPASS, "res\\zQuestLoop.ogg")
        except:
            self.bgm = "res\\zQuestLoop.ogg"
        
        try:
            self.fail1 = os.path.join(sys._MEIPASS, "res\\fail1.ogg")
        except:
            self.fail1 = "res\\fail1.ogg"
        
        try:
            self.fail2 = os.path.join(sys._MEIPASS, "res\\fail2.ogg")
        except:
            self.fail2 = "res\\fail2.ogg"
        
        try:
            self.fail3 = os.path.join(sys._MEIPASS, "res\\fail3.ogg")
        except:
            self.fail3 = "res\\fail3.ogg"
        
        try:
            self.good4 = os.path.join(sys._MEIPASS, "res\\good4.ogg")
        except:
            self.good4 = "res\\good4.ogg"
        
        random.shuffle(self.questions)
        ContestScreen.setManualText(self)
        self.autoFlag = False
        
    
    def on_enter(self):
        if self.reason != "":
            self.goStart(0, 1)
        #para futuros comandos
        try:
            ContestScreen.playBGMusic(self.bgm)
        except:
            pass
        if self.runf == True:
            Clock.schedule_interval(self.setProBar, 0.03)
            self.runf = False
        

    def setProBar(self, *args, **kwargs):
        if self.ids.proBar.value > 0 and self.aue == True and uc.timerFlag == True:
            self.ids.proBar.value = float(self.ids.proBar.value) - 0.25
        elif self.aue == True and uc.timerFlag == True:
            self.aue = False
            self.setAutoText()
        else:
            pass

    def playBGMusic(*args):
        #pass
        sound = SoundLoader.load(*args)
        sound.loop = True
        sound.play()
    
    def playFX(*args):
        #pass
        fxsound = SoundLoader.load(*args)
        fxsound.loop = False
        fxsound.play()


    def setAutoText(self,*args,**kwargs):
        self.canInteract = False
        self.fdList = {"a":self.ids.a, "b":self.ids.b, "c":self.ids.c, "d":self.ids.d}
        try:
            del self.fdList[self.ansList[4]]
        except:
            pass

        self.sc1 = Clock.schedule_once(self.setF1, 0.5)
        self.sc2 = Clock.schedule_once(self.setF2, 1.3)
        self.sc3 = Clock.schedule_once(self.setF3, 2.1)
        self.sc4 = Clock.schedule_once(self.setTr, 2.9)
        self.autoFlag = True

    def setF1(self,*args,**kwargs):
        if self.autoFlag == True:
            try:
                self.fdList[list(self.fdList)[0]].md_bg_color = RED
                ContestScreen.playFX(self.fail1)
            except:
                pass
    def setF2(self,*args,**kwargs):
        if self.autoFlag == True:
            try:
                self.fdList[list(self.fdList)[1]].md_bg_color = RED
                ContestScreen.playFX(self.fail2)
            except:
                pass
    def setF3(self,*args,**kwargs):
        if self.autoFlag == True:
            try:
                self.fdList[list(self.fdList)[2]].md_bg_color = RED
                ContestScreen.playFX(self.fail3)
            except:
                pass
    def setTr(self,*args,**kwargs):
        if self.autoFlag == True:
            try:
                self.ids[self.ansList[4]].md_bg_color = GREEN
                Clock.schedule_once(self.setManualText, 3)
                ContestScreen.playFX(self.good4)
                del self.fdList
            except:
                pass
    
    def setManualText(self,*args,**kw):
        self.aue = True
        try:
            if uc.timerFlag == True:
                self.ids.proBar.value = 100
            else:
                self.ids.proBar.value = 0
            
            if len(self.questions) < uc.howMany2Ask:
                totalQuestions = len(self.questions)
            else:
                totalQuestions = uc.howMany2Ask
            self.totalQuestions = totalQuestions
            self.selectedQuestion = self.questions[uc.asked]
            uc.asked = uc.asked + 1

            if uc.asked > totalQuestions:
                uc.asked = uc.asked - 1
                0/0

            self.ansList = ["", "", "", ""]
            self.ids.ask.text = self.selectedQuestion["question"]
            self.ansList = [self.selectedQuestion["a"], self.selectedQuestion["b"], self.selectedQuestion["c"], self.selectedQuestion["d"]]
            random.shuffle(self.ansList)
            index_int_2_ans_letter = ["a", "b", "c", "d"]
            self.ansList.append(index_int_2_ans_letter[self.ansList.index(self.selectedQuestion[self.selectedQuestion["ans"]])])

            self.ids.a.text = self.ansList[0]
            self.ids.b.text = self.ansList[1]
            self.ids.c.text = self.ansList[2]
            self.ids.d.text = self.ansList[3]

            PURPLE = 0.33,0.00,0.50,1
            self.ids.a.md_bg_color = PURPLE
            self.ids.b.md_bg_color = PURPLE
            self.ids.c.md_bg_color = PURPLE
            self.ids.d.md_bg_color = PURPLE
            self.canInteract = True
            self.ids.tbar.title = str(uc.langDict['questionCount_Upbar'][uc.langSelect].format(akd=uc.asked,ttq=totalQuestions))

        except Exception as exc:
            print(exc)
            self.goStart(self.trueCt, totalQuestions)
        



    def select(self, IDSL, SELECTION):
        #print(SELECTION)
        

        if self.canInteract == True:
            if SELECTION == self.selectedQuestion[self.selectedQuestion["ans"]]:
                ContestScreen.playFX(self.good4)
                #print("succ :", SELECTION)
                if IDSL == "a":
                    self.ids.a.md_bg_color = GREEN
                elif IDSL == "b":
                    self.ids.b.md_bg_color = GREEN
                elif IDSL == "c":
                    self.ids.c.md_bg_color = GREEN
                elif IDSL == "d":
                    self.ids.d.md_bg_color = GREEN
                self.canInteract = False
                self.trueCt = self.trueCt + 1
                
            else:
                #print("fail :", SELECTION)
                ContestScreen.playFX(self.fail1)
                if IDSL == "a":
                    self.ids.a.md_bg_color = RED
                elif IDSL == "b":
                    self.ids.b.md_bg_color = RED
                elif IDSL == "c":
                    self.ids.c.md_bg_color = RED
                elif IDSL == "d":
                    self.ids.d.md_bg_color = RED
                if self.ids.a.text == self.selectedQuestion[self.selectedQuestion["ans"]]:
                    self.ids.a.md_bg_color = GREEN
                elif self.ids.b.text == self.selectedQuestion[self.selectedQuestion["ans"]]:
                    self.ids.b.md_bg_color = GREEN
                elif self.ids.c.text == self.selectedQuestion[self.selectedQuestion["ans"]]:
                    self.ids.c.md_bg_color = GREEN
                elif self.ids.d.text == self.selectedQuestion[self.selectedQuestion["ans"]]:
                    self.ids.d.md_bg_color = GREEN
                self.failCt = self.failCt + 1
                self.canInteract = False

            Clock.schedule_once(self.setManualText, 3)
            self.aue = False


    def exit_app(self):
        exit()


    
    def show_alert_dialog(self, aciertos, total):
        uc.sessionGood = uc.sessionGood + aciertos
        uc.sessionTotal = uc.sessionTotal + uc.asked
        
        try:
            perc = int((uc.sessionGood / uc.sessionTotal) * 100)
        except:
            perc = 0


        try:
            ratioIs = round(float((aciertos/total)*10),2)
        except:
            ratioIs = 0.1

        if ratioIs < 5:
            mark =  uc.langDict["CS_youFailed_String"][uc.langSelect]
        else:
            mark =  uc.langDict["CS_youPassed_String"][uc.langSelect]
        

        if self.reason == "":
            self.dialog = MDDialog(
            title= uc.langDict["CS_results_DiaTitle"][uc.langSelect],
            text= uc.langDict["CS_results_DiaText"][uc.langSelect].format(aciertos=aciertos, total=total, ratioIs=ratioIs, mark=mark, sessionGood=uc.sessionGood, sessionTotal=uc.sessionTotal, perc=perc),
            buttons=[
                    MDFlatButton(
                        text= uc.langDict["CS_restart_DiaButton"][uc.langSelect],
                        on_press= self.closeView)])
        else:
            self.dialog = MDDialog(
            title= uc.langDict["CS_results_DiaTitle"][uc.langSelect],
            text=self.reason,
            buttons=[
                    MDFlatButton(
                        text= uc.langDict["CS_restart_DiaButton"][uc.langSelect],
                        on_press= self.closeView)])

        self.dialog.open()


    def closeView(self, *args, **kwargs):	
        self.dialog.dismiss()


    def goStart(self, *args, **kwargs):
        self.autoFlag = False
        try:
            self.sc1.cancel()
            self.sc2.cancel()
            self.sc3.cancel()
            self.sc4.cancel()
        except:
            pass
        self.show_alert_dialog(args[0], args[1])
        self.canInteract = True
        self.toSkip = []
        self.failCt, self.trueCt, self.totalQuestions, uc.asked, self.askCount = 0, 0, 0, 0, 0
        self.reason = ""
        self.ids.a.text = ""
        self.ids.b.text = ""
        self.ids.c.text = ""
        self.ids.d.text = ""
        self.ansList = ["", "", "", ""]
        self.ids.ask.text = ""
        self.selectedQuestion = ""
        self.fdList = {}
        self.app.change_screen("BootScreen")

        