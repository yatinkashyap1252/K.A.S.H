import pyttsx3
from nltk.corpus import wordnet
import nltk
# nltk.download('wordnet')

class Speaking:

    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()


class dict:
    speaking=Speaking()
    speaking.speak("Enter the word")
    text=input("Enter the word:")
    synsets = wordnet.synsets(text)
    for synset in synsets:
        print(synset.definition())
        speaking.speak(synset.definition())

# class GFG:
#     def dictionary(self):       
#         speaking = Speaking()        
#         speaking.speak("Which word do you want to find the meaning, sir?")
#         query = str(input())
#         dictionary = PyDictionary()
#         word = dictionary.meaning(query)
#         # print(len(word))
#         # print(word)
#         """the below code is for synonyms and antonym just for some more feature!!!"""
#         # synonyms = dictionary.synonym(query)
#         # antonyms = dictionary.antonym(query)
#         # print(synonyms)
#         # print(antonyms)

#         #the 2 for loop is used bcz of speaking a single every meaning related to word which are mainly separated by comma
#         if word is not None:
#             for i in word:
#                 speaking.speak(f"The meaning of {query} is {i}")
#         else:
#             speaking.speak("Sorry sir, I am unable to find the meaning of this word")
        