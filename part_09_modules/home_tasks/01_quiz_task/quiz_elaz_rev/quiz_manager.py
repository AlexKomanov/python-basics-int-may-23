from quiz_questions import game_questions as questions
import random
import os
import time

ROUNDS = 5
q_list = list(questions.items())
right_ans = 0
wrong_ans = 0


def get_random_question():
    rand_question = random.choice(q_list)
    q, a = rand_question
    q_list.remove(rand_question)
    return q, a


def check_answer(a: str, user_input: str):
    return user_input.lower() == a.lower()


def run():
  
    for round in range(len(q_list)):
        global right_ans
        global wrong_ans

        question = get_random_question()
        print(f'{question[0]}: ')
        user_input = input()
        if user_input == '':
            break

        if check_answer(question[1], user_input):
            right_ans += 1
        else:
            wrong_ans += 1

        if check_answer(question[1], user_input):
            print("Correct!")
        else:
            print(f'{check_answer(question[1], user_input)} => {question[1]}')

        time.sleep(1.3)
        os.system('cls')

    print(f"You'v answered right on {right_ans} questions\nand wrong on {wrong_ans}...")


if __name__ == "__main__":
    run()

