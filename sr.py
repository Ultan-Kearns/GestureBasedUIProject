import speech_recognition as sr
import pyaudio

def voice_input():
    #get speech
    r = sr.Recognizer()
    microphone = sr.Microphone()
    #boiler plate code to filter out ambient noise noise from mic
    with microphone as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
    #test example taken from docs
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


voice_input()
