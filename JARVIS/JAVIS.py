import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

eg = pyttsx3.init()
voices = eg.getProperty("voices")
newVoiceRate = 190
eg.setProperty('rate', newVoiceRate)
eg.setProperty('voice', voices[0].id)


# for voice
def speak(audio):
    eg.say(audio)
    eg.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good after noon !")
    else:
        speak("Good evening, sir!")

    speak("I'm Jarvis. Please!  how may I help you? ")

# to take input from the user


def takeInput():
    ''' It takes microphone input from the user and return string output. '''
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listenning .........")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    try:

        print("Recognizing ... ")
        query = r.recognize_google(audio)
        print(f"User said: {query}")
        # speak(text)

    except Exception as e:
        print("Sorry! Please repeat again .... ")
        return "None"

    return query


# our own files(make it to read automatically using speech recognization system )
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeInput().lower()

        # logic to executing tasked based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia ...... ")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia.... ")
            print()
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("www.youtube.com")
            
        elif 'google' in query: 
            webbrowser.open("www.google.com")
            
        elif 'facebook' in query:
            webbrowser.open("www.facebook.com")
            
        elif 'geeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/user/himanshukumnq5k/")

        elif 'close' in query:
            print()
            print()
            print("Thanks for using... ")
            speak("Thanks for using...")
            break
