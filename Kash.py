 #import part of program
import pyttsx3
import speech_recognition
import os
import datetime

#setting the audio base for the program
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

# audio=input("enter the line:")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

import speech_recognition

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        speak("Listening")
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source, 0, 4)
        try:
            print("Recognizing...")
            # speak("one minute sir.")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Say that again please...")
            speak("say that again please")
            return "None"
        return query
    
def alarm(query):
    timehere=open("alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__=="__main__":
    while True:
        query=takecommand().lower()
        if "wake up" in query:
            from greetMe import greetMe
            greetMe()

            while True:
                query=takecommand().lower()
                if "bye" in query:
                    speak("bye")
                    break
                elif "hello" in query:
                    speak("hello, how are you?")
                elif "play" in query:
                    speak("playing music")
                    os.system("start sample.mp3")
                elif "meaning" in query:
                    from Speaking_Dict import dict
                    dict()
                elif "date" in query:
                    time=datetime.datetime.now()
                    speak(time)
                elif "i am fine" in query:
                    speak("that's great ,sir!good to hear that")
                elif "how are you" in query:
                    speak("I am fine, sir. How can I help you today?")
                elif "open" in query:
                    speak("opening")
                    from openApp import openapp
                    openapp(query)
                elif "close" in query:
                    from openApp import closeapp
                    closeapp(query)
                elif "google" in query:
                    speak("searching on google")
                    from googleSerach import searchgoogle
                    searchgoogle(query)
                elif "wikipedia" in query:
                    speak("searching on wikipedia")
                    from googleSerach import wikipediasearch
                    wikipediasearch(query)
                elif "youtube" in query:
                    speak("opening youtube")
                    from googleSerach import searchyoutube
                    searchyoutube(query)
                elif "temperature" in query:
                    speak("checking temperature")
                    from googleSerach import searchgoogle
                    searchgoogle(query)
                elif "is the time" in query:
                    time = datetime.datetime.now().strftime("%H:%M")
                    hour=int(datetime.datetime.now().hour)
                    if hour>=0 and hour<=12:
                        b="Morning"
                    elif hour>12 and hour<=18:
                        b="noon"
                    else:
                        b="Noon"
                    result=f"Hello!sir,the time is {time} in the {b}"
                    print(result)
                    speak("Hello!sir,the time is" + time + "in the" +b)
        else:
            speak("Turning off the engine")
            break