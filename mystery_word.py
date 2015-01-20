import random
import re

with open("/usr/share/dict/words") as w:
    word_list = w.readlines()

guessed = []
revealed = []


def random_word_assignment():
    global random_word
    random_word = random.choice(word_list).strip().lower()
    return random_word


def game_intro(random_word):
    print_statement = "The word has {} letters. You have 8 guesses.".format(
        len(random_word), counter)
    print(print_statement)
    return print_statement


def change_count_guess(counter):
    counter -= 1
    guessed.append(guess)
    print(counter_statement)
    return counter


# def display_counter():
#     print(counter_statement)


def correct_guess(guess, revealed):
    revealed.append(guess)
    print("Good job! " + counter_statement)
    return revealed


def incorrect_guess(guess, counter):
    counter -= 1
    guessed.append(guess)
    print("Nope. " + counter_statement)
    return guessed


def display_correct_guesses(guess):
    print(" ".join(char if char in revealed else "_" for char in random_word))
    return (" ".join(char if char in revealed else "_" for char
            in random_word))


def get_guess():
    guess = input("What's your guess?  ").lower()
    if guess in re.search[a-z]:
        return str(guess)
        print(guess)
    else:
        print("{} is not a valid choice. Try again.".format(guess))


def guess_list():
    print(guessed)
    return guessed


# def game_over():
#     game_over = "The word was {}."format(random_word)
#     print(game_over)



counter = 8
game_intro(random_word_assignment())

while True:
    while counter > 0 and len(random_word) != len(revealed):
        guess = input("What's your guess?  ")
        counter_statement = "You have {} guesses left. '\n'".format(counter)
        if len(guess) > 1:
            guess = input("You can only guess one letter at a time. ")
        elif guess in random_word:
            correct_guess(guess, revealed)
            display_correct_guesses(guess)
        elif guess not in random_word:
            counter -= 1
            incorrect_guess(guess, counter)
            display_correct_guesses(guess)
            print(guessed)
        else:
            print("You have run out of guesses. The word is {}.".
                  format(random_word))
            break

    else:
        if len(random_word) == len(revealed):
            print("You won!")
            break
        else:
            break

# Still accepts non-letters as correct. Replay function not working.
