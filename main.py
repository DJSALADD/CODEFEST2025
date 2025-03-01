from config import *
from google import genai

client = genai.Client(api_key=GEMINI)

chat = client.chats.create(model="gemini-2.0-flash")
chat.send_message("You are a blank model that has no idea what I am talking about unless I taught it to you. Don't answer me unless I explained the topic to you. Act as a student")

user_input = ""

while user_input != "exit":
    user_input = input("User: ")

    response = chat.send_message(user_input)

    print("Response: ", response.text)




