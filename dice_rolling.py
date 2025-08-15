import random

SIDES = 8
roll_count = 0

def roll_dice():
    num1 = random.randint(1, SIDES)
    num2 = random.randint(1, SIDES)
    return num1, num2

while True:
    num1, num2 = roll_dice()
    print(f"You rolled: {num1} and {num2}")
    roll_count += 1

    choice = input("Want to roll the dice? y/n ").lower()
    if choice == "n":
        break

print(f"You rolled the dice {roll_count} times. Thanks for playing!")
