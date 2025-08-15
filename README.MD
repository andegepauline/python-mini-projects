# Python Mini Projects Collection for Different Levels

This is a collection of Python mini-projects designed to strengthen my core programming skills in python such as loops, conditionals, functions, error handling, and working with external modules.
Each project is self-contained, runs in the terminal, clearly commented and is explained for easy understanding.


## Table of Contents
1. [Dice Rolling Game](#1-dice-rolling-game)
2. [Number Guessing Game](#2-number-guessing-game)
3.  [Simple Calculator](#3-simple-calculator)
4. [Word Frequency Counter](#4-word-frequency-counter)

---

## 1. Dice Rolling Game
**Description:**  
Simulates rolling two dice (with a configurable number of sides - currently set to 8). The program keeps track of how many times the dice have been rolled and stops when the user chooses to quit.

**Key Features:**
- Random dice rolls using `random.randint()`
- Continuous play until the user enters **'n'**
- Roll count tracking

**Concepts Used:**  
- `random` module for dice rolls  
- Loops (`while True`) for repeated gameplay  
- User input handling  
- Counters for tracking number of rolls 

### How to Run
1. Make sure Python is installed on your machine.

2. Clone the repository:
- git clone https://github.com/andegepauline/python-mini-projects.git

3. Navigate into the folder:
- cd python-mini-projects

4. Run the Python file:
- python dice_rolling_game.py

---

## 2. Number Guessing Game
**Description:**  
This is a fun interactive game where the program picks a random number between 1 and 100, and the player tries to guess it. After each guess, the program tells the player if their guess is too high, too low, or correct. It also tracks how many attempts it takes to guess the number.

**Key Features:**
- Random number generation using `random.randint()`
- Feedback after each guess (too high, too low, correct!)
- Attempt counter to track how many guesses the user made
- Continuous play until the correct number is guessed

**Concepts Used:**
- `random` module for number generation
- Loops (`while True`) for repeated guessing
- Conditional statements (`if, elif, else`) for feedback
- User input handling and type conversion
- Counters to track attempts

### How to Run
1. Make sure Python is installed on your machine.

2. Clone the repository:
- git clone https://github.com/andegepauline/python-mini-projects.git

3. Navigate into the folder:
- cd python-mini-projects

4. Run the Python file:
- python number_guessing_game.py

---

## 3. Simple Calculator
**Description:**
This is a basic calculator program that allows users to perform arithmetic operations (`+`, `-`, `*`, `/`) on two numbers. It runs continuously until the user chooses to exit. The calculator also includes input validation to handle errors such as invalid numbers unsupported operators, or division by zero.

**Key Features**
- Supports **addition, subtraction, multiplication, and division**  
- Continuous use until the user types **'exit'**  
- Handles invalid inputs gracefully  
- Prevents **division by zero**

**Concepts Used**
- Loops (`while True`) for repeated operations  
- Conditional statements (`if/elif/else`) to handle operations  
- Exception handling (`try/except`) for invalid inputs  
- User input handling

### How to Run
1. Make sure Python is installed on your machine.

2. Clone the repository:
- git clone https://github.com/andegepauline/python-mini-projects.git

3. Navigate into the folder:
- cd python-mini-projects

4. Run the Python file:
- python simple_calculator.py

---

## 4. Word Frequency Counter
**Description:**
This program counts how many times each word appears in a given sentence or paragraph.  
It processes the input by **removing punctuation**, **converting text to lowercase**, and then displays word frequencies. It is useful for basic text analysis and understanding how often words are repeated.

**Key Features**
- Removes punctuation automatically  
- Converts all words to lowercase for uniform counting  
- Displays a word frequency dictionary  
- Works with both short sentences and longer paragraphs  

**Concepts Used**
- String manipulation (`lower()`, `translate()`, `split()`) 
- `string` module for punctuation removal
- Dictionary for counting word occurrences  
- Loops (`for`) to process words anf frequency calculation  
- User input handling  

### How to Run
1. Make sure Python is installed on your machine.

2. Clone the repository:
- git clone https://github.com/andegepauline/python-mini-projects.git

3. Navigate into the folder:
- cd python-mini-projects

4. Run the Python file:
- python word_frequency_counter.py

---

## 📌 Future Mini Projects

This collection will grow over time with more small but fun Python projects. Stay tuned!
