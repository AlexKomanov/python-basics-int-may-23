# Python Quiz Game

This is a simple Python quiz game where players can answer questions and earn points.

## Quiz Questions

The quiz questions and answers are stored in the `quiz_questions.py` file as a dictionary. You can add or modify questions in this file.

### Sample Questions

- What is the capital of France?  
  - Answer: Paris

- Which planet is known as the Red Planet?  
  - Answer: Mars

- What is the largest mammal in the world?  
  - Answer: Blue whale

- What is the chemical symbol for gold?  
  - Answer: Au

- Who wrote the play 'Romeo and Juliet'?  
  - Answer: William Shakespeare

- What is the largest organ in the human body?  
  - Answer: Skin

- How many continents are there on Earth?  
  - Answer: 7

- Which gas do plants absorb from the atmosphere during photosynthesis?  
  - Answer: Carbon dioxide

- Who painted the Mona Lisa?  
  - Answer: Leonardo da Vinci

- What is the smallest prime number?  
  - Answer: 2

## Game Logic (quiz_manager.py)

The game logic is implemented in the `quiz_manager.py` file. 
It contains functions for selecting random questions, checking answers, and maintaining the user's score.

**1. Import Required Modules:**

The code begins by importing two modules: `random` and `quiz_questions`. 
The `random` module is used for generating random questions, and `quiz_questions` contains a dictionary of quiz 
questions and answers.

**2. Initialize User's Score:**

The variable `user_score` is initialized to `0`. This variable will be used to keep track of the user's score as they answer questions correctly.

**3. Define get_random_question() function:**

The `get_random_question()` is a function that selects a random question from the `quiz_questions` module. 
Here's what this function does:
- It uses `random.choice()` to select a random question-answer pair from the `quiz_questions.game_questions` dictionary.
- It returns both the selected question and its corresponding answer as a tuple.
- **(Optional):** Define a return type as `-> Tuple[str, str]`. It will require the following import:`from typing import Tuple`

**4. Define check_answer() function:**

The `check_answer(question, user_answer)` is a function that checks whether the user's answer matches the correct 
answer for a given question. Here's what this function does:
- It takes two parameters: `question` (the question text) and `user_answer` (the user's answer).
- It retrieves the correct answer for the given question from `quiz_questions.game_questions` using `quiz_questions.game_questions.get(question)`.
- It performs a case-insensitive comparison between the `user_answer` and the correct answer by converting both to lowercase.
- It returns `True` if the user's answer is correct and `False` otherwise.

### Game Flow (main.py):

1. **Import Functions and Variables from `quiz_manager`**:
   - The code uses `from quiz_manager import *` to import all functions and variables from the `quiz_manager` module. This allows you to use functions like `get_random_question()` and `check_answer()` as well as the `user_score` variable without specifying the module name.

2. **Initialize `wrong_answers_counter`**:
   - The variable `wrong_answers_counter` is initialized to 0. This variable will be used to keep track of how many consecutive wrong answers the user has given.

3. **Welcome Message**:
   - The code displays a welcome message to the user with instructions on how to play the quiz.

4. **Main Game Loop**:
   - The code enters a `while` loop, which will continue running until either the user decides to quit by typing "quit" or the user gives three consecutive wrong answers.

5. **Get a Random Question**:
   - Inside the loop, it uses `get_random_question()` to retrieve a random question and its corresponding answer. This question is stored in the `question` variable, and the answer is stored in the `answer` variable.

6. **Display the Question and Get User's Answer**:
   - It prints the question to the screen using `print("\nQuestion", question)`.
   - It prompts the user for their answer using `user_answer = input("Your answer: ")`.

7. **Check for Quit Command**:
   - It checks if the user's input is "quit" (case-insensitive). If the user wants to quit, the loop breaks, and the game ends.

8. **Check User's Answer**:
   - If the user's answer is not "quit," it proceeds to check if the answer is correct using `check_answer(question, user_answer)`.
   - If the answer is correct, it informs the user that they earned a point and updates the `user_score`.
   - If the answer is incorrect, it provides the correct answer to the user and increments the `wrong_answers_counter`.

9. **End of Game**:
   - The loop continues until either the user decides to quit or until `wrong_answers_counter` reaches 3 (indicating three consecutive wrong answers).
   - After exiting the loop, the code displays a "Thanks for playing!" message along with the user's final score.


## Playing the Game (main.py)
1. To play the game, run the `main.py` inside your IDE.
2. Enjoy the game!


## How to Run with a terminal
1. Open your terminal.
2. Navigate to the directory containing these files.
3. Run `python main.py` to start the game.
4. Enjoy the game!


