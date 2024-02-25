import sys
import time as time
import requests
from bs4 import BeautifulSoup
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
            audio = r.listen(source, timeout=2,phrase_time_limit=8)

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
        cmd = input("Enter the Command: ")
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
    try:
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
        pygame.init()
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
        print(translation.text)
        return translation.text
    except:
        print("Some Error")

def get_current_temperature(city):
    try:
        api_key = 'b55d9a0a22028f7880c8e3c052e0c3c6' 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        print(temperature)
        return temperature
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"

def search_wikipedia(question_type, topic):
    wikipedia.set_lang("en") 
    try:
        if question_type == 'what':
            result = wikipedia.summary(topic, sentences=2)
        elif question_type == 'who':
            result = wikipedia.summary(topic, sentences=1)
        elif question_type == 'how':
            search_query = f"How {topic}"
            result = wikipedia.summary(search_query, sentences=2)
        print(result)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        result = f"Please provide more specific information. Ambiguous term: {e}"
        print(result)
        return result


def thecmdrushe():
    while True:
        main_cmd = listening_cmd()
        main_input = main_cmd.lower()
        keywords = ["wake up", "rush", "rushee", "hey rush", "hello rush", "hey rushee", "hello rushee"]
        cmd_to_start = any(keyword in main_input for keyword in keywords)
        #cmd to get the access of Rushe
        if   cmd_to_start:
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
                    break
                
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
                    openPath = ("C:\\Users\\default\\Videos")
                    newpath = openPath.replace('default',userName)
                    os.startfile(newpath) 
                elif "document folder" in secondary_cmd or "document path"  in secondary_cmd:
                    try:
                        openPath = ("C:\\Users\\default\\Documents")
                        newpath = openPath.replace('default',userName)
                        os.startfile(newpath) 
                    except:
                        openPath = ("C:\\Users\\default\\OneDrive\\Documents")
                        newpath = openPath.replace('default',userName)
                        os.startfile(newpath) 
                elif "music folder" in secondary_cmd or "music path"  in secondary_cmd:
                    openPath = ("C:\\Users\\default\\Music")
                    newpath = openPath.replace('default',userName)
                    os.startfile(newpath) 
              
                #wikipeida 
                elif ( "who" or "what" or "how" in secondary_cmd ) and ('search'  in secondary_cmd or'wikipedia' in secondary_cmd) :
                    set_questiontype = ''
                    if "who" in secondary_cmd:
                        set_questiontype = 'who'
                    elif "what" in secondary_cmd:
                        set_questiontype = 'what'
                    elif "how" in secondary_cmd:
                        set_questiontype = "how"
                    topic = secondary_cmd.replace(" in wikipedia", ' ') 
                    topic = secondary_cmd.replace('search', ' ')
                    talk(search_wikipedia(set_questiontype, topic))
              
                #translate
                elif "translate" in secondary_cmd :
                    remove_the_translate_words = secondary_cmd.replace("translate",' ')
                    print("Which Language you want change")
                    talk("Which Language you want change")
                    which_lang = listening_cmd().lower()
                    translate_voice(remove_the_translate_words,which_lang)

                # close app
                elif "close" in secondary_cmd.lower():
                    talk("ok, closeing ")
                    place = secondary_cmd.replace('close',' ').replace('browser',' ').replace(' ','')
                    print(place)
                    close_app(place)

                # open apps
                elif "open" in secondary_cmd.lower():
                    talk("opening")
                    place = secondary_cmd.replace('open',' ').replace('browser',' ').replace(' ','')
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
                    break
                    
                elif "what is current temperature in" in secondary_cmd.lower():
                    city = secondary_cmd.replace("what is current temperature in", ' ').lower()
                    talk(f"Current Temperature in {city} {get_current_temperature(city)}")


             

if __name__ == "__main__":
    wish()
    talk("welcome sir , I am rushe your assistant ")
    thecmdrushe()

#this is testing line
