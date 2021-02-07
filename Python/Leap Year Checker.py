def leapYearCheck():
    loop = "y"
    while loop == "y":

        year = int(input("What year do you want to check?\n"))

        if year % 4 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
        
        loop = str(input("Do you want to check another year?( y / n )\n"))

leapYearCheck()
