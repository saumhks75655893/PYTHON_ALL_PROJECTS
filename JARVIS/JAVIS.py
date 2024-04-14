import pyttsx3
import speech_recognition as sr
import datetime


eg = pyttsx3.init()
voices = eg.getProperty("voices")
newVoiceRate = 180
eg.setProperty('rate', newVoiceRate)
eg.setProperty('voice', voices[0].id)


# for voice
def speak(audio):
    eg.say(audio)
    eg.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning , sir!")
    elif hour >= 12 and hour < 18:
        speak("Good after noon, sir!")
    else:
        speak("Good evening, sir!")

    speak("I'm Jarvis. Please! tell me , how may I help you? ")

# to take input from the user 
def takeInput():
    ''' It takes microphone input from the user and return string output. '''

# our own files(make it to read automatically using speech recognization system )
if __name__ == "__main__":
    wishMe()
