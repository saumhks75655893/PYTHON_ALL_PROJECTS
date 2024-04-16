import pyttsx3
import speech_recognition as sr
import datetime


# for voice
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voices", voice[0].id)
setNewvoice = 150
engine.setProperty('rate', setNewvoice)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getInput():
    r = sr.Recognizer()
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source:
            print("Listening ......... ")
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.2)
             
            #listens for the user's input 
            audio = r.listen(source)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
 
            print("\"Did you say : \" ",MyText)
            speak(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")


if __name__ == "__main__":
    speak("Hey! I'm Jarvis, Please tell How can I help You ? ")
    getInput()
