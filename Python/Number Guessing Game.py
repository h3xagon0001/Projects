import random

targetNum = random.randint(1,101)
inputNum = 0

print("Let's play a game.")
print("Guess a number between 1 and 100.")

while inputNum != targetNum:

    inputNum = int(input())

    if inputNum > targetNum:
       print("Your number is too big.")
    elif inputNum < targetNum:
       print("Your number is too small.")

print(f"You are correct. The correct number is {targetNum}")