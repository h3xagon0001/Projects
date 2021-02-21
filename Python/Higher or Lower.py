import random

def welcomeMsg():
    print("Welcome to higher or lower. You have to guess if your number is higher or lower then the computer's one. The lowest number is 1 and highest number is 10.")

def highOrLow():
    
    cpu_num = random.randint(1,10)
    player_num = random.randint(1,10)
            
    print(f"Your number: {player_num}")
    guess = (input("Do you think your number is higher or lower than the computer's? ( h / l )\n"))

    if player_num > cpu_num and guess == "h":
        print(f"You are correct. Your number: {player_num} Computer's number: {cpu_num}")
            
    elif player_num < cpu_num and guess == "l":
        print(f"You are correct. Your number: {player_num} Computer's number: {cpu_num}")
            
    else:
        print(f"Your are wrong. Your number: {player_num} Computer's number: {cpu_num}")
            
    def replayGame():
        replay = (input("Do you want to play again? ( y / n )\n"))
        if replay == "y":
            highOrLow()
        else:
            print("Thanks for playing.")
            input()
            
    replayGame()

welcomeMsg()
highOrLow()
