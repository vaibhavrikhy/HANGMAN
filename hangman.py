import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True






def get_guessed_word(secret_word, letters_guessed):
    word_guessed = ''
    for letter in secret_word:
        if letter in letters_guessed:
            word_guessed += letter
        else:
            word_guessed += '_'
    return word_guessed



def get_available_letters(letters_guessed):
    import string
    alpha = string.ascii_lowercase
    temp = ''
    for letter in alpha:
        if letter not in letters_guessed:
            temp += letter
    return temp

    
    

def hangman(secret_word):
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    print("welcome to the game hangman!")
    print(f"im thinking of a word that is {len(secret_word)} letter long.")
    print(f"You have {warnings_left} warnings left.")


    while guesses_left > 0:
         print("_" * 10)
         print(f"you have {guesses_left} guesses left")
         print(f"available letter:{get_available_letters(letters_guessed)}")
         letter = input("please guess a letter: ")
         # letters_guessed.append(letter)
         if not letter.isalpha():
             if warnings_left > 0:
                 warnings_left -= 1
                 print(f"Oops! That is not a valid letter. you have {warnings_left} warnings left: { get_guessed_word(secret_word,letters_guessed)} ")
             else:
                 guesses_left -= 1
                 print(f"Oops! That is not a valid letter. you have {guesses_left} guesses left: { get_guessed_word(secret_word,letters_guessed)}")
         elif letter in letters_guessed:
            if warnings_left > 0:
                warnings_left -= 1
                print(f"Oops! You have already guessed that letter. you have {warnings_left} warnings left: {get_guessed_word(secret_word, letters_guessed)} ")


            else:
                guesses_left -= 1
                print(f"Oops! That is not a valid letter. you have {guesses_left} guesses left: {get_guessed_word(secret_word, letters_guessed)}")
         elif letter in secret_word:
             letters_guessed.append(letter)
             print("Good guess:", get_guessed_word(secret_word, letters_guessed))
         else:
             letters_guessed.append(letter)
             if letter in "aeiou":
                 guesses_left -= 2
             else:
                guesses_left -= 1
             print(f"oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
         if is_word_guessed(secret_word,letters_guessed):
             print("_" * 10)
             print("Congratulations you won!")
             unique_letters = set(secret_word)
             score = guesses_left * len(unique_letters)
             print(f"Your total score for this game is:{score}")
             return
         else: print(f"Sorry, You ran out of guesses. the word is {secret_word}")




def match_with_gaps(my_word, other_word):
    if len(my_word) != len(other_word):
        return False
    for index in range (len(my_word)):
        if my_word[index] == '_':
            continue
        if other_word[index] != my_word[index]:
            return False
    return True



def show_possible_matches(my_word):
    match = []
    for word in wordlist:
        if match_with_gaps(my_word,word):
            match.append(word)
    if match:
        print(' '.join(match))
    else:
        print("No matches found")




def hangman_with_hints(secret_word):
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    print("welcome to the game hangman!")
    print(f"im thinking of a word that is {len(secret_word)} letter long.")
    print(f"You have {warnings_left} warnings left.")

    while guesses_left > 0:
        print("_" * 10)
        print(f"you have {guesses_left} guesses left")
        print(f"available letter:{get_available_letters(letters_guessed)}")
        letter = input("please guess a letter: ")
        if letter == '*':
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))


        elif not letter.isalpha():
            if warnings_left > 0:
                warnings_left -= 1
                print(
                    f"Oops! That is not a valid letter. you have {warnings_left} warnings left: {get_guessed_word(secret_word, letters_guessed)} ")
            else:
                guesses_left -= 1
                print(
                    f"Oops! That is not a valid letter. you have {guesses_left} guesses left: {get_guessed_word(secret_word, letters_guessed)}")
        elif letter in letters_guessed:
            if warnings_left > 0:
                warnings_left -= 1
                print(
                    f"Oops! You have already guessed that letter. you have {warnings_left} warnings left: {get_guessed_word(secret_word, letters_guessed)} ")


            else:
                guesses_left -= 1
                print(
                    f"Oops! That is not a valid letter. you have {guesses_left} guesses left: {get_guessed_word(secret_word, letters_guessed)}")
        elif letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            word_guessed = is_word_guessed(secret_word,letters_guessed)
        else:
            letters_guessed.append(letter)
            if letter in "aeiou":
                guesses_left -= 2
            else:
                guesses_left -= 1
            print(f"oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            if word_guessed:
                break
    # Evaluates whether the user won or lost and prints appropriate message.
    if word_guessed:
        print("Congratulations, you won!")
        score = len(secret_word) * guesses_left
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)




if __name__ == "__main__":

    secret_word = 'tact'
    hangman_with_hints(secret_word)

