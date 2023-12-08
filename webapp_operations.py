# webapp_operations.py
import os
import webbrowser # Web browser interaction
import pywhatkit as pwk  
from text_to_speech import speak

# 'Open Website' Command
def open_website(url, site_name):
    try:
        webbrowser.open(url)
        speak(f"Sure, Opening {site_name}")
    except Exception as e:
        speak(f"Sorry, I couldn't open {site_name}. Error: {str(e)}")

# 'Open Web/App' Command
def open_app_or_website(app_name, app_executable, website_url):
    if os.path.isfile(app_executable):
        os.system(app_executable)
        speak(f"Opening {app_name} app.")
    else:
        webbrowser.open(website_url)
        speak(f"Opening {app_name} website.")
        
# 'Play on Youtube' Command
def playOnYoutube(query):
    query = query.replace("on youtube", "")
    if "play" in query:
        query = query.replace("play", "")
    speak("playing"+query)
    pwk.playonyt(query)
    

