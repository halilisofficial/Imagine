import speech_recognition as sr
from pyttsx3 import init as pyx3
from webbrowser import open as wopen
from pyautogui import press as pig
from random import randint
from time import sleep as slp
from datetime import datetime as date
import tkinter as tk
r = sr.Recognizer()
def speak(command):
    engine = pyx3()
    engine.say(command)
    engine.runAndWait()
return_array = ["yes?", "thats me!", "Yo!", "Here I Am!", "I am Summoned!", "Hello!"]
def commands(mt):
    if "sleep" in mt:
        speak("Sleeping 60 seconds")
        slp(60)
        speak("What did i miss")
        return
    if "stop" in mt or "continue" in mt or "mute" in mt:
        pig("volumemute")
        return
    if "information" in mt:
        window = tk.Tk()
        window.title("Imagine")
        window.iconbitmap('images.ico')
        greeting = tk.Label(
            text="sleep(slēp)\nstop(stäp)\tcontinue(kənˈtinyo͞o)\tmute(myo͞ot)\ninformation(infərˈmāSH(ə)n)\ntext(tekst)\ntime(tīm)\thour(ˈou(ə)r)\ndown(doun)\nup(əp)\nyoutube(yo͞o t(y)o͞ob)\ngoogle(ˈɡo͞oɡ(ə)l)\nimagine close(iˈmajən klōs)\timagine stop(iˈmajən stäp)\timagine exit(iˈmajən ˈeɡzət)\nimagine(iˈmajən)",
            foreground="white",
            background="black")
        greeting.pack()
        window.mainloop()
        return
    if "text" in mt:
        for element in mt.split("text")[1]:
            pig(element)
        pig("enter")
    if "time" in mt or "hour" in mt:
        strTime = date.now().strftime("%H:%M")
        speak(strTime)
        return
    if "down" in mt:
        pig("volumedown")
        pig("volumedown")
        pig("volumedown")
        return
    if "up" in mt:
        pig("volumeup")
        pig("volumeup")
        return
    if "youtube" in mt:
        wopen("https://www.youtube.com")
        speak("Opening youtube")
        return
    if "google" in mt:
        wopen("https://www.google.com")
        speak("Opening google")
        slp(1)
        for element in mt.split("google")[1]:
            pig(element)
        pig("enter")
        return
    if (("close" in mt and "imagine") or ("imagine" in mt and "stop" in mt) or ("imagine" in mt and "exit" in mt))and len(mt.split()) == 2:
        speak("Good Bye!")
        quit()
    if "imagine" in mt:
        return speak(return_array[randint(0,len(return_array)-1)])
while (1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            mt = r.recognize_google(audio2)
            mt = mt.lower()
            commands(mt)
    except sr.RequestError as e:
        continue
    except sr.UnknownValueError as ex:
        continue
    finally:
        r = sr.Recognizer()
if __name__ == '__main__':
    pass