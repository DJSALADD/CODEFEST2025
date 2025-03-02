from config import *
from google import genai

# Extra keys
client = genai.Client(api_key=GEMINI)
client2 = genai.Client(api_key="AIzaSyBwqN60ljF6pSIO0P7v0GFzeNW_i55YMOE")
chat = client.chats.create(model="gemini-2.0-flash")

#initial_subject = input("Please enter the subject you'd like to teach: ").strip()
#print(f"Subject set to: {initial_subject}")

conversation_history = []

def take_quiz(initial_subject):
    quiz_data = []

    for counter in range(1, 6):
        # Generate a multiple choice question
        question_prompt = f"Create a multiple-choice question (with 4 choices) related to '{initial_subject}'."
        quiz_response = chat.send_message(question_prompt)
        quiz_text = quiz_response.text.strip()

        for choice in ['A)', 'B)', 'C)', 'D)']:
            if choice in quiz_text:
                quiz_text = quiz_text.split(choice)[0].strip()
                break

        choices_prompt = (
            f"Provide four possible answer choices for the question: '{quiz_text}', and indicate the correct answer. "
            "Format:\nA) Choice 1\nB) Choice 2\nC) Choice 3\nD) Choice 4\nCorrect: X (A/B/C/D)"
        )
        choices_response = chat.send_message(choices_prompt)
        choices_lines = choices_response.text.strip().split("\n")

        choices = {}
        correct_answer = None

        for line in choices_lines:
            if line.startswith("A)") or line.startswith("B)") or line.startswith("C)") or line.startswith("D)"):
                choices[line[0]] = line[3:].strip()
            elif line.startswith("Correct:"):
                correct_answer = line.split(":")[1].strip()

        if len(choices) != 4 or correct_answer not in ["A", "B", "C", "D"]:
            continue

        quiz_data.append({
            "question": quiz_text,
            "correct_answer": correct_answer,
            "choices": choices,
        })

    return quiz_data

# Erase when done
def test():
    # Test quiz creation
    test_quiz = take_quiz("math")
    for i, q in enumerate(test_quiz, 1):
        print("Question: ")
        print(f"Q{i}: {q['question']}")

        print("Answer Choices")
        for key, choice in q["choices"].items():
            print(f"   {key}) {choice}")

        print("Correct Answer")
        print(f"   Correct Answer: {q['correct_answer']}")
        print(
        )

def chatbox(message):
    user_prompt = (
        f"You are a curious student eager to learn. The user has provided the following input: '{message}'. "
        f"Ask thoughtful and specific questions to help them explain the concept clearly. "
        f"Ask practical, follow-up questions if their explanations need more depth, assuming a high school level. "
        f"Stay engaged and ask relevant questions about the user's input."
        f"When creating the output just print it as plain text with no bulletin points and bold also create spaces between repsonses"
        f"Also make the response shorter and directly about: {message}"
    )

    chatbot_response = chat.send_message(user_prompt)
    chat_text = chatbot_response.text.strip()
    return {'topic': chat_text}