import guess
import hangman

print(f"*********************************")
print("*** Select one game to play ! ***")
print("*********************************")

print("(1) Hangman!")
print("(2) Guess the Number!")

game = int(input("Which game? "))
if (game == 1):
    print(f"Playing -> Game: Hangman! ...")
    hangman.play()
elif (game == 2):
    print(f"Playing -> Game: Guess the Number! ...")
    guess.play()
