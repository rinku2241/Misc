#Project JARVIS 
import datetime
import email
from email.message import EmailMessage  
import speech_recognition as sr
from ast import main
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
email=["harry:harry2@gmail.com", "damon:daemon2@gmail.com"


engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good mornings")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else: 
        speak("good evening")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio =r.listen(source)
    try:
        print("recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f'user said:{query}\n')
    except Exception as e:
        # print(e)

        print("say that again please")
        return "none"
    return query
def sendmail(to, content):
    server= smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("rinku2241@gmail.com", "daemondemetra")
    server.sendmail("rinku2241@gmail.com", to, content)


    speak("i am jarvis , how may i help you? ")
if __name__=="__main__":
    speak('Welcome Daemon,')

    wishme()
    while True:
        query=takecommand().lower()

        
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            url='https://youtube.com/'
            speak("opening youtube")

            webbrowser.open(url)
        elif 'open google' in query:
            url='https://google.com/'
            speak("opening google")

            webbrowser.open(url)
        elif 'play music' in query:
            music_dir ='C:\\Users\\DaeMon\\Downloads\\PUnjabi songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the time is {strTime}")

        elif 'excellent' in query:
            speak("thank you sir , i always like to help you ")
        elif'go to sleep' in query:
            speak('okay sir , lemme know when you need me')
        elif 'exit' in query:
            speak("okay im going away ,ill miss you sirr" )
            break
        elif 'open code' in query:
            codepath="C:\\Users\\DaeMon\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'house of the dragon' in query:
            try:
                speak("what should i say")
                content = takecommand()
                to="danielradclyffe20@gmail.com"
                sendmail(to, content)
                speak("email has been sent ")
            except Exception as e:
                print(e)
                speak("sorry something went wrong ")
            
            #here hange
            
            
            