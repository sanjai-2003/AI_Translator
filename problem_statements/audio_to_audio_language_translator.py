import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
s=input("Source language: ")
t=input("Target Language: ")
with sr.Microphone() as source:
    print("Speak now")
    voice = recognizer.listen(source)
    listen = recognizer.recognize_google(voice, language=s)
    print(listen)

translator = googletrans.Translator()
translate = translator.translate(listen, dest=t)
t1 = gtts.gTTS(translate.text, lang=t)
t1.save("hello.mp3")
playsound.playsound("hello.mp3")

