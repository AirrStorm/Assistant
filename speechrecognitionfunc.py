import speech_recognition as sr

def listen():
    recog = sr.Recognizer()

    mic = sr.Microphone()
    with mic as source:
        recog.adjust_for_ambient_noise(source)
        recog.dynamic_energy_threshold = 280 
        print("Listening....")
        audio = recog.listen(source)
        try:
            text = recog.recognize_google(audio)
            print(text)
            return text.lower()

        except sr.UnknownValueError:
            print("Sorry, couldn't understand you")
            return ""
        
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

