# text_to_speech.py
import pyttsx3 as p

# Initialize the text-to-speech engine
engine = p.init()

# Set engine properties
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english')

# Function to enable the engine to speak
def speak(text):
    print("Saying:", text)
    engine.say(text)
    engine.runAndWait()

