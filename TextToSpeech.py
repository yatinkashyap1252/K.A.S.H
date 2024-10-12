from gtts import gTTS
import os
# from gtts.lang import tts_langs

# print(tts_langs())   #helps to get the list of all languages supported by it
sentence=input("Enter the text:")
#lang-en,es(spanish),fr(french)
audio = gTTS(text=sentence, lang='es', slow=False)

audio.save("sample.mp3")  #welcome wil be the file name which is save and contain text voice

os.system("start sample.mp3")  #this will help to direct open the audio file