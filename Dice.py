

import random

print("Dice Roller Simulator")

while True:
    roll = input("Press Enter to roll the dice or 'q' to quit: ")
    if roll.lower() == 'q':
        print("Exiting Dice Roller.")
        break
    dice = random.randint(1, 6)
    print(f"You rolled: {dice}\n")
