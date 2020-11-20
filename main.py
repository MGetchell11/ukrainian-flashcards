
import random
from wordDict import words
from sys import exit

ukrainian_word = random.choice(list(words.keys()))

def flash_cards():
    instructions = "INSTRUCTIONS: Type z for random Ukrainian word, x for English translation, q to quit"
    print(instructions + "\n")
    x = ukrainian_word
    print(x + "\n")
    user_input = input("Type z, x, or q\n")
    if user_input == "z":
        print(random.choice(list(words.keys())))
    elif user_input == "x":
        print(dict(words.values(x)))
    elif user_input == "q":
        exit(0)
    else:
        print("Not a valid input, please try again.")
flash_cards()