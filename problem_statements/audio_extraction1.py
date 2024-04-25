import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator
import gtts
from playsound import playsound

recognizer = sr.Recognizer()

def extract_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio_file = "extracted_audio.wav"
    audio.write_audiofile(audio_file)
    return audio_file

def main():
    video_path = "san.mp4"
    extracted_audio_file = extract_audio(video_path)
    audio_file = extracted_audio_file
    target_lang=input("Please enter target language: ")
    source_lang=input("Please enter source language: ")
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        listen = recognizer.recognize_google(audio_data, language=source_lang)
        translator = Translator()
        translate = translator.translate(listen, dest=target_lang)
        t1 = gtts.gTTS(translate.text, lang=target_lang)
        t1.save("Test1.mp3")
        playsound("Test1.mp3")
    print("Transcription:", listen)

if __name__ == "__main__":
    main()
