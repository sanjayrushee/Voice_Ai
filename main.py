import sys
import time
import pywhatkit
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os 
import subprocess as sp
import pyjokes
import ctypes
import wikipedia
from gtts import gTTS
import pygame
from io import BytesIO
from googletrans import Translator
from getallapps import get_to_open
from close_the_app import close_app
from requirementschecking import mic_checking
from requirementschecking import get_user_name



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
list_of_apps_opend = []
r = sr.Recognizer()
userName = get_user_name()



def talk(talk):
    engine.say(talk)
    engine.runAndWait()


def listening_cmd():
    if mic_checking():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=2, phrase_time_limit=5)

        try:
            print("Recognizing...")
            cmd = r.recognize_google(audio, language='en-in')
            print(f"You said: {cmd}\n")


        except Exception as e:
            print("Speech recognition could not understand audio")
            return "none"

        return cmd
    else:
        print("Microphone is not connected")
        cmd = input("Enter cmdand: ")
        return cmd



def wish():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
    elif hour >= 18 and hour < 20:
        print("Good Evening!")
    elif hour >= 20 and hour < 24:
        print("Good Night!")
    else:
        print("Good Night!")

def translate_voice(inputText,which_lang):
    select_language = {
    "english": "en",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "italian": "it",
    "portuguese": "pt",
    "russian": "ru",
    "chinese (Simplified)": "zh-CN",
    "japanese": "ja",
    "korean": "ko",
    "arabic": "ar",
    "hindi": "hi",
    "bengali": "bn",
    "tamil": "ta",
    "telugu": "te",
    "urdu": "ur" }
    get_target_language = select_language[which_lang]
    translator = Translator()
    translation = translator.translate(inputText, dest=get_target_language)
    pygame.mixer.init()
    tts = gTTS(text=translation.text, lang=get_target_language, slow=False)
    speech_bytes = BytesIO()
    tts.write_to_fp(speech_bytes)
    speech_bytes.seek(0)
    pygame.mixer.music.load(speech_bytes)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()
    return translation.text


def thecmdrushe():
    while True:
        main_cmd = listening_cmd()
        main_cmd = main_cmd.lower()
        cmd_to_start = ["wake up", "rush", "rushee",'hey rush',"hello rush","hey rushee","hello rushee"]
        Search_keyWoards = ["wikipedia",'what is meant by','tell me about' ,'who the heck is']
        #cmd to get the access of Rushe
        if   main_cmd in cmd_to_start:
            talk("i am ready sir , please tell me what can i do for you. ")
            while True:
                secondary_cmd = listening_cmd()
                secondary_cmd = secondary_cmd.lower()
                
                # playing song in youtube
                if "play" in secondary_cmd:
                    music = secondary_cmd.replace('play', '')
                    print(music)
                    talk("playing")
                    pywhatkit.playonyt(music)
                
                #getting worst jokes     
                elif "some joke" in secondary_cmd:
                    jk = pyjokes.get_joke()
                    print(jk)
                    talk(jk)
                
                #Open the default folders in windows
                elif "open download" in secondary_cmd or "open download folder" in secondary_cmd:
                    openPath = ("C:\\Users\\default\\Downloads")   
                    newpath = openPath.replace('default',userName)
                    os.startfile(newpath)
                elif "video folder" in secondary_cmd or "video path"  in secondary_cmd:
                    os.startfile("C:\\Users\\default\\Video")
                    newpath = openPath.replace('default',userName)
                    os.startfile(newpath) 
                elif "document folder" in secondary_cmd or "document path"  in secondary_cmd:
                    os.startfile("C:\\Users\\default\\Documents")
                    newpath = openPath.replace('default',userName)
                    os.startfile(newpath) 
                elif "music folder" in secondary_cmd or "music path"  in secondary_cmd:
                    os.startfile("C:\\Users\\default\\Music")
                    newpath = openPath.replace('default',userName)
                    os.startfile(newpath) 
                elif "picture folder" in secondary_cmd or "picture path"  in secondary_cmd:
                    os.startfile("C:\\Users\\default\\Pictures")
                    newpath = openPath.replace('default',userName)
                    os.startfile(newpath) 
                
                #translate
                elif "translate" in secondary_cmd :
                    remove_the_translate_words = secondary_cmd.replace("translate",' ')
                    which_lang = listening_cmd().lower()
                    translate_voice(remove_the_translate_words,which_lang)

                # close app
                elif "close " in secondary_cmd.lower():
                    talk("ok")
                    place = secondary_cmd.replace('close','')
                    place = place.lstrip()
                    print(place)
                    close_app(place)

                # open apps
                elif "open " in secondary_cmd.lower():
                    talk("opening")
                    place = secondary_cmd.replace('open','')
                    place = place.lstrip()
                    print(place)
                    get_to_open(place)
                
                #asking time
                elif "time now" in secondary_cmd.lower():
                    time = datetime.datetime.now().strftime('%I %M %p')
                    print(time)
                    talk("The current time is" + time)
                
                #asking loacation 
                elif "where is" in secondary_cmd:
                    location = secondary_cmd.replace("where is", "")
                    talk("searching" + location)
                    webbrowser.open("https://www.google.com/maps/place/" + location)

                elif "go to study" in secondary_cmd.lower() or "study mode" in secondary_cmd.lower():
                    # talk("which one you want sir")
                    webbrowser.open("https://swayam.gov.in/") # need to develope 

               #rushee sleep and exit
                elif "see you later" in secondary_cmd.lower():
                    talk("see you later , sir ")
                    exit()
                elif "go to sleep" in secondary_cmd:
                    talk("Call me when you need")
                    break
                
                #system poweroff and others
                elif "power off " in secondary_cmd.lower() or "shut down" in secondary_cmd.lower():
                    talk("Your system will be power off in few seconds")
                    os.system("shutdown /s /t 7")
                    os.system('taskkill /F /IM *')
                    sys.exit()

                elif "restart my pc" in secondary_cmd.lower() or "restart my computer" in secondary_cmd.lower():
                    talk("your system will be Restart in few seconds ")
                    os.system("shutdown /r /t  1")
                    time.sleep(1)
                    sys.exit()

                elif "lock my pc" in secondary_cmd.lower() or "lock my computer" in secondary_cmd.lower():
                    talk("ok")
                    ctypes.windll.user32.LockWorkStation()

                #createing notepad
                elif "notepad" in secondary_cmd.lower() or "Notepad " in secondary_cmd:
                    notepad = "notepad.exe"
                    filename = "file.txt"
                    sp.Popen([notepad, filename])
                    
                elif "what is temperature" in secondary_cmd.lower():
                    pass

             

if __name__ == "__main__":
    wish()
    talk("welcome sir , I am rushe your assistant ")
    thecmdrushe()

#this is testing line
