# Python program for random
# binary strings generation

# import random for rng
import random

# Defining function
def randombinary(length,lines):

    # Loop for amount of lines
    for x in range(lines):

        # Variable to store random binary
        string = ""

        # Loop for length of string
        for x in range(length):

            # str convert randint into string
            temp = str(random.randint(0,1))
    
             # Making random result into final result
            string += temp

        print (string)

print("This is a random binary string generator.")
print("Please enter the following parameters.")

# Driver code
length = int(input("Length of string: "))
lines = int(input("Amount of lines: "))

randombinary(length,lines)
input()
