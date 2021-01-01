# This prgram uses random
# to simulate dice rolling

import random

# Defining dice rolling function
def diceroll(s):
    print(random.randint(0,s))


# driver code
s = int(input("Amount of sides: "
))

diceroll(s)
input()