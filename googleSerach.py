import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia

# Initialize speech recognition and text-to-speech engines
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # it takes microphone input from the user and returns string output
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        speak("Listening")
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("say that again please")
        return "None"

def searchgoogle(query):
    speak("this is what i found on google")
    query = query.replace("google", "")
    query = query.replace("search", "")
    try:
        pywhatkit.search(query)
        print(wikipedia.summary(query,2))
        speak(wikipedia.summary(query, 2))
    except:
        speak("sorry i am unable to find this on google")

def searchyoutube(query):
    speak("this is what i found on youtube")
    query = query.replace("youtube", "")
    query = query.replace("search", "")
    try:
        pywhatkit.playonyt(query)
        
    except:
        speak("sorry i am unable to find this on youtube")

def wikipediasearch(query):
    speak("this is what i found on wikipedia")
    query = query.replace("wikipedia", "")
    query = query.replace("search", "")
    try:
        speak("According to wikipedia:")
        speak(wikipedia.summary(query, 2))
        print(wikipedia.summary(query, 2))
    except:
        speak("sorry i am unable to find this on wikipedia")
