import random


def play():
    file = open("words.txt", "r")
    words = []
    for line in file:
        words.append(line.strip())
    file.close()

    id = random.randrange(0, len(words))
    secret_word = words[id].upper()
    print(secret_word)

    print("Welcome to the Hangman Game!")
    print("**********************")

    right_letters = [" _ " for letter in secret_word]
    hanged = False
    hit_the_word = False
    errors = 0

    while not hanged and not hit_the_word:
        shot_letter = input("Give me one letter: ")
        shot_letter = shot_letter.strip().upper()

#        print(shot_letter, secret_word)
        if shot_letter in secret_word:
            index = 0
            for letter in secret_word:
                if shot_letter == letter:
                    right_letters[index] = letter
                index += 1
        else:
            errors += 1

        if errors == 5:
            break
        if " _ " not in right_letters:
            break
        print(right_letters)

    if " _ " in right_letters:
        print("Well!!! Not today dear, maybe next time!!")
    else:
        print("Congratulations you beat the game!!")
    print(f"\nGame Over")


if (__name__ == "__main__"):
    play()
