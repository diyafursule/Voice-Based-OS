# main.py
import threading 
import time
from text_to_speech import speak
from speech_recognizer import takeCommand
from datetime_operations import wishMe
from background_tasks import check_for_updates, perform_maintenance, perform_background_tasks
from assistant_functions import assistant_function

if __name__ == "__main__":
    # Call wishMe() Func
    wishMe()
    
    # Shared variable for last activity time
    last_activity_time_lock = threading.Lock()
    last_activity_time = time.time()

    
    # Start the background task thread
    background_thread = threading.Thread(target=perform_background_tasks)
    background_thread.start()
    
    while True:
        query = takeCommand()
        if query == "exit":
            speak("Okay...Goodbye!")
            break
        if query != "None":
            assistant_function(query)
            last_activity_time = time.time()

        # Check for inactivity
        with last_activity_time_lock:
            if time.time() - last_activity_time >= 20:
                speak("No activity. Exiting.")
                exit()
            
    # Wait for the background task thread to finish
    background_thread.join()  

