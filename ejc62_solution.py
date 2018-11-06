import random

num_games = 1
wins = 0
losses = 0
results = [["Wins: ", "0"], ["Losses: ", "0"]]

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
    global results
    global losses
    print(secret_word)
    secret_word = secret_word.strip().lower()
    letters_guessed = []
    guesses_remaining = 10
    previous_guess = "_" * len(secret_word)

    print("The secret word has " + str(len(secret_word)) + " characters.")
    print("You have " + str(guesses_remaining) + " guesses.")

    while guesses_remaining > 0:
        letters_guessed.append(input("Guess a character in the secret word: ").lower())
        current_guess = get_current_guess(secret_word, letters_guessed)
        print("The partially guessed word is", current_guess)

        if is_secret_guessed(secret_word, letters_guessed) == True:
            print("It's a win!")
            
            wins += 1
            results[0][1] = wins
            
            guesses_remaining = 0
        else:
            if current_guess == previous_guess:
                guesses_remaining -= 1
                print("You have " + str(guesses_remaining) + " guesses remaining")
                
        previous_guess = current_guess
    else:
        print("The word was", secret_word)
        if(secret_word != previous_guess):
            losses += 1
            results[1][1] = losses
        

#loads file and puts words into list
def load_words(file_name):
    file = open(file_name, "r")
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
    quit = input("Press c to continue or q to quit: ")
    if (quit.lower() == "q"):
        res, av = game_stats(num_games)
        return (res, av)
    elif (quit.lower() == "c"):
        num_games += 1
        first_game(choose_secret_word())
        second_game()
    else:
        second_game()

def game_stats(num_games):
    global results
    global wins
    global losses
    average = "The average win percentage is " + str(float(wins / num_games) * 100) + "%"
    return (results, average)

first_game("Emmanuel")
second_game()
