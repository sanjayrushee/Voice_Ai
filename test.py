from tkinter import *
import sys
import time
import requests
import pywhatkit
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os 
import threading
from PIL import Image, ImageTk
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
engine.setProperty('voice', voices[0].id)
r = sr.Recognizer()
userName = get_user_name() 
list_of_apps_opend = []

def talk(talk):
    engine.say(talk)
    engine.runAndWait()

def listening_cmd(label):
    def listen_and_recognize():
        if mic_checking():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source) 
                label.config(text="Listening...")
                audio = r.listen(source, phrase_time_limit=5) 

            try:
                label.config(text="Recognizing...")
                cmd = r.recognize_google(audio, language='en-in')
                print(f"You said: {cmd}\n")
                time.sleep(1)
                label.config(text=cmd)
                time.sleep(2)
                return cmd
            
            except sr.UnknownValueError:
                label.config(text="Could not understand audio. Please try again")
                print("Speech recognition could not understand audio. Please try again.")
                return "unknown"
            
        else:
            label.config(text="Microphone is not connected")
            print("Microphone is not connected")
    


def translate_voice(inputText,which_lang):
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')
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

def thecmdrushe(label):
    secondary_cmd = listening_cmd(label)
    response = ""

    # playing song in youtube
    if "play" in secondary_cmd:
        music = secondary_cmd.replace('play', '')
        print(music)
        
        response = "playing"
        label.config(text=response)
        talk(response)
        pywhatkit.playonyt(music)
        print("goes here")

        
    
    #getting worst jokes     
    elif "some joke" in secondary_cmd:
        response = pyjokes.get_joke()
        print(response)
        label.config(text=response)
        talk(response)
    
    #Open the default folders in windows
    elif "open download" in secondary_cmd or "open download folder" in secondary_cmd:
        openPath = ("C:\\Users\\default\\Downloads")  
        newpath = openPath.replace('default',userName)
        response = "opening"
        label.config(text=response)
        talk(response)
        os.startfile(newpath)

    elif "video folder" in secondary_cmd or "video path"  in secondary_cmd:
        openPath = ("C:\\Users\\default\\Videos")
        newpath = openPath.replace('default',userName)
        response = "opening"
        label.config(text=response)
        talk(response)
        os.startfile(newpath) 

    elif "document folder" in secondary_cmd or "document path"  in secondary_cmd:
        try:
            openPath = ("C:\\Users\\default\\Documents")
            newpath = openPath.replace('default',userName)
            response = "opening"
            label.config(text=response)
            talk(response)
            os.startfile(newpath) 
        except:
            openPath = ("C:\\Users\\default\\OneDrive\\Documents")
            newpath = openPath.replace('default',userName)
            response = "opening"
            label.config(text=response)
            talk(response)
            os.startfile(newpath) 

    elif "music folder" in secondary_cmd or "music path"  in secondary_cmd:
        openPath = ("C:\\Users\\default\\Music")
        newpath = openPath.replace('default',userName)
        response = "opening"
        label.config(text=response)
        talk(response)
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
        response = search_wikipedia(set_questiontype, topic)
        label.config(text=response)
        talk(response)
    
    #translate
    elif "translate" in secondary_cmd :
        remove_the_translate_words = secondary_cmd.replace("translate",' ')
        label.config(text="Which Language you want change")
        talk("Which Language you want change")
        which_lang = listening_cmd(label).lower()
        label.config(text=which_lang)
        response = translate_voice(remove_the_translate_words,which_lang)
        label.config(text=response)

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
        datewithtime = datetime.datetime.now().strftime('%I %M %p')
        print(datewithtime)
        response = "The current time is " + datewithtime
        label.config(text=response)
        talk(response)
    
    #asking loacation 
    elif "where is" in secondary_cmd:
        location = secondary_cmd.replace("where is", "")
        response = "searching" + location
        talk(response)
        webbrowser.open("https://www.google.com/maps/place/" + location)

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
        
    elif "what is current temperature in" in secondary_cmd.lower():
        city = secondary_cmd.replace("what is current temperature in", ' ').lower()
        response = f"Current Temperature in {city} {get_current_temperature(city)}"
        label.config(text=response)
        talk(response)
    else:
        label.config(text="Invalid ,Try Again")

    

text_label = None

def create_text(root, text_content):
    global text_label  
    max_height = 150
    fixed_width = 480

    text_label = Label(root, text=text_content, wraplength=fixed_width, justify="left", background="#E7DBDB")
    text_label.place(x=580, y=380)

    num_lines = len(text_content.split('\n'))

    font_size = 20  
    while font_size < 100:  
        text_label.config(font=("Helvetica", font_size))
        text_label.update_idletasks()  
        text_label_width = text_label.winfo_reqwidth()
        text_label_height = text_label.winfo_reqheight()

        if text_label_height > max_height or text_label_width > fixed_width:
            font_size -= 1 
            text_label.config(font=("Helvetica", font_size))
            text_label.update_idletasks()  
            text_label_width = text_label.winfo_reqwidth()
            text_label_height = text_label.winfo_reqheight()

        else:
            break

def button_clicked():
    global text_label 
    thecmdrushe(text_label)

root = Tk()
root.title("Voice Assistant")

bg = PhotoImage(file="background.png")

image_width = bg.width()
image_height = bg.height()

root.geometry(f"{image_width}x{image_height}")

canvas = Canvas(root, width=image_width, height=image_height, highlightthickness=0)
canvas.pack()

canvas.create_image(image_width/2, image_height/2, image=bg)

text_content = "Your text goes here."
create_text(root, text_content)

button_image = PhotoImage(file="button.png")
button = Button(canvas, image=button_image, command=button_clicked, bd=0, highlightthickness=0, bg="#E7DBDB", activebackground="#E7DBDB")
button.place(x=276, y=354)

root.mainloop()
