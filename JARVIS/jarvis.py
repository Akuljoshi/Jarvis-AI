import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:  
        speak("Good Morning!")
    
    elif hour >=12 and hour <18:  
        speak("Good Afternoon!")

    else: 
        speak("Good Evening!")

    speak("My name is Jarvis. how may I help you")

def takeComand():
    #It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akuljoshi100@gmail.com', 'your_pass')
    server.sendmail('akuljoshi100@gmail.com', to, content)
    server.close()
     
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeComand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print((results).encode('utf8')) 
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'F:\\akul\\music'
            songs = os.listdir(music_dir)
            print(songs)
            n = len(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,n)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            #codepath = "C:\\Users\\a\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            codepath = "C:\\Users\\a\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)

        elif 'email to akul' in query:
            try:
                speak("what should I say?")
                content = takeComand()
                to = "akuljoshi100@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry , i am unable to send this e-mail")

        elif 'quit' in query:
            speak("see you soon, bye bye")
            exit()
           
        elif 'exit' in query:
            speak("see you soon, bye bye")
            exit()



        
