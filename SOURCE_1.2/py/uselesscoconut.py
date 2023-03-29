gameNo = 1
jFile = ""
jfiles = []
randomizerEnabled = True
asked = 0
gitRoot = "https://gist.githubusercontent.com/kairotlei/adf26da8bb9beb5a7628342fb612b42c/raw/"
gitRootDiscr = "pkyzzer"
gitDb = "hi"
dlDone = False
timerFlag = False
storFolder = ""
sessionGood = 0
sessionTotal = 0
howMany2Ask = 10

# 0 for Spanish, 1 for English
langSelect = 0



langDict = {
"mainMenu_Title":["Menú principal","Main menu"],

"questions_Title":["Preguntas","Questions"],

"downloadingQuestions_String":["Descargando preguntas...","Downloading questions..."],

"loading_String":["Cargando","Loading"],

"failToLoad_Snack":["Error al descargar.","Error on download."],

"failOnLoad_Snack":["Error de carga.","Error on load."],

"failOnLoad_Label":[
    "[size=20] No se puede continuar.[/size] \n\n [size=14]- Revisa la conexión a Internet. \n - Permite el acceso a [i]github.com[/i] y [i]githubusercontent.com[/i] en caso de estar bloqueados.[/size]",
    "[size=20] Sorry, can't continue.[/size] \n\n [size=14]- Check your internet connection. \n - Plase allow access to [i]github.com[/i] and [i]githubusercontent.com[/i] if blocked.[/size]"],

"noInternet_Snack":[
    "No hay internet - usando recursos descargados en última ejecución",
    "No Internet - using local resources from last execution"],

"about_DiaTitle":["Información software","About this software"],

"about_DiaText":[
"""Originalmente un clon de '¿Quién quiere ser millonario?' creado para simular exámenes tipo test.
                
Inspirado en Zeitgeist, un trivia semanal de Interference en Twitch.
Música compuesta por Vivid Muzik, extraída de los streams de Twitch.
Efectos de sonido extraídos de los streams de Twitch.
Interference, Zeitgeist  ©  2010-2023 Centrifuge Ltd.
Twitch: twitch.tv/interference

Escrito en Python3 y KivyMD con Visual Studio Code.

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
"""Originally a 'Who wants to be a millionaire?' clone created to simulate test exams.
                
Inspired on Zeitgeist, a weekly trivia on Twitch by Interference.
Original music Vivid Muzik, extracted from Twitch streams.
Sound effects extracted from Twitch streams.
Interference, Zeitgeist  ©  2010-2023 Centrifuge Ltd.
Twitch: twitch.tv/interference

Written in Python3 and KivyMD using Visual Studio Code.

Other 3rd party software:
GitHub  ©  2008-2022 GitHub, Inc.
Kivy / KivyMD  ©  2010-2022 Andrés Rodríguez, Kivy Team and others.
PyInstaller  ©  2005-2022 Giovanni Bajo, PyInstaller Team.
Wget  ©  1996-2021 Free Software Foundation, Inc.

Special thanks to:
- Interference by the original game.
- Martín by teaching GUIs creation for Python.
- My huge patience.

k."""],


"about_DiaButton":["Ver prototipo inicial","Look how this all started \n (first working prototype)"],
"questionCount_Upbar":[" Pregunta {akd} de {ttq}"," Question {akd} of {ttq}"],
"questionCount_Selector":["Nº preguntas (default: 10)","Question Nº. (default: 10)"],
"CS_coudlntLoadFile_String":["No se ha podido cargar el archivo de preguntas.","Couldn't load questions file."],
"CS_youFailed_String":["Suspendes, vuelve a intentarlo.","You failed, try again."],
"CS_youPassed_String":["Apruebas, enhorabuena!","You pass, congrats!"],
"CS_results_DiaTitle":["Resultados","Results"],

"CS_results_DiaText":[
    """Has acertado {aciertos} de {total} preguntas.
Tu nota sobre 10 es de {ratioIs}.
{mark}

En esta sesión llevas {sessionGood} preguntas buenas de {sessionTotal} ({perc}%)""",

    """You got {aciertos} out of {total} questions right.
Your mark out of 10 is {ratioIs}.
{mark}

On this session you got {sessionGood} correct answers out of {sessionTotal} ({perc}%)"""],
"CS_restart_DiaButton":["REINICIAR","RESTART"],
"intro_Label": ["[size=20]Pygeist[/size] \n  Inspirado en Zeitgeist de Interference \n", "[size=20]Pygeist[/size] \n  Inspired on Zeitgeist by Interference \n"]
}