from flask import Flask, render_template, request, jsonify
from ai import take_quiz

app = Flask(__name__)

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