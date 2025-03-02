from flask import Flask, render_template, request, jsonify
from ai import take_quiz

from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import threading


app = Flask(__name__)

recognizer = sr.Recognizer()
mic = sr.Microphone()

listening = False  # State control
transcription = ""  # Store transcribed text


def listen():
    """Continuously listen and update transcription."""
    global listening, transcription
    with mic as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Calibration complete! Ready to listen.")

    while listening:
        with mic as source:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
                transcription = recognizer.recognize_google(audio)
                print("Transcribed:", transcription)
            except sr.UnknownValueError:
                transcription = "[Could not understand]"
            except sr.RequestError as e:
                transcription = f"[Error: {e}]"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start_listening", methods=["POST"])
def start_listening():
    global listening
    if not listening:
        listening = True
        thread = threading.Thread(target=listen)
        thread.start()
    return jsonify({"status": "Listening started"})


@app.route("/stop_listening", methods=["POST"])
def stop_listening():
    global listening
    listening = False
    return jsonify({"status": "Listening stopped"})


@app.route("/get_text", methods=["GET"])
def get_text():
    return jsonify({"text": transcription})


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # Get JSON data sent by the frontend
    topic = data.get('topic')
    quiz_data = take_quiz(topic)
    print(quiz_data)
    return quiz_data

if __name__ == '__main__':
    app.run()