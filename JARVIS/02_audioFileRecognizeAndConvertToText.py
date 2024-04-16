# import library
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
newvoiceRate = 170
engine.setProperty('rate',newvoiceRate)
engine.setProperty('voice',voice[0].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()


def getInput():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile('complete_freedom.wav') as source:    

        audio_text = r.record(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        print("converting the audio file into the text .... ")
        speak("Converting the autio file into the text ....")
        text = r.recognize_google(audio_text)
        print()
        print(text)
        speak(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        

if __name__ == "__main__":
    value = "Hey ! I'm Jarvis , How may I help you ? "
    speak(value)
    getInput()
