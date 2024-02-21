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
from getallapps import get_to_open
from close_the_app import close_app
from requirementschecking import mic_checking
from requirementschecking import get_user_name



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
list_of_apps_opend = []
r = sr.Recognizer()



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


def thecmdrushe():
    while True:
        main_cmd = listening_cmd()
        main_cmd = main_cmd.lower()
        cmd_to_start = ["wake up", "rush", "rushee",'hey rush',"hello rush","hey rushee","hello rushee"]
        if   main_cmd in cmd_to_start:
            talk("i am ready sir , please tell me what can i do for you. ")
            while True:
                secondary_cmd = listening_cmd()
                secondary_cmd = secondary_cmd.lower()
                if "play" in secondary_cmd:
                    music = secondary_cmd.replace('play', '')
                    print(music)
                    talk("playing")
                    pywhatkit.playonyt(music)
                elif "some joke" in secondary_cmd:
                    jk = pyjokes.get_joke()
                    print(jk)
                    talk(jk)
                
                elif "open download" in secondary_cmd or "open download path" in secondary_cmd:
                    openPath = ("C:\\Users\\default\\Downloads")   
                    
                elif "open video" in secondary_cmd or "open video path"  in secondary_cmd:
                    os.startfile("C:\\Users\\fortever\\Video")     #replace your user path
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

                elif "time now" in secondary_cmd.lower():
                    time = datetime.datetime.now().strftime('%I %M %p')
                    print(time)
                    talk("The current time is" + time)
                elif "where is" in secondary_cmd:
                    location = secondary_cmd.replace("where is", "")
                    talk("searching" + location)
                    webbrowser.open("https://www.google.com/maps/place/" + location)
                elif "go to study" in secondary_cmd.lower() or "study mode" in secondary_cmd.lower():
                    # talk("which one you want sir")
                    webbrowser.open("https://swayam.gov.in/") # need to develope 

                elif "music" in secondary_cmd or "play some music " in secondary_cmd.lower():
                    song = os.listdir("E:\\Music\\Songs")  #replace your user path
                    os.startfile(os.path.join("E:\\Music\\Songs", song[5])) #replace your user path
                    break
                elif "see you later" in secondary_cmd.lower():
                    print("see you later , sir ")
                    exit()
                elif "go to sleep" in secondary_cmd:
                    talk("Call me when you need")
                    break
                elif "power off " in secondary_cmd.lower() or "poweroff" in secondary_cmd.lower():
                    talk("Your system will be power off in few seconds")
                    os.system("shutdown /s /t 7")
                    os.system('taskkill /F /IM *')
                    sys.exit()
                elif "restart my pc" in secondary_cmd.lower() or "restart my computer" in secondary_cmd.lower():
                    talk("your system will be Restart in few seconds ")
                    os.system("shutdown /r /t  1")
                    ti.sleep(1)
                    sys.exit()
                elif "lock my pc" in secondary_cmd.lower() or "lock my computer" in secondary_cmd.lower():
                    talk("ok")
                    ctypes.windll.user32.LockWorkStation()
                elif "notepad" in secondary_cmd.lower() or "Notepad " in secondary_cmd:
                    notepad = "notepad.exe"
                    filename = "file.txt"
                    sp.Popen([notepad, filename])
                elif "movie folder" in secondary_cmd.lower():
                    mf = "which movie folder , I want to open sirrr " + "Normal movie fooo" \
                                                                        "lder or telegram path"
                    print(mf)
                    talk(mf)
                    mfs = listening_cmd().lower()
                    if "one" in mfs.lower() or "normal movie" in mfs.lower() or "1" in mfs.lower():
                        talk("opening")
                        os.startfile("D:\\Movie") #replace your user path
                    elif "two" in mfs.lower() or "telegram" in mfs.lower() or "2" in mfs.lower():
                        talk("opening")
                        os.startfile("E:\\cDownloads\\Telegram Desktop") #replace your user path
                    else:
                        print("can't hear you , sir")
                # elif "send email" in secondary_cmd.lower() or "send a email" in secondary_cmd.lower():
                # smail()

                elif "what is temperature" in secondary_cmd.lower():
                    pass
                # shut down
                elif "power off" in secondary_cmd.lower():
                    talk("Your system will be power off in few seconds ")
                    os.system("shutdown /s /t 1")
                    exit()
             

if __name__ == "__main__":
    wish()
    talk("welcome sir , I am rushe your assistant ")
    thecmdrushe()

#this is testing line
