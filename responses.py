import re
from dattime import datetime,

def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Hey there!'),
        process_message(message, ['bye', 'goodbye'], 'Goodbye!'),
        process_message(message, ['how', 'are', 'you'], 'I\'m doing fine thanks!'),
        process_message(message, ['your', 'name'], 'My name is Mario, nice to meet you!'),
        process_message(message, ['help', 'me'], 'I will do my best to assist you!')
        # Add more responses here
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response

# Test your system
# get_response('What is your name bruv?')
# get_response('Can you help me with something please?')
def input_message(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return "Hey! How's it going?"

    if user_message in ("who are you","who are you?"):
        return "I am Bot"

    if user_message in ("time","time?"):
        now = dattime.now()
        date_time = now.strftime("%d/%m/%y,%H:%M:%S")
        return str(date_time)

    return "no response"
