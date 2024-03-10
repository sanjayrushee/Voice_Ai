import sys
import time as time
import requests
import pywhatkit
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os 
import tkinter as tk
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
engine.setProperty('voice',voices[0].id)
r = sr.Recognizer()
userName = get_user_name() 
list_of_apps_opend = []


def talk(talk):
    engine.say(talk)
    engine.runAndWait()
    


def listening_cmd():
    if mic_checking():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) 

            print("Listening...")
            audio = r.listen(source, phrase_time_limit=5) 

        try:
            print("Recognizing...")
            cmd = r.recognize_google(audio, language='en-in')
            print(f"You said: {cmd}\n")
            return cmd
            
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio. Please try again.")
            return "unknown"
            
    else:
        print("Microphone is not connected")
        cmd = input("Enter the Command: ")
        return cmd

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
        secondary_cmd = listening_cmd()
        secondary_cmd = secondary_cmd.lower()
        response = ""
        # playing song in youtube
        if "play" in secondary_cmd:
            music = secondary_cmd.replace('play', '')
            print(music)
            response = "playing"
            talk(response)
            pywhatkit.playonyt(music)
            
        
        #getting worst jokes     
        elif "some joke" in secondary_cmd:
            response = pyjokes.get_joke()
            print(response)
            talk(response)
        
        #Open the default folders in windows
        elif "open download" in secondary_cmd or "open download folder" in secondary_cmd:
            openPath = ("C:\\Users\\default\\Downloads")  
            newpath = openPath.replace('default',userName)
            response = "opening"
            talk(response)
            os.startfile(newpath)

        elif "video folder" in secondary_cmd or "video path"  in secondary_cmd:
            openPath = ("C:\\Users\\default\\Videos")
            newpath = openPath.replace('default',userName)
            response = "opening"
            talk(response)
            os.startfile(newpath) 

        elif "document folder" in secondary_cmd or "document path"  in secondary_cmd:
            try:
                openPath = ("C:\\Users\\default\\Documents")
                newpath = openPath.replace('default',userName)
                response = "opening"
                talk(response)
                os.startfile(newpath) 
            except:
                openPath = ("C:\\Users\\default\\OneDrive\\Documents")
                newpath = openPath.replace('default',userName)
                response = "opening"
                talk(response)
                os.startfile(newpath) 

        elif "music folder" in secondary_cmd or "music path"  in secondary_cmd:
            openPath = ("C:\\Users\\default\\Music")
            newpath = openPath.replace('default',userName)
            response = "opening"
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
            talk(response)
        
        #translate
        elif "translate" in secondary_cmd :
            remove_the_translate_words = secondary_cmd.replace("translate",' ')
            print("Which Language you want change")
            talk("Which Language you want change")
            which_lang = listening_cmd().lower()
            response = translate_voice(remove_the_translate_words,which_lang)

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
            response = "The current time is" + time
            talk(response)
        
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
            talk(response)
        return response


class VoiceAssistantUI:
    def __init__(self, assistant):
        self.assistant = assistant
        self.thread_stop = threading.Event()

        self.root = tk.Tk()
        self.root.title("Voice Assistant")

        # Set the background color of the window
        self.root.configure(bg="#2C3E50")  # Dark blue background

        # Create a canvas to draw the circular background
        self.canvas = tk.Canvas(self.root, width=120, height=120, bg="#2C3E50", highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

       
        # Load the microphone icon image and resize it
        mic_image = Image.open("mic.png")  # Replace "mic.png" with your mic icon image file
        mic_image = mic_image.resize((100, 100))  # Adjust the size as needed
        self.mic_image = ImageTk.PhotoImage(mic_image)

        # Create a button with the microphone icon and customized properties
        self.mic_button = tk.Button(
            self.root,
            image=self.mic_image,
            command=self.thecmdrushe_thread,
            bd=0,
            bg="#2C3E50",  # Dark blue background
            activebackground="#2C3E50",
            borderwidth=0,
            relief=tk.FLAT
        )

        # Place the mic button at the center of the canvas
        self.canvas.create_window(60, 60, window=self.mic_button)

        # Create a label to display the text
        self.text_label = tk.Label(
            self.root, text="", bg="#2C3E50", fg="#ECF0F1", font=("Arial", 16)
        )

        # Place the label at the center of the window
        self.text_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Center the window on the screen
        self.center_window()

        # Set up window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def center_window(self):
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position of the window
        x = (screen_width - 500) // 2
        y = (screen_height - 400) // 2

        # Set the window position
        self.root.geometry('500x400+{}+{}'.format(x, y))

    def thecmdrushe_thread(self):
        print("Voice recognition started!")
        text = thecmdrushe()  # Call your voice recognition function here
        print("Voice recognition completed!")
        # Update the label with the recognized text
        self.text_label.config(text=" " + text)

    def on_close(self):
        # Set the flag to stop the thread
        self.thread_stop.set()
        # Wait for the thread to complete
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = VoiceAssistantUI(None)  # Pass your voice assistant instance here
    ui.run()