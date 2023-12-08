import cv2  # OpenCV library for computer vision tasks
import pyscreenshot  # Python library for taking screenshots
import pulsectl # Volume control library'
import screen_brightness_control as sbc #Screen brightness controller library
from text_to_speech import speak

# 'Take Screenshot' Command
def take_screenshot():
    #try:
        screenshot = pyscreenshot.grab()
        screenshot.save("/path/to/save/screenshot.png")  # Replace with the desired path
        speak("Screenshot taken and saved.")

# 'Open Camera' Command
def open_camera():
    cap = cv2.VideoCapture(0)  # indicates the default camera (usually the built-in webcam)

    if not cap.isOpened():
        speak("Sorry, I couldn't open the camera.")
        return

    speak("Opening the camera. Press 'Q' to close the camera.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Camera Feed", frame)

        # Check for the 'Q' key to exit the camera feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    speak("Camera is closed.")
    
# Function to get the current volume
def get_current_volume():
    # Initialize the PulseAudio control
    pulse = pulsectl.Pulse('volume-control-script')
    for sink in pulse.sink_list():
        print(f"Sink {sink.index}: {sink.description}, Volume: {round(sink.volume.value_flat * 100)}%")
        
# Function to get the current screen brightness
def get_current_brightness():
    current_brightness = sbc.get_brightness()
    print(f"Current brightness level: {current_brightness}")
