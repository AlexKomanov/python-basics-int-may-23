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

The game logic is implemented in the `quiz_manager.py` file. It contains functions for selecting random questions, checking answers, and maintaining the user's score.

### Functions

- `get_random_question()`: Selects a random question from the question dictionary.
- `check_answer(question, user_answer)`: Checks if the user's answer is correct.
- `user_score`: Keeps track of the user's score.

## Playing the Game (main.py)

To play the game, run the `main.py` script.

### Instructions

1. The game will welcome you and present a random question.
2. Answer the question or type 'quit' to exit the game.
3. Your score will be displayed after each answer.
4. Keep answering questions and accumulating points.
5. Enjoy the game!

## How to Run

1. Open your terminal.
2. Navigate to the directory containing these files.
3. Run `python main.py` to start the game.

Have fun and test your knowledge!
