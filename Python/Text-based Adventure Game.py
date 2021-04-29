# import modules
import random

# classes for enemy and player
class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class Player:
    def __init__(self, health, damage, gold, potions):
        self.health = health
        self.damage = damage
        self.gold = gold
        self.potions = potions

# function when killed by enemy
def playerDead():
    pass
# random enemy function
def randomEnemy():
    x = random.randint(1, 3)
    if x == 1:
        y = Enemy("Giant Lizard", 30, 4)
    elif x == 2:
        y = Enemy("Wild Boar", 15, 8)
    elif x == 3:
        y = Enemy("Skeleton", 20, 6)

    # returns value of enemy
    return y

# recieves input from player
def playGame():

    choice = int(input("[1] Explore the jungle\n[2] Find a town\n[3] Stats\n[4] Exit game\n"))
    if choice == 1:
        fightEnemy()

    #elif choice == 2:

    elif choice == 3:
        print(f"Health: {player.health}\nDamage: {player.damage}\nGold: {player.gold}\nPotions: {player.potions}")
        playGame()

    #elif choice == 4:

    #else:
    #    print("Invalid choice")
    #    playGame()

# function for combat
def fightEnemy():
    enemy = randomEnemy()
    print(f"You explore the jungle and you encounter a {enemy.name}")

    while True:
        choice = int(input("[1] Attack\n[2] Items\n[3] Run\n"))
        if choice == 1:
            # deal damage to enemy
            enemy.health = enemy.health - player.damage
            print(f"You attack the {enemy.name} for {player.damage} damage.")

            # check if enemy is dead
            if enemy.health <= 0:
                gold = random.randint(5, 10)
                player.gold = player.gold + gold
                print(f"{enemy.name} has been defeated.")
                print(f"You have earned {gold} gold.")
                playGame()
            
            # deal damage to player
            player.health = player.health - enemy.damage
            print(f"The {enemy.name} attacks you for {enemy.damage} damage.")

            # check if player is dead
            if player.health <= 0:
                print(f"You have been slain by {enemy.name}")
                print("Thanks for playing!")
                input()
                exit()

            # print health of player and enemy
            else:
                print(f"Player health: {player.health}\nEnemy health: {enemy.health}")

        elif choice == 2:
            print(f"You have {player.potions} potions.")
            x = input("Use a potion?(y/n)\n")
            if x == "y" and player.potions >= 1:
                player.potions = player.potions - 1
                player.health = 50

        elif choice == 3:
            playGame()

player = Player(50, 5, 10, 1)

print("Welcome to Py Adventure")
print("A text-based adventure game.")
print("")
print("You wake up in a jungle. You look around with no memory of how you ended up there.")
playGame()

# thx pZouLL#0001 and JellyFishy#7462