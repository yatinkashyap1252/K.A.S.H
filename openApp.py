import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandpromt": "cmd", "paint": "paint", "vscode": "code", "word": "word"}

def openapp(query):
    speak("Launching sir!")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("kash", "")
        query = query.replace(" ", "")
        query = query.replace("open", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak(f"opening {app}")
                os.system(f"start {dictapp[app]}")
                return
        speak("sorry i cant open that app")

def closeapp(query):
    speak("Closing sir!")
    if "tab" in query:
        num_tabs = 1
        if "one" in query or "1" in query:
            num_tabs = 1
        elif "two" in query or "2" in query:
            num_tabs = 2
        elif "three" in query or "3" in query:
            num_tabs = 3
        elif "four" in query or "4" in query:
            num_tabs = 4
        elif "five" in query or "5" in query:
            num_tabs = 5
        for _ in range(num_tabs):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("All tabs closed! sir")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak(f"closing {app}")
                try:
                    os.system(f"taskkill /im {dictapp[app]}.exe")
                except Exception as e:
                    speak(f"Error closing {app}: {str(e)}")
                return
        speak("sorry i cant close that app")