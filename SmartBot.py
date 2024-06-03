import pyttsx3
import speech_recognition
import webbrowser
import pyjokes
import os

r = speech_recognition.Recognizer()
YTSeach = ['Youtube Search', 'Search Youtube', 'Search for a video on youtube', 'YouTube search']
TellJoke = ['Tell me a joke', 'Joke', 'Tell me a funny joke', 'tell me a joke', 'joke, tell me a funny joke']
Shutdown = ['shut down my pc', 'shut down my commputer', 'shut down', 'turn off']

def SpeakText(command):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-80)
    engine.say(command)
    engine.runAndWait()


def Listen():
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=1)
        SpeakText("What do you want me to do")

        audio2 = r.listen(source2)

        try:
            MyText = r.recognize_google(audio2)
            print(MyText)

            if MyText in YTSeach:

                with speech_recognition.Microphone() as source2:
                    SpeakText('What do you want to search?')
                    r.adjust_for_ambient_noise(source2, duration=1)
                    audio2 = r.listen(source2)
                    try:
                        video = r.recognize_google(audio2)
                    except:
                        SpeakText("Didn't Recognise voice")
                        SpeakText("Try again")
                        Listen()
                        return

                    video = video.lower()
                SpeakText("Searching " + video)
                webbrowser.open("https://www.youtube.com/results?search_query=" + video)

            if MyText in TellJoke:
                SpeakText(pyjokes.get_joke())

            if MyText in Shutdown:
                SpeakText("Shutting down computer in 5")
                SpeakText('4')
                SpeakText('3')
                SpeakText('2')
                SpeakText('1')
                SpeakText('Good bye')

                os.system('shutdown -s')

        except:
            SpeakText("Didn't Recognise voice")
            SpeakText("Try again")
            Listen()
            return

Listen()
