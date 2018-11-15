import random
import sys

#global variables used in game_stats function
num_games = 1
wins = 0
losses = 0

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
    global wins
    global losses
    secret_word = secret_word.strip().lower()
    letters_guessed = []
    guesses_remaining = 10
    previous_guess = "_" * len(secret_word)

    print("The secret word has " + str(len(secret_word)) + " characters.")
    print("You have " + str(guesses_remaining) + " guesses.")

    #ensures there are a finite number of guesses
    while guesses_remaining > 0:
        while True:
            letter = input("Guess a character in the secret word: ").lower()
            if letter.isalpha() and len(letter) == 1:
                break
            else:
                print("Input must be one letter")

        letters_guessed.append(letter)
        current_guess = get_current_guess(secret_word, letters_guessed)
        print("The partially guessed word is", current_guess)

        if is_secret_guessed(secret_word, letters_guessed) == True:
            print("It's a win!")
            wins += 1
            guesses_remaining = 0
        else:
            if current_guess == previous_guess:
                guesses_remaining -= 1
                print("You have " + str(guesses_remaining) + " guesses remaining")

        previous_guess = current_guess
    else:
        print("The word was", secret_word)
        if secret_word != previous_guess:
            losses += 1


#loads file and puts words into list
def load_words(file_name):
    #checking that the file exists
    try:
        file = open(file_name, "r")
    except:
        print("Please download the text file 'words.txt' and store in same location as the python file to continue playing hangman.")
        #program terminates if the file does not exist
        sys.exit()
    else:
        words = []
        for word in file:
            words.append(word)
        return (words, len(words))

#chooses a random word from list
def choose_secret_word():
    words = load_words("words.txt")
    return words[0][random.randint(0, words[1] - 1)]

#loads first game but with random word
def second_game():
    global num_games
    #allows user to continue or quit
    quit = input("Press c to continue or q to quit: ").lower()
    if (quit == "q"):
        stats = game_stats(num_games)
        print("Wins: " + str(stats[0]) + "\nLosses: " + str(stats[1]) + "\n" + stats[2])
    elif (quit == "c"):
        num_games += 1
        first_game(choose_secret_word())
        second_game()
    else:
        #if user does not choose 'c' or 'q' then this function will be called again to ask the same question
        second_game()

#takes in number of games and returns win/loss frequencies and average
def game_stats(num_games):
    average = "The average win percentage is " + str(float(wins / num_games) * 100) + "%"
    return (wins, losses, average)

#starts the first game with the word being 'Emmanuel'
first_game("Emmanuel")
second_game()
