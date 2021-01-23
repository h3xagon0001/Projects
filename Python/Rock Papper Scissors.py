def rpsGame():
    # modules
    import random

    # varibles
    computerChoice = ""
    playerChoice = ""
    replayGame = "yes"

    # loop game
    while replayGame == "yes":
        # player's choice
        playerChoice = input("What is your choice? [ rock / paper / scissors ]\n")

        # computer's choice
        computerChoice = random.randrange(3)
        if computerChoice == 0:
            computerChoice = "rock"
        elif computerChoice == 1:
            computerChoice = "paper"
        else:
            computerChoice = "scissors"

        # find out who won
        if playerChoice == computerChoice:
            print("Tie!")

        elif playerChoice == "rock":
            if computerChoice == "scissors":
                print(f"You win! {playerChoice} beats {computerChoice}")
            else:
                print(f"You lose :( {computerChoice} beats {playerChoice}")

        elif playerChoice == "paper":
            if computerChoice == "rock":
                print(f"You win! {playerChoice} beats {computerChoice}")
            else:
                print(f"You lose :( {computerChoice} beats {playerChoice}")

        elif playerChoice == "scissors":
            if computerChoice == "paper":
                print(f"You win! {playerChoice} beats {computerChoice}")
            else:
                print(f"You lose :( {computerChoice} beats {playerChoice}")

        replayGame = input("Do you want to play again? [ yes / no ]\n")
    print("Thanks for playing")
    input()
rpsGame()