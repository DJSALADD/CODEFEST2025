from config import *
from google import genai
import json

# Extra keys
client = genai.Client(api_key=GEMINI)
client2 = genai.Client(api_key="AIzaSyBwqN60ljF6pSIO0P7v0GFzeNW_i55YMOE")
chat = client.chats.create(model="gemini-2.0-flash")

initial_subject = input("Please enter the subject you'd like to teach: ").strip()
print(f"Subject set to: {initial_subject}")

conversation_history = []

def take_quiz(initial_subject):
    counter = 1
    answers = {}
    correct_answers = []
    quiz_data = []

    while counter <= 5:
        question_prompt = f"Create a multiple-choice question (with 4 choices) related to '{initial_subject}' based on the following conversation: {conversation_history}"
        quiz_response = chat.send_message(question_prompt)
        
        quiz_text = quiz_response.text.strip()
        print(f"Question {counter}: {quiz_text}")
        
        answer = input("Your Answer (A, B, C, or D): ").strip().upper()
        
        while answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input! Please enter A, B, C, or D.")
            answer = input("Your Answer (A, B, C, or D): ").strip().upper()
        
        answers[counter] = answer
        
        grading_prompt = (
            f"Here is the user's answer for question {counter}:\n"
            f"Question: {quiz_text}\n"
            f"User Answer: {answer}\n"
            f"Please grade the answer and provide feedback, including whether the answer is correct or incorrect."
        )
        
        grading_response = chat.send_message(grading_prompt)
        print(grading_response.text)
        
        is_correct = "correct answer" in grading_response.text.lower()
        
        # Store quiz data in dictionary
        quiz_data.append({
            "question": quiz_text,
            "user_answer": answer,
            "feedback": grading_response.text,
            "correct": is_correct
        })
        
        if is_correct:
            correct_answers.append(answer)
        
        counter += 1

    score_prompt = (
        f"Here are the user's answers: {answers}\n"
        f"These were the correct answers: {correct_answers}\n"
        f"Please calculate the score based on the user's answers and the correct answers. "
        f"Each correct answer is worth 1 point. Return the percentage score."
    )

    score_response = chat.send_message(score_prompt)
    
    # Return to dictionary
    return {
        "quiz_data": quiz_data,
        "score_feedback": score_response.text
    }

while True:
    user_input = input("User: ").strip()

    # Exit
    if user_input.lower() == "exit":
        print("Analyzing your explanations and summarizing key points...")

        summary_prompt = (
            f"Analyze the user's responses during this session on '{initial_subject}'. "
            f"Identify any gaps, misunderstandings, or areas where the user lacked confidence. "
            f"Summarize what was correct and fill in any missing details to strengthen their understanding."
            f"If there is no user response or not sufficient data give a summary of the topic: {user_input}."
        )

        summary_response = chat.send_message(summary_prompt)
        print("\nFinal Summary:\n", summary_response.text)       
        print("Generating a quiz based on your discussion...\n")

        # Take the Quiz and get the quiz data as a dictionary
        quiz_results = take_quiz(initial_subject)

        # Print score
        print("\nQuiz Results:")
        print(quiz_results["score_feedback"])

        print("Session ended.")
        break

    # Add the user input to history
    conversation_history.append(user_input)

    # If input is related to the initial subject
    subject_check_prompt = (
        f"Reply in the format 'yes' or 'no; [subject]'. "
        f"Is the following input related to the subject '{initial_subject}'? "
        f"If yes, respond with 'yes'. "
        f"If no, determine the most relevant subject and respond in the format 'no; [subject]'.\n\n"
        f"Input: {user_input}"
    )

    subject_response = chat.send_message(subject_check_prompt)
    subject_response_text = subject_response.text.strip().lower()

    # Handle responses if user input matches subject
    if subject_response_text == "yes":
        # Train the AI
        student_prompt = (
            f"You are a curious student eager to learn. The user is someone applying their knowledge on '{initial_subject}'. "
            f"Ask thoughtful and specific questions to help them explain concepts clearly. "
            f"Ask practical, follow-up questions if their explanations need more depth, assuming a high school level. "
            f"At the end, analyze their responses, identify gaps, and summarize missing details where they lacked confidence. "
            f"Stay engaged and ask relevant questions about the user's input: {user_input}."
        )
        
        student_response = chat.send_message(student_prompt)
        print("AI Student: ", student_response.text)

    # User input not related to inital subject
    elif subject_response_text.startswith("no;"):
        _, suggested_subject = subject_response_text.split(";", 1)
        suggested_subject = suggested_subject.strip()

        confirm_change = input(
            f"It looks like your input is related to '{suggested_subject}' instead of '{initial_subject}'. "
            f"Do you want to switch subjects? (yes/no): "
        ).strip().lower()

        if confirm_change == "yes":
            initial_subject = suggested_subject
            print(f"Subject changed to: {initial_subject}")
        else:
            print(f"Continuing with the current subject: {initial_subject}")

    else:
        print("Unexpected response from API. Please try again.")