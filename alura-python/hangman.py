import random


def play():
    greeting_message()
    secret_word = load_secret_word()
    right_letters = start_right_letters(secret_word)

    hanged = False
    hit_the_word = False
    errors = 0

    print_hangman(right_letters, errors)
    while not hanged and not hit_the_word:
        shot_letter = input("\nGive me one letter: ")
        shot_letter = shot_letter.strip().upper()

        if shot_letter in secret_word:
            hit_the_mark(secret_word, right_letters, shot_letter)
        else:
            errors += 1

        if errors == 5:
            break
        if " _ " not in right_letters:
            break
        print_hangman(right_letters, errors)

    print_hangman(right_letters, errors)
    finish_game(secret_word, right_letters)


def hit_the_mark(secret_word, right_letters, shot_letter):
    index = 0
    for letter in secret_word:
        if shot_letter == letter:
            right_letters[index] = letter
        index += 1


def finish_game(secret_word, right_letters):
    if " _ " in right_letters:
        print("Well!!! Not today dear, maybe next time!!")
    else:
        print("Congratulations you beat the game!!")
    print(f"\nGame Over (Secret word is: {secret_word})")


def start_right_letters(secret_word):
    right_letters = [" _ " for letter in secret_word]
    return right_letters


def load_secret_word():
    file = open("words.txt", "r")
    words = []
    for line in file:
        words.append(line.strip())
    file.close()

    id = random.randrange(0, len(words))
    secret_word = words[id].upper()
    # print(secret_word)
    return secret_word


def greeting_message():
    print("Welcome to the Hangman Game!")
    print("**********************")


def print_hangman(right_letters, errors):
    if errors == 0:
        print(
            """
            +----+
            |    |
                 |
                 |
                 |
                 |
           =========
            """
        )
    elif errors == 1:
        print(
            """
            +----+
            |    |
            O    |
                 |
                 |
                 |
           =========
            """
        )
    elif errors == 2:
        print(
            """
            +----+
            |    |
            O    |
           /|    |
                 |
                 |
           =========
            """
        )
    elif errors == 3:
        print(
            """
            +----+
            |    |
            O    |
           /|\   |
                 |
                 |
           =========
            """
        )
    elif errors == 4:
        print(
            """
            +----+
            |    |
            O    |
           /|\   |
           /     |
                 |
           =========
            """
        )
    elif errors == 5:
        print(
            """
            +----+
            |    |
           Q/    |
          /|\    |
          / \    |
                 |
          =========
            """
        )
    for letter in right_letters:
        print(f" {letter} ", end="")
    print("")


if __name__ == "__main__":
    play()
