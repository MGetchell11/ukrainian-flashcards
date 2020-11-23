
import random
from wordDict import words

def flash_cards():
    instructions = "INSTRUCTIONS: Type z for random Ukrainian word, x for English translation, q to quit"
    print(instructions + "\n")
    while True:
        user_input = input("Type z, x, or q\n")
        if user_input == "z":
            z = random.choice(list(words.keys()))
            print(z + "\n")
        elif user_input == "x":
            x = words.get(z)
            print(z + " = " + x + "\n")
            return flash_cards()
        elif user_input == "q":
            break
        else:
            print("Not a valid input, please try again.\n")
            return flash_cards()
flash_cards()