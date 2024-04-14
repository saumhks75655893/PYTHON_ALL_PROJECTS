import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing .... ")
        query = r.recognize_google_cloud(audio, language="en-in")
        print(f"user said : {query} \n")

    except Exception as e:
        print("Sorry ! Please say that again . . ")
        return "None"

    return query



if __name__ == "__main__":
    speak("Hello, It's Jarvis ! How may I help you? ")
    speak(takeInput())
