import random

class Individual:
    def __init__(self,
            age: int = 0,
            wallet: int = 0,
            savings: int = 0,
            income: int = 0,
            needs: int = 0,
            wants: int = 0
    ):
        self.age        = age
        self.wallet     = wallet
        self.savings    = savings
        self.income     = income
        self.needs      = needs
        self.wants      = wants
        


    def isDead(self) -> bool:
        # when using this method make sure to roll
        # 12 times before increasing the age by 1
        monthlyDeathPercentage = 0.0006 * 1.0845 ** self.age
        if random.uniform(0, 100) < monthlyDeathPercentage:
            return True
        else:
            return False

class Household:
    def __init__(self, members: list[Individual], savings: int=0):
        self.members = members
        self.savings = savings
        for member in members:
            self.savings += member.savings
            member.savings = 0

# maybe name, fixed/average/variable cost, revenue, profit, etc.
class Firm:
    pass

class Government:
    def __init__(self, budget: int, taxRate: float, interestRate: float):
        self.budget         = budget
        self.taxRate        = taxRate
        self.interestRate   = interestRate
        

a = Individual(savings=100)
b = Individual(savings=150)

print(a.savings, b.savings)
c = Household(members=[a, b])
print(c.members)
print(c.savings)

print(a.savings, b.savings)
