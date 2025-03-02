from config import *
from google import genai

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
    correct_answers = {}
    quiz_data = []

    while counter <= 5:
        # Generate a multiple choice question
        question_prompt = f"Create a multiple-choice question (with 4 choices) related to '{initial_subject}' based on the following conversation: {conversation_history}"
        quiz_response = chat.send_message(question_prompt)
        quiz_text = quiz_response.text.strip()

        # Generate answer choices with the correct answer
        choices_prompt = f"Provide four possible answer choices for the question: '{quiz_text}', and indicate the correct answer. Format:\nA) Choice 1\nB) Choice 2\nC) Choice 3\nD) Choice 4\nCorrect: X (A/B/C/D)"
        choices_response = chat.send_message(choices_prompt)
        choices_lines = choices_response.text.strip().split("\n")

        choices = {}
        correct_answer = None

        for line in choices_lines:
            if line.startswith("A)"):
                choices["A"] = line[3:].strip()
            elif line.startswith("B)"):
                choices["B"] = line[3:].strip()
            elif line.startswith("C)"):
                choices["C"] = line[3:].strip()
            elif line.startswith("D)"):
                choices["D"] = line[3:].strip()
            elif line.startswith("Correct:"):
                correct_answer = line.split(":")[1].strip()

        if len(choices) != 4 or correct_answer not in ["A", "B", "C", "D"]:
            print("Error generating choices. Retrying...")
            continue

        # Display question and choices
        print(f"\nQuestion {counter}: {quiz_text}")

        # Get user input
        answer = input("Your Answer (A, B, C, or D): ").strip().upper()
        while answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input! Please enter A, B, C, or D.")
            answer = input("Your Answer (A, B, C, or D): ").strip().upper()

        # Store user answer and correct answer
        answers[counter] = answer
        correct_answers[counter] = correct_answer

        # Grade the response
        is_correct = answer == correct_answer
        feedback = "Correct!" if is_correct else f"Incorrect. The correct answer was {correct_answer}) {choices[correct_answer]}."

        # Store quiz data
        quiz_data.append({
            "question": quiz_text,
            "user_answer": answer,
            "correct_answer": correct_answer,
            "choices": choices,
            "is_correct": is_correct,
            "feedback": feedback
        })

        counter += 1

    # Calculate score
    score = sum(1 for q in answers if answers[q] == correct_answers[q])
    total_questions = len(correct_answers)
    percentage_score = (score / total_questions) * 100

    # Return the results as a dictionary
    return {
        "quiz_data": quiz_data,
        "score": f"You got {score}/{total_questions} correct ({percentage_score:.2f}%).",
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
        print(quiz_results["score"])

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