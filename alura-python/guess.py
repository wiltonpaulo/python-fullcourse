from random import randint


def play():
    print("Game Guess the Number!")
    print("**********************")

    secret_number = randint(0, 100)
    print(secret_number)
    score = 1000
    level = 0
    # randrange(1, 99)

    print("What difficult level do you want?")
    print("(1) Easy / (2) Medium / (3) Hard")

    while level > 1 or level < 3:
        level = int(input("Choose one number: "))
        if level == 1:
            max_attempt = 20
            print("You choose EASY Level")
            break
        elif level == 2:
            max_attempt = 10
            print("You choose MEDIUM Level")
            break
        elif level == 3:
            max_attempt = 5
            print("You choose HARD Level")
            break
        else:
            print("You have to type 1, 2 or 3")

    attempt = 1
    loose_score = score / max_attempt

    while attempt <= max_attempt:
        user_number = int(
            input(
                f"Please type a number and try to guess", f"({attempt}/{max_attempt}): "
            )
        )
        if user_number == secret_number:
            print(
                f"Awesome!!! you are good at guessing. The secret_number is {secret_number}\n"
            )
            break
        else:
            if user_number > secret_number:
                print("Your number is too HIGH")
            elif user_number < secret_number:
                print("Your number is too LOW")
            attempt = attempt + 1
            score = score - loose_score

    print("**********************")
    if max_attempt <= attempt:
        score = 0
        print("Hahahahahah! You loose!!!")

    print(f"Game Over: the secret_number is: {secret_number}")
    print(f"Score: {score}")


if __name__ == "__main__":
    play()
