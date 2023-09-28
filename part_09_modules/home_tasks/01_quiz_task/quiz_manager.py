import random
from quiz_questions import *

user_score = 0  # Keeps track of the user's score.


def get_random_question():  # Selects a random question from the question dictionary.
    question, answer = random.choice(list(game_questions.items()))  # ('What is the capital of France?', 'Paris')
    # game_questions.pop(question)
    return question, answer


def check_answer(question, user_answer):  # Checks if the user's answer is correct.
    pass
