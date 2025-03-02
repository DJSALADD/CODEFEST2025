from flask import Flask, render_template, request, jsonify
from wrapper import take_quiz, chatbox

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # Get JSON data sent by the frontend
    topic = data.get('topic')
    quiz_data = take_quiz(topic)
    return quiz_data

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()  # Get JSON data sent by the frontend
    topic = data.get('topic')
    print(topic)
    message = chatbox(topic)
    print(message)
    return message 

if __name__ == '__main__':
    app.run()