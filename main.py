from config import *
from google import genai

# Extra keys
client = genai.Client(api_key=GEMINI)
client2 = genai.Client(api_key="AIzaSyBwqN60ljF6pSIO0P7v0GFzeNW_i55YMOE")
chat = client.chats.create(model="gemini-2.0-flash")

initial_subject = input("Please enter the subject you'd like to teach: ").strip()
print(f"Subject set to: {initial_subject}")

while True:
    user_input = input("User: ").strip()

    # Exit
    if user_input.lower() == "exit":
        print("Analyzing your explanations and summarizing key points...")
        
        #Provide gaps and improvements
        summary_prompt = (
            f"Analyze the user's responses during this session on '{initial_subject}'. "
            f"Identify any gaps, misunderstandings, or areas where the user lacked confidence. "
            f"Summarize what was correct and fill in any missing details to strengthen their understanding."
            f"If there is no user response or not sufficient data give a summary of the topic: {user_input}"
            f"When giving a response only output the answer you do not have to reply to this prompt"
        )
        
        summary_response = chat.send_message(summary_prompt)
        print("\nFinal Summary:\n", summary_response.text)
        
        print("Session ended.")
        break

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
