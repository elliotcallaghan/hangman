#compares letters_guessed to secret_word
def is_secret_guessed(secret_word, letters_guessed):
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed and letter == len(secret_word) - 1:
            return True
        elif secret_word[letter] not in letters_guessed:
            return False

#returns word that player has guessed so far
def get_current_guess(secret_word, letters_guessed):
    current_guess = ""

    for letter in secret_word:
        if letter in letters_guessed:
            current_guess += letter
        else:
            current_guess += "_"

    return current_guess

#loops through the first game
def first_game(secret_word):
    letters_guessed = []
    guesses_remaining = 11

    print("The secret word has " + str(len(secret_word)) + " characters.")
    print("You have " + str(guesses_remaining) + " guesses.")

    while guesses_remaining > 0:
        letters_guessed.append(input("Guess a character in the secret word: "))
        print("The partially guessed word is " + get_current_guess(secret_word, letters_guessed))

        if is_secret_guessed(secret_word, letters_guessed) == True:
            print("It's a win!")
            break
        else:
            guesses_remaining -= 1
            print("You have " + str(guesses_remaining) + " guesses remaining")

secret_word = "emmanuel"
first_game(secret_word)