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
def first_game(secret_word = "Emmanuel"):
    secret_word = secret_word.lower()
    letters_guessed = []
    guesses_remaining = 5
    previous_guess = "_" * len(secret_word)

    print("The secret word has " + str(len(secret_word)) + " characters.")
    print("You have " + str(guesses_remaining) + " guesses.")

    while guesses_remaining > 0:
        letters_guessed.append(input("Guess a character in the secret word: ").lower())
        current_guess = get_current_guess(secret_word, letters_guessed)
        print("The partially guessed word is", current_guess)

        if is_secret_guessed(secret_word, letters_guessed) == True:
            print("It's a win!")
            break
        else:
            if current_guess == previous_guess:
                guesses_remaining -= 1
                print("You have " + str(guesses_remaining) + " guesses remaining")
                
        previous_guess = current_guess
    else:
        print("The word was", secret_word)

#loads file and puts words into list
def load_words(file_name):
    file = open(file_name, "r")
    words = []
    
    for word in file:
        words.append(word)

    return (words, len(words))

#chooses a random word from list
def choose_secret_word():
    import random
    words = load_words("words.txt")
    return words[0][random.randint(0, words[1] - 1)]

#loads first game but with random word
def second_game():
    first_game(choose_secret_word())

first_game()
second_game()