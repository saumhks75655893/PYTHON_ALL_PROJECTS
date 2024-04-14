# for voice
import pyttsx3

eg = pyttsx3.init()
voices = eg.getProperty("voices")
# print(voices[0].id)
# print(voices[1].id)
newVoiceRate = 130
eg.setProperty('rate', newVoiceRate)
eg.setProperty('voice',voices[0].id)


# for voice
def speak(audio):
    eg.say(audio)
    eg.runAndWait()


# our own files(make it to read automatically using speech recognization system )
if __name__ == "__main__":
    with open("text.txt", "r") as f:
        value = f.read()
        speak(value)
