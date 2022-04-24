import speech_recognition as sr
from pyttsx3 import init as pyx3
from webbrowser import open as wopen
from pyautogui import press as pig
from random import randint
from time import sleep as slp
from datetime import datetime as datem
import tkinter as tk
from psutil import sensors_battery as bat
flag = False
#pyinstaller --onefile --icon=images.ico main.py
battery = bat()
r = sr.Recognizer()
def speak(command):
    engine = pyx3()
    engine.say(command)
    engine.runAndWait()
return_array = ["yes?", "thats me!", "Yo!", "Here I Am!", "I am Summoned!", "Hello!"]
speak(return_array[randint(0, len(return_array) - 1)])
def commands(mt):
    if "stop" in mt or "continue" in mt:
        pig("volumemute")
        return
    elif "battery" in mt:
        percent = str(battery.percent)
        speak("Battery %"+percent)
        return
    elif "information" in mt:
        window = tk.Tk()
        window.title("Imagine")
        window.iconbitmap('images.ico')
        greeting = tk.Label(
            text="Imagine is the activate and deactivate command\nstop continue\nbattery\ninformation\ntext line(for enter)\ntime\ntoday\ndown\nup\nyoutube(with searching content)\ngoogle(with searching content)\ntranslate(with searching content)\nsystemexit",
            foreground="white",
            background="black")
        greeting.pack()
        window.mainloop()
    elif "text" in mt or "line" in mt:
        if "text" in mt:
            for element in str(mt.split("text")[1]):
                pig(element)
        else:
            for element in str(mt.split("line")[1]):
                pig(element)
            pig("enter")
    elif "time" in mt:
        strTime = datem.now().strftime("%H:%M")
        speak(strTime)
        return
    elif "today" in mt:
        today = datem.now().strftime("%d,%m")
        speak("date:"+str(today))
        return
    elif "down" in mt:
        pig("volumedown")
        pig("volumedown")
        pig("volumedown")
        return
    elif "up" in mt:
        pig("volumeup")
        pig("volumeup")
        return
    elif "youtube" in mt:
        speak("Opening youtube")
        if not mt == "youtube":
            wopen(("https://www.youtube.com/results?search_query="+str(mt.split("youtube")[1])).replace(" ", "+"))
        else:
            wopen("https://www.youtube.com")
        return
    elif "google" in mt:
        wopen("https://www.google.com")
        speak("Opening google")
        slp(1)
        for element in str(mt.split("google")[1]):
            pig(element)
        pig("enter")
        return
    elif "translate" in mt:
        wopen("https://translate.google.com")
        speak("Opening translate")
        slp(1)
        for element in str(mt.split("translate")[1]):
            pig(element)
        pig("enter")
        return
    elif "system exit" in mt or "systemexit" in mt:
        speak("Good Bye!")
        quit()
while (1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            mt = r.recognize_google(audio2)
            mt = mt.lower()
            if "imagine" in mt:
                flag = not flag
                if flag:
                    speak("Activated")
                else:
                    speak("deactivated")
            if flag:
                commands(mt)
    except sr.RequestError as e:
        continue
    except sr.UnknownValueError as ex:
        continue
    finally:
        r = sr.Recognizer()
if __name__ == '__main__':
    pass