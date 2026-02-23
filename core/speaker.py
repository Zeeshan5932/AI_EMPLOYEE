import pyttsx3
import time
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)