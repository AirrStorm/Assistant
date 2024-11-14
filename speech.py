from gtts import gTTS
from playsound import playsound
import os

def convert(answer):
    try:
        lan = 'en'
        speech = gTTS(text=answer, lang=lan, slow=False)
        speech.save("answer.mp3")
        
        playsound("answer.mp3")  # Play the sound
        
        os.remove("answer.mp3")  # Optional: Remove the file after playing it
    except Exception as e:
        print(f"An error occurred: {e}")

