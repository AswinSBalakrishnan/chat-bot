import random

def get_response(user_message):
    # Define rules or templates for generating responses
    greetings = ["Hello!", "Hi there!", "Hey!"]
    how_are_you_responses = ["I'm doing well, thank you!", "I'm fine, thanks for asking."]
    name_responses = ["I'm a chatbot!", "I'm just a humble chatbot."]
    bye_responses = ["Goodbye!", "See you later!", "Bye! Have a great day!"]
    thanks_responses = ["You're welcome!", "No problem!", "My pleasure!"]
    age_responses = ["I don't have an age!", "I'm ageless!", "I exist beyond the concept of time."]
    favorite_color_responses = ["I don't have a favorite color!", "I'm partial to all colors!", "My favorite color is transparent."]

    # Convert user message to lowercase for case-insensitive matching
    user_message = user_message.lower()

    # Check user message against predefined patterns and generate response
    if "hi" in user_message or "hello" in user_message:
        return random.choice(greetings)
    elif "how are you" in user_message:
        return random.choice(how_are_you_responses)
    elif "what's your name" in user_message or "who are you" in user_message:
        return random.choice(name_responses)
    elif "bye" in user_message:
        return random.choice(bye_responses)
    elif "thank you" in user_message or "thanks" in user_message:
        return random.choice(thanks_responses)
    elif "how old are you" in user_message or "what's your age" in user_message:
        return random.choice(age_responses)
    elif "favorite color" in user_message:
        return random.choice(favorite_color_responses)
    else:
        return "I'm not sure how to respond to that."
