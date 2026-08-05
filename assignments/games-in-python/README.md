# 📘 Assignment: Games in Python

## 🎯 Objective

Build a playable Hangman-style word game using core Python concepts. In this assignment, you will practice working with strings, loops, conditionals, and user input while managing game state.

## 📝 Tasks

### 🛠️ Build the Hangman Core Loop

#### Description
Create a program that picks a random word from a predefined list and allows the player to guess one letter at a time.

#### Requirements
Completed program should:

- Store at least 5 possible words in a list.
- Randomly select one word when the game starts.
- Prompt the user to enter a single-letter guess each turn.
- Show the current word progress using underscores for unknown letters (for example: `_ _ a _ _`).

### 🛠️ Add Win and Loss Conditions

#### Description
Expand your game so it tracks incorrect guesses and ends with a clear result message.

#### Requirements
Completed program should:

- Start the player with a fixed number of incorrect attempts (for example: 6).
- Reduce remaining attempts only when a new incorrect letter is guessed.
- End the game with a win message when the word is fully guessed.
- End the game with a loss message when attempts reach 0, and reveal the word.
