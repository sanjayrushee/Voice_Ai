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

    
'''
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



