# speech_recognition.py
import speech_recognition as sr

# Function to take User Commands (Listen, Recognize, Display)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print("Could Not Understand...")
        return "None"

