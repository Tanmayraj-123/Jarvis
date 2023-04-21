import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good evening Sir!")
    speak("I am jarvis the assistant manager of Tanmay raj")
    speak("How may i help you sir?")

def takeCommand() -> object:
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 200, 10)

    try:
        print("Recognizing...."),
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please....")
        return "None"
    return query
    
if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open vedantu' in query:
            webbrowser.open("vedantu.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open w3schools' in query:
            webbrowser.open("w3schools.com")

        elif 'open email' in query:
            webbrowser.open("gmail.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Khanak Raj\\Music\\New Song'
            songs = os.listdir(music_dir)
            print (songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Tanmay Sir, The time is {strTime}")  

        elif 'open minecraft' in query:
            mineCraft = "C:\\Users\\Khanak Raj\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(mineCraft)    