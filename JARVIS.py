import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import psutil
import os
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source :
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not understanding")
            return ""


def speechtx(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(x)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speechtx("Good Morning sir!")

    elif hour>=12 and hour<18:
        speechtx("Good Afternoon sir!")

    else:
        speechtx("Good Evening! sir")
if __name__=='__main__' :

    wishMe()
    speechtx(" how can i help you ")
    while True:
        data1 = sptext().lower()

        if "time" in data1:
           time = datetime.datetime.now().strftime("%I%M%p")
           speechtx(time)


        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")


        elif "wikipedia" in data1:
            speechtx('Searching Wikipedia...')
            data1= data1.replace("wikipedia", "")
            results = wikipedia.summary(data1, sentences=2)
            speechtx("According to Wikipedia")
            print(results)
            speechtx(results)

        elif 'open google' in data1:
            webbrowser.open("google.com")


        elif "battery" in data1:
            battery_status = psutil.sensors_battery()
            battery_status1 = battery_status.percent
            speechtx(battery_status1)


        elif 'your name' in data1:
            speechtx("my name is jarvis. i am a google assistant.  I am here to make your life easier. You can command me to perform various tasks ")


        elif 'play song' in data1:
            add = r'C:\Users\DELL\Desktop\music'
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong[0]))


        elif 'stop' in data1:
            speechtx("thank you")
            break






















    



