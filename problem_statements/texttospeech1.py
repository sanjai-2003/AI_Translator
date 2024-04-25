from googletrans import Translator
import gtts
import tempfile
from playsound import playsound
s=input("Please enter source Language: ")
text1=input("Please enter text to be translated: ")
e=input("Please enter the Language the text has to be translated: ")
translator = Translator()
translated_text = translator.translate(text1, src=s, dest=e).text
t1 = gtts.gTTS(translated_text, lang=e)
t1.save("Test.mp3")
playsound("Test.mp3")


