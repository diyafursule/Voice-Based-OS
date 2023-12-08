# assistant_functions.py
import os
import datetime
from text_to_speech import speak
from speech_recognizer import takeCommand
from file_operations import read_file, write_file, get_file_attributes, create_directory, delete_file_or_directory, search_for_file_or_directory, get_file_properties, file_search, copy_file, create_file
from datetime_operations import speak_time_in_oclock, speak_today_date, speak_today_day
from webapp_operations import open_website, open_app_or_website, playOnYoutube
from information import search_wikipedia, perform_search, fetch_information, send_whatsapp_message, tell_joke
from system_utilities import take_screenshot, open_camera, get_current_volume, get_current_brightness

# Your 'Assistant' functionality functions go here
# Queries
def assistant_function(query):
    if any(s in query.lower() for s in ("hi", "hello", "hey", "hay", "hai")):
        if "hi" in query.lower() or "hai" in query.lower():
            speak("Hi! I am Nova. How can I assist you?")
        elif "hello" in query.lower():
            speak("Hello! I am Nova. How can I assist you")
        elif "hey" in query.lower() or "hay" in query.lower() or "hai" in query.lower():
            speak("Hey there! I am Nova. How can I assist you")

    elif "your name" in query:
        speak("I am Nova, your assistant.")
    
    elif "who are you" in query:
        speak("I am Nova, your assistant.")

    elif "yourself" in query:
        speak("Sure.. My name is Nova. I am your assistant.")
        
    elif "how are you" in query:
        speak("I am good. Hope you are doing great too.")
        
        
    elif "search file" in query:
        search_name = query.replace("search file", "").strip()
        results = search_for_file_or_directory(search_name)
        if isinstance(results, list):
            speak("Here are the search results:")
            for result in results:
                speak(result)
        else:
            speak(results)
        
    elif "create directory" in query.lower():
        directory_name = query.replace("create directory", "").strip()
        response = create_directory(directory_name)
        speak(response)

    elif "delete file" in query.lower():
        file_path = query.replace("delete file", "").strip()
        response = delete_file_or_directory(file_path)
        speak(response)
        
    elif "file search" in query.lower():
        search_files(query)
        
    elif "copy file" in query.lower():
        copy_file(query)
        
    elif "create file" in query.lower():
        file_name = query.replace("create file", "").strip()
        speak(f"What content would you like to add to the file '{file_name}'?")
        content = takeCommand()
        create_file(file_name, content)

    elif "on wikipedia" in query.lower():
        search_wikipedia(query)
    
    elif "joke" in query.lower():
        tell_joke()

    elif "on youtube" in query.lower():
        playOnYoutube(query)
        exit()
    
    elif "play" in query:
        playOnYoutube(query)
        exit()
        
    elif "search" in query:
        perform_search(query)
        
    elif "tell me" in query.lower():
        fetch_information(query)
        
    elif "whatsapp message" in query:
        send_whatsapp_message()
            
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("the time is - "+strTime)
        speak_time_in_oclock()
    
    elif "date" in query:
        speak_today_date()
        
    elif "day" in query:
        speak_today_day()
     
    elif "screenshot" in query.lower():
    	take_screenshot()
    	
    elif "open camera" in query.lower():
    	open_camera()
    	
    elif "get volume" in query.lower():
    	get_current_volume()
    	
    elif "get brightness" in query.lower():
    	get_current_brightness()
        
    elif "open youtube" in query.lower():
        open_website("https://www.youtube.com", "YouTube")
        
    elif "open stack overflow" in query.lower():
        open_website("https://stackoverflow.com", "StackOverflow")
        
    elif "open wikipedia" in query.lower():
        open_website("https://www.wikipedia.org", "Wikipedia")
        
    elif "open github" in query.lower():
        open_website("https://github.com", "GitHub")

    elif "open amazon" in query.lower():
        open_website("https://www.amazon.com", "Amazon")
    
    elif "open weather" in query:
        open_website("https://www.weather.com", "The Weather Channel")
    
    elif "open gmail" in query.lower():
        open_website("https://mail.google.com", "Gmail")

    elif "open google docs" in query.lower():
        open_website("https://docs.google.com", "Google Docs")

    elif "open google slides" in query.lower():
        open_website("https://slides.google.com", "Google Slides")

    elif "open google sheets" in query.lower():
        open_website("https://sheets.google.com", "Google Sheets")

    elif "open news" in query.lower():
        open_website("https://news.google.com", "Google News")

    elif "open nptel" in query.lower():
        open_website("https://nptel.ac.in", "NPTEL")

    elif "open leetcode" in query.lower():
        open_website("https://leetcode.com", "LeetCode")

    elif "open codechef" in query.lower():
        open_website("https://www.codechef.com", "CodeChef")

    elif "open overleaf" in query.lower():
        open_website("https://www.overleaf.com", "Overleaf")

    elif "open notion" in query.lower():
        open_website("https://www.notion.so", "Notion")

    elif "open canva" in query.lower():
        open_website("https://www.canva.com", "Canva")

    elif "open udemy" in query.lower():
        open_website("https://www.udemy.com", "Udemy")

    elif "open coursera" in query.lower():
        open_website("https://www.coursera.org", "Coursera")
        
    elif "open whatsapp" in query.lower():
        open_app_or_website("WhatsApp", "/path/to/whatsapp/executable", "https://web.whatsapp.com")

    elif "open linkedin" in query.lower():
        open_app_or_website("LinkedIn", "/path/to/linkedin/executable", "https://www.linkedin.com")

    elif "open spotify" in query.lower():
        open_app_or_website("Spotify", "/path/to/spotify/executable", "https://www.spotify.com")

    elif "open twitter" in query.lower():
        open_app_or_website("Twitter", "/path/to/twitter/executable", "https://twitter.com")

    elif "open telegram" in query.lower():
        open_app_or_website("Telegram", "/path/to/telegram/executable", "https://web.telegram.org")
        
    elif "open instagram" in query.lower():
        open_app_or_website("Instagram", "/path/to/instagram/executable", "https://www.instagram.com")

    elif "open facebook" in query.lower():
        open_app_or_website("Facebook", "/path/to/facebook/executable", "https://www.facebook.com")
    	
