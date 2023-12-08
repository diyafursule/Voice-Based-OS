# datetime_operations.py
import datetime
import os
from text_to_speech import speak

# Function to greet when the program begins to run
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 12 <= hour < 18:
        speak("Good Afternoon " + os.getlogin().capitalize())
    elif 0 <= hour < 12:
        speak("Good Morning " + os.getlogin().capitalize())
    else:
        speak("Good Evening " + os.getlogin().capitalize())

# 'Time' Command
def speak_time_in_oclock():
    now = datetime.datetime.now()
    hour = now.strftime("%I")  # %I is for 12-hour clock format
    minutes = now.strftime("%M")
    am_pm = now.strftime("%p")

    time_text = f"{hour} {minutes} {am_pm}"
    speak(f"The time is {time_text}")
    
# 'Date' Command
def speak_today_date():
    now = datetime.datetime.now()
    day_of_week = now.strftime("%A")  # E.g., "Monday"
    formatted_date = now.strftime("%B %d, %Y")  # E.g., "October 25, 2023"
    speak(f"Today's date is {formatted_date}. It is {day_of_week}")

# 'Day' Command
def speak_today_day():
    now = datetime.datetime.now()
    day_of_week = now.strftime("%A")  # E.g., "Monday"
    speak(f"Today is {day_of_week}")
