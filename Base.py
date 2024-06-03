import pyttsx3
import speech_recognition

r = speech_recognition.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-80)
    engine.say(command)
    engine.runAndWait()


def Listen():
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=1)
        SpeakText("Say somthing")

        audio2 = r.listen(source2)

        try:
            MyText = r.recognize_google(audio2)
        except:
            SpeakText("Didn't Recognise voice")
            SpeakText("Try again")
            Listen()
            return
    print(MyText)
    SpeakText("You said "+MyText)

Listen()
