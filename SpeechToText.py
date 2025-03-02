import speech_recognition as sr
import keyboard
import sys

# Initialize the recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Instructions
print("Press 'spacebar' to start/stop listening. Press 'q' to quit.")

listening = False  # Toggle state

def toggle_listen():
    """Toggles the listening state."""
    global listening
    listening = not listening
    if listening:
        print("\nListening... (Press spacebar to stop)")
    else:
        print("\nStopped listening.")

# Bind spacebar to toggle listening
keyboard.add_hotkey("space", toggle_listen)

with mic as source:
    print("\nCalibrating microphone for background noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=2)  # Adaptive noise reduction
    print("Calibration complete! Ready to listen.")

while True:
    if listening:
        with mic as source:
            try:
                print("\nSay something...")  # Indicate when listening starts
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)  # Unlimited listening
                
                text = recognizer.recognize_google(audio)  # Convert speech to text
                
                # Dynamically update the output in real-time
                sys.stdout.write("\r" + text + " " * 10)  # Overwrite previous text
                sys.stdout.flush()
                
            except sr.UnknownValueError:
                sys.stdout.write("\r[Could not understand]      ")
                sys.stdout.flush()
            except sr.RequestError as e:
                sys.stdout.write(f"\r[Error: {e}]      ")
                sys.stdout.flush()

    if keyboard.is_pressed("q"):  # Quit when 'q' is pressed
        print("\nExiting program...")
        break