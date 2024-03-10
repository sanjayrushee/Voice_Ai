'''import requests
#import folium
res=requests.get('https://ipinfo.io/')
data = res.json()
print(data)


def secondCmd():
    if sr.Microphone is True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            cmd = r.recognize_google(audio)
            print(f" you said : {cmd}\n")
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
    else:
        print("mic is not connect")
        cmd = input()
    return cmd
import time
import pyautogui
def close_all_software():
    # Wait for a short delay before starting
    time.sleep(2)
    # Simulate pressing the Alt+F4 keyboard shortcut multiple times
    for _ in range(10):
        pyautogui.hotkey('alt', 'f4')
        time.sleep(0.5)
close_all_software()
from close_the_app import close_app
from getallapps import  list_of_software
for i in list_of_software():
    close_app(i)
import os
import subprocess
# Get the running processes
process = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE)
output, _ = process.communicate()
# Parse the output to get process names
process_names = [line.split()[0].decode() for line in output.splitlines()[3:]]
# Terminate each process
for name in process_names:
    os.system(f"taskkill /F /IM {name}")
import os
os.startfile("C:\\Users\\fortever\\Downloads")
def tester():
    enter = input("fdfd: ")
    list_a = []
    i =0
    while i < 5:
        if enter == "1" :
            cmd = input()
            list_a.append(cmd)
        elif enter == 2:
            cmd = input("dfd")
            list_a.append(cmd)
        i = i+1
    return list_a
simple = tester()
import time
import pygetwindow as gw
import pyautogui
# Wait for Chrome window to be active
chrome_window = None
while not chrome_window:
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
    time.sleep(1)
# Bring Chrome window to the front
chrome_window.activate()
# Switch to the Instagram tab
pyautogui.hotkey('Ctrl', 'Tab')
time.sleep(0.5)  # Wait for the tab switch to complete

# Close the active tab
pyautogui.hotkey('Ctrl', 'w')
import pyaudio
# Initialize PyAudio
audio = pyaudio.PyAudio()

# Get the number of available audio devices
num_devices = audio.get_device_count()

# Check if any microphone device is found
is_microphone_connected = False
for i in range(num_devices):
    device_info = audio.get_device_info_by_index(i)
    if device_info["maxInputChannels"] > 0:
        is_microphone_connected = True
        break

# Print the microphone connection status
if is_microphone_connected:
    print("Microphone is connected.")
else:
    print("Microphone is not connected.")

# Terminate PyAudio
audio.terminate()

pywhatkit.sendwhatmsg("+919025328897",
					"Geeks For Geeks!",
					22, 59
                      )

import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)
    try:
        # Recognize speech using Google Speech Recognition with English (India) language
        text = recognizer.recognize_google(audio, language="en-IN")
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print("Error occurred: {0}".format(e))

import pywhatkit


pywhatkit.sendwhatmsg_instantly(
    phone_no="+91 90253 28897",
    message="Howdy! This message will be sent instantly!",
)

from collections import deque

# Declaring deque
while True:
    queue = deque(['name', 'age', 'DOB'])
    print(queue)
    enter = input()
    queue.append(enter)
    print(queue)

import time
import datetime
import pywhatkit as kit

class WhatsAppBot:
    def __init__(self):
        pass

    def take_Command(self):
        # Simulate taking command from user
        return input("Enter command: ")

    def talk(self, message):
        # Simulate speaking the message
        print(message)

    def SearchCont(self, command):
        # Simulate searching for contact
        # Return (name, numberID, F)
        return ("Rock Ravi", "+919025328897", True)

    def AddContact(self):
        # Simulate adding a new contact
        pass

    def whatsapp(self, command):
        try:
            command = command.replace('send a message to', '')
            command = command.strip()
            name, numberID, F = self.SearchCont(command)
            if F:
                print(numberID)
                self.talk(f'Boss, what message do you want to send to {name}')
                message = self.take_Command()
                hour = int(datetime.datetime.now().hour)
                min = int(datetime.datetime.now().minute)
                print(hour, min)
                if "group" in command:
                    time.sleep(10)  # Wait for 10 seconds before sending the message
                    kit.sendwhatmsg_to_group(numberID, message, int(hour), int(min) + 1)
                else:
                    time.sleep(10)  # Wait for 10 seconds before sending the message
                    kit.sendwhatmsg(numberID, message, int(hour), int(min) + 1)
                self.talk("Boss message have been sent")
            if not F:
                self.talk(f'Boss, the name not found in our data base, shall I add the contact')
                AddOrNot = self.take_Command()
                print(AddOrNot)
                if ("yes" in AddOrNot) or ("add" in AddOrNot) or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                    self.AddContact()
                elif "no" in AddOrNot:
                    self.talk('Ok Boss')
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    bot = WhatsAppBot()
    bot.whatsapp("send a message to Rock Ravi")


import wikipedia
secondary_cmd = input()
try:
    if ('wikipedia' in secondary_cmd):
        result = secondary_cmd.replace("wikipedia",' ')
    elif('what is meant by' in secondary_cmd):
        result = secondary_cmd.replace('what is meant by',' ')
    print("Give me a second")
    info = wikipedia.summary(result,3)
    print("According to wikipedia" + info)
except:
    pass

    
 elif "music" in secondary_cmd or "play some music " in secondary_cmd.lower():
                    song = os.listdir("E:\\Music\\Songs")  #replace your user path
                    os.startfile(os.path.join("E:\\Music\\Songs", song[5])) #replace your user path
                    break

    

from gtts import gTTS
import pygame
from io import BytesIO
from googletrans import Translator

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
    "urdu": "ur"
}


def translate_voice(inputText,get_target_language):
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

text_to_translate = input("Enter the text to translate: ")
remove_the_translate_words = text_to_translate.replace("translate this",' ') or text_to_translate.replace("translate",' ')
target_language = input("Enter the target language (e.g., 'fr' for French): ").lower()
get_target_language = select_language[target_language]

print(translate_voice(remove_the_translate_words,get_target_language))

import requests
from bs4 import BeautifulSoup



import requests

def get_current_temperature(city):
    try:
        api_key = 'b55d9a0a22028f7880c8e3c052e0c3c6'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    city = input("Enter city name: ")
    temperature = get_current_temperature(city)
    print(f"Current temperature in {city}: {temperature}°C")


import pygame
from googletrans import Translator
from gtts import gTTS
from io import BytesIO

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

secondary_cmd = input("enter the words :")
remove_the_translate_words = secondary_cmd.replace("translate",' ')
which_lang = input("Which Language you want change :")
translate_voice(remove_the_translate_words,which_lang)

import wikipedia

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
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Please provide more specific information. Ambiguous term: {e}")

if __name__ == "__main__":
    question_type = input("Enter your question type (what, who, how): ").lower()
    topic = input("Enter the topic: ")
    search_wikipedia(question_type, topic)


import tkinter as tk
from tkinter import font

class VoiceAssistantApp:
    def __init__(self, master):
        self.master = master
        master.title("Voice Assistant")

        # Create fonts
        self.heading_font = font.Font(family="Poppins", size=24, weight="bold")
        self.text_font = font.Font(family="Poppins", size=14)

        # Create container frame
        self.container = tk.Frame(master, bg="white")
        self.container.pack(padx=20, pady=20)

        # Create heading label
        self.heading_label = tk.Label(self.container, text="Voice Assistant", font=self.heading_font, bg="white")
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Create description label
        self.description_label = tk.Label(self.container, text="Click the button and say something", font=self.text_font, bg="white")
        self.description_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Create microphone button
        self.microphone_button = tk.Button(self.container, text="\uf130", font=("FontAwesome", 40), bg="#ff5f6d", fg="white", bd=0)
        self.microphone_button.grid(row=2, column=0, pady=10)

        # Create text entry
        self.text_entry = tk.Entry(self.container, font=self.text_font, bg="white", bd=2, relief=tk.FLAT, justify=tk.CENTER)
        self.text_entry.grid(row=3, column=0, columnspan=2, pady=(20, 0), ipady=10, ipadx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

import tkinter as tk
from tkinter import font
import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import wikipedia
from googletrans import Translator
import pygame
from gtts import gTTS
import requests
import os
import datetime
import webbrowser
import time
import sys
import ctypes
from io import BytesIO
from getallapps import get_to_open
from close_the_app import close_app
from requirementschecking import mic_checking
from requirementschecking import get_user_name

class VoiceAssistantApp:
    def __init__(self, master):
        self.master = master
        master.title("Voice Assistant")

        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

        # Create fonts
        self.heading_font = font.Font(family="Poppins", size=24, weight="bold")
        self.text_font = font.Font(family="Poppins", size=14)

        # Create container frame
        self.container = tk.Frame(master, bg="white")
        self.container.pack(padx=20, pady=20)

        # Create heading label
        self.heading_label = tk.Label(self.container, text="Voice Assistant", font=self.heading_font, bg="white")
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Create description label
        self.description_label = tk.Label(self.container, text="Click the button and say something", font=self.text_font, bg="white")
        self.description_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Create microphone button
        self.microphone_button = tk.Button(self.container, text="\uf130", font=("FontAwesome", 40), bg="#ff5f6d", fg="white", bd=0, command=self.start_listening)
        self.microphone_button.grid(row=2, column=0, pady=10)

        # Create text entry
        self.text_entry = tk.Entry(self.container, font=self.text_font, bg="white", bd=2, relief=tk.FLAT, justify=tk.CENTER)
        self.text_entry.grid(row=3, column=0, columnspan=2, pady=(20, 0), ipady=10, ipadx=10)


    def start_listening(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2, phrase_time_limit=8)

        try:
            print("Recognizing...")
            cmd = r.recognize_google(audio, language='en-in')
            print(f"You said: {cmd}\n")
            self.process_command(cmd)
        except Exception as e:
            print("Speech recognition could not understand audio")
            return "none"

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def translate_voice(self,inputText,which_lang):
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

    def get_current_temperature(self,city):
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

    def search_wikipedia(self,question_type, topic):
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

    def process_command(self):
        main_cmd = self.start_listening()

        main_input = main_cmd.lower()
        talk = self.talk()
        print(main_input)
        userName = get_user_name() 

        keywords = ["wake up", "rush", "rushee", "hey rush", "hello rush", "hey rushee", "hello rushee"]
        cmd_to_start = any(keyword in main_input for keyword in keywords)
        #cmd to get the access of Rushe
        while True:
            if   cmd_to_start:
                talk("i am ready sir , please tell me what can i do for you. ")
                while True:
                    secondary_cmd = self.start_listening()
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
                        talk(self.search_wikipedia(set_questiontype, topic))
                
                    #translate
                    elif "translate" in secondary_cmd :
                        remove_the_translate_words = secondary_cmd.replace("translate",' ')
                        print("Which Language you want change")
                        talk("Which Language you want change")
                        which_lang = self.listening_cmd().lower()
                        self.translate_voice(remove_the_translate_words,which_lang)

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
                        talk(f"Current Temperature in {city} {self.get_current_temperature(city)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    app.process_command()
''' 

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
import tkinter as tk
import threading
from PIL import Image, ImageTk
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
r = sr.Recognizer()

def listening_cmd():
    if mic_checking():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) 

            print("Listening...")
            audio = r.listen(source, phrase_time_limit=8) 

        try:
            print("Recognizing...")
            cmd = r.recognize_google(audio, language='en-in')
            #print(f"You said: {cmd}\n")
            return cmd
            
        except sr.UnknownValueError:
            #print("Speech recognition could not understand audio. Please try again.")
            return "unknown"
            
    else:
        print("Microphone is not connected")
        cmd = input("Enter the Command: ")
        return cmd
print(listening_cmd())