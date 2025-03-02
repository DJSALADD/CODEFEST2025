mood_table = {"Neutral" : 1, "Confused" : 2, "Curious" : 3,"Happy" : 4 }

def get_mood(chat) -> int:
    mood = chat.send_message("How do you feel about information that I provided? Only for this time say one word Neutral/Confused(provided information is wrong)/Curious(you think I need provide more information)/Happy(everything is perfect)")
    return mood_table.get(mood.text)