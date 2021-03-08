####################
#### UNFINISHED ####
####################

class Budget:
    def __init__(self, amount):
        self.amount = amount
        
    def transferBudget(self,):
            
def optionSelect():
    print("[1] View Budget")
    print("[2] Transfer Budget")
    print("[3] Quit")
    option = int(input("Choose an option: "))
    return option
    
def viewBudget():
    print(f"Food RM{food.amount}")
    print(f"Leisure RM{leisure.amount}")
    print(f"Clothing RM{clothing.amount}")
    print(f"Stationery RM{stationery.amount}")
    optionSelect()

food = Budget(840)
leisure = Budget(50)
clothing = Budget(60)
stationery = Budget(50)


x = optionSelect()
if x == 1:
    viewBudget()
elif x == 2:
    transferBudget()

# thx @abe#6802
