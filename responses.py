import random

def get_response(message: str) -> str:
    p_message = message.lower()
    phrases = ['kirat bhaiya', 'kirat sir', 'kirat baia', 'kirat bhaaiyaaa']
    for phrase in phrases:
        if phrase in p_message:
            return "Hey there! Let's make things simple and cool, okay? You can just call me Kirat. No need for all those extras. Sounds good?"
 #       return "No issues found in your message. All good!
