import random
from os import system


minimum = 0
maximum = 10

secret_number = random.randint(minimum,maximum)
attemt = 0

user_number = int(input('Enter Number between 0 and 10: '))

while True:
    attemt += 1
    if user_number < secret_number:
        print("May be greater")

    elif user_number > secret_number:
        print("Maybe smaller")

    else:
        print(f"Awesome! You find it in attemt - {attemt}")
        break

    user_number = int(input())
