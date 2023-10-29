import random

def roll_dice():
    return random.randint(0,6)

while True:
    print("Enter 1 to roll the dice")
    print("Enter 2  to exit the program")
    x = int(input())
    if x == 1:
            result = roll_dice()
            print("You rolled a " + str(result))
    if x == 2:
            print("Thank you! ")
            break
