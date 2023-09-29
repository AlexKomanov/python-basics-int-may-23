from quiz_manager import *

wrong_answers_counter = 0

print("Welcome to the Quiz Game!")
print("Answer a question or type 'quit' to exit.")

while wrong_answers_counter < 3:
    question, answer = get_random_question()
    print("\nQuestion", question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == "quit":
        break

    if check_answer(question, user_answer):
        print("Correct! You earned a point.")
        user_score += 1
    else:
        print("Incorrect. The correct answer is:", answer)
        wrong_answers_counter += 1

print("\nThanks for playing!")
print("Your Score:", user_score)
