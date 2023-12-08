import wikipedia
import pywhatkit as pwk
import pyttsx3 as p
from text_to_speech import speak

# Initialize the text-to-speech engine
engine = p.init()

# Set engine properties
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english')

# Function to search on Wikipedia
def search_wikipedia(query):
    speak("Searching Wikipedia....")    
    # Remove "wikipedia" from the query
    query = query.replace("wikipedia", "")   
    # Get Wikipedia summary
    results = wikipedia.summary(query, sentences=2)
        
    # Adjust the speech rate
    engine.setProperty('rate', 125)    
    # Speak the Wikipedia results
    speak("According to Wikipedia..")
    speak(results)   
    # Reset the speech rate
    engine.setProperty('rate', 150)
    
# Function to perform searches
def perform_search(query):
    query = query.replace("search", "")   
    # Check for specific search engines
    if "on google" in query:
        query = query.replace("on google", "")
        search_engine = "Google"
    elif "on youtube" in query:
        query = query.replace("on youtube", "")
        search_engine = "YouTube"
    else:
        search_engine = "Default"   
    # Perform the search using pywhatkit
    pwk.search(query)
    
# Function to fetch information
def fetch_information(query):
    query = query.replace("tell me", "")
    if "about" in query:
        query = query.replace("about", "")
    speak(f"Sure, Here is what I found about {query}")
    pwk.info(query)
    
# Function to Send WhatsApp message
def send_whatsapp_message():
    try:
        speak("Please provide a number to send a message")
        number = takeCommand()      
        speak("What should I send?")
        message = takeCommand()
        
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute) + 2
        # added 2 extra minutes to ensure that time does not change in between the process
        
        pwk.sendwhatmsg(f"+91{number}", message, hour, minute, 8)
        speak("Message Sent")      
    except Exception as e:
        print(e)
        speak("Sorry! Could not send the message")
        
# Function to tell a joke
def tell_joke():
    # Get a neutral joke in English
    my_joke = pyjokes.get_joke(language="en", category="neutral")
    # Speak the introduction
    speak("Oh! Here is one,")
    # Adjust the speech rate for better delivery
    engine.setProperty('rate', 125)
    # Speak the joke
    speak(my_joke)
    # Reset the speech rate to the default value
    engine.setProperty('rate', 150)
