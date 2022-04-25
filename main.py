from speech_recognition import Recognizer as ssr
from speech_recognition import Microphone as mic
from speech_recognition import RequestError
from speech_recognition import UnknownValueError
from pyttsx3 import init as pyx3
from webbrowser import open as wopen
from pyautogui import press as pig
from random import randint
from time import sleep as slp
from datetime import datetime as datem
import tkinter as tk
from psutil import sensors_battery as bat
#pyinstaller --onefile --icon=images.ico main.py
def speak(command):
    engine = pyx3()
    engine.say(command)
    engine.runAndWait()
def commands(mt):
    if "stop" in mt or "continue" in mt:
        pig("volumemute")
        return
    elif "battery" in mt:
        battery = bat()
        percent = str(battery.percent)
        speak("Battery %"+percent)
        return
    elif "information" in mt:
        window = tk.Tk()
        window.title("Imagine")
        window.iconbitmap('images.ico')
        greeting = tk.Label(
            text="Imagine is the activate and deactivate command\nstop continue\nbattery\ninformation\ntext line(for enter)\ntime\ntoday\ndown\nup\nyoutube(with searching content)\nwhatsapp\ngoogle(with searching content)\ntranslate(with searching content)\nsystemexit",
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
    elif "whatsapp" in mt:
        speak("Opening whatsapp")
        wopen("https://web.whatsapp.com")

        return
    elif "google" in mt:
        speak("Opening google")
        wopen("https://www.google.com")
        slp(1)
        for element in str(mt.split("google")[1]):
            pig(element)
        pig("enter")
        return
    elif "translate" in mt:
        speak("Opening translate")
        wopen("https://translate.google.com")
        slp(1)
        for element in str(mt.split("translate")[1]):
            pig(element)
        pig("enter")
        return
    elif "system exit" in mt or "systemexit" in mt:
        speak("Good Bye!")
        quit()
if __name__ == '__main__':
    return_array = ["yes?", "thats me!", "Yo!", "Here I Am!", "I am Summoned!", "Hello!"]
    flag = True
    r = ssr()
    speak(return_array[randint(0, len(return_array) - 1)])
    while (1):
        try:
            with mic() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                mt = str(r.recognize_google(audio2))
                mt = mt.lower()
                if "imagine" in mt:
                    flag = not flag
                    speak("Activated") if flag else speak("deactivated")
                if flag:
                    commands(mt)
                slp(0.3)
        except RequestError as e:
            continue
        except UnknownValueError as ex:
            continue
        finally:
            r = ssr()
    pass