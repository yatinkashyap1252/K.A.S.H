import pyttsx3
import datetime
import os

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extracttime=open("alarmtext.txt","rt")
time=extracttime.read()
Time=str(time)
extracttime.close()

