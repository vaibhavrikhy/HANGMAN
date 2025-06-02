# Hangman Game with Hints

A Python implementation of the classic word-guessing game **Hangman**, with an optional hint feature that shows possible matching words.

## 🎮 Features

- Basic Hangman game logic with word guessing and scoring.
- Hints system: Type `*` to view possible word matches.
- Letter validation and warning system for invalid inputs.
- Vowel penalty for wrong guesses (-2 guesses for vowels, -1 for consonants).
- Keeps track of guessed letters and available letters.
- Score calculated based on remaining guesses and unique letters in the word.

## 📁 Files

- `hangman.py`: Main game logic and functions.
- `words.txt`: Word list file containing valid words used by the game.

## 🚀 How to Run

1. Clone this repository or download the files.
2. Ensure you have Python installed (Python 3.x recommended).
3. Prepare the `words.txt` file with valid words (space-separated).
4. Run the script in your terminal or IDE:

```bash
python hangman.py


🧠 Game Instructions
The game randomly chooses a word from words.txt.

You have 6 guesses to find the word.

Enter a letter to guess it.

Use * to see possible matching words based on your current progress.

Repeated or invalid inputs reduce warnings or guesses.

The game ends when you guess the word or run out of guesses.

🧪 Example
arduino
Copy
Edit
I'm thinking of a word that is 4 letters long.
You have 3 warnings left.
----------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: t
Good guess: t__t


✅ To Do
Add a difficulty level selector.
Improve the hint system to avoid showing words with previously guessed wrong letters.
Add support for uppercase inputs.

# This project is for educational purposes and is freely available to modify and distribute.

