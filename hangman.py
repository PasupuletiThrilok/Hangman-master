import random

with open("words.txt", "r") as file:
    words = file.read().splitlines()


def select_word(word_list):
    return random.choice(word_list)


def take_guess(available_letters, secret, lives):
    guess = input("\nGuess a letter: ")
    while not guess.isalpha():
        guess = input("\nYou must guess a letter! \n\nGuess again: ")
    while len(guess) > 1:
        guess = input("\nYou must only guess one letter at a time! \n\nGuess again: ")
    while guess not in available_letters:
        guess = input("\nYou've guessed that letter already! \n\nGuess again: ")
    if guess not in secret.values():
        lives = lives - 1
        if lives > 0:
            print("\nIncorrect guess! You only have " + str(lives) + " lives left!")
            return guess, lives
        else:
            return guess, lives
    else:
        return guess, lives


def get_status(status, secret, current_guess):
    for k, v in zip(secret.keys(), secret.values()):
        if current_guess == v:
            status[k] = v
            print("\nCorrect guess!\n")
    print(''.join(status))
    return status


def track_guesses(current_guess, available_letters):
    available_letters = available_letters.replace(current_guess, '')
    return available_letters


def game():
    secret = select_word(words)
    mydict = {}
    for x in range(len(secret)):
        mydict.update({x: secret[x]})
    secret = mydict
    print(f'\nLet\'s play hangman!\n\nYour word is {str(len(secret))} letters long.')
    status = ['_'] * len(secret)
    print(*status)
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    lives = 5
    while list(status) != list(secret.values()):
        current_guess, lives = take_guess(available_letters, secret, lives)

        status = get_status(status, secret, current_guess)
        available_letters = track_guesses(current_guess, available_letters)
        if status == list(secret.values()):
            print("\nGuess what!\n\nYou win!")
            break
        if lives == 0:
            print("\nYou're out of guesses! You lose!")
            break
        continue


if __name__ == "__main__":
    game()
    while True:
        again = input("\nDo you want to play again? Yes(Y) or No(N)\n")
        while again.lower() not in ["y", "yes", "n", "no"]:
            input("\nPlease input Yes(Y) or No(N): \n")
        if again.lower() == "yes" or again.lower() == "y":
            game()
        else:
            print("\nThanks for playing!")
            break
