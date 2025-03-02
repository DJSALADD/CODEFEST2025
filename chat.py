#TODO refactor and split into two function
def init_conversation(initial_subject : str, user_input : str, chat):

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
        return subject_response.text

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
#TODO
def check_subject (initial_subject : str, user_input : str, chat):
    pass

def chat_with_bot(user_input : str, chat) -> str:
    subject_response = chat.send_message(user_input)
    return subject_response.text