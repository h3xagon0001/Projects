import random

class Individual:
    def __init__(self,
            age: int = 0,
            wallet: int = 0,
            savings: int = 0,
            income: int = 0,
            needs: int = 0,
            wants: int = 0,
            inHousehold: bool = False
    ):
        self.age        = age
        self.wallet     = wallet
        self.savings    = savings
        self.income     = income
        self.needs      = needs
        self.wants      = wants
        self.inHousehold= False
        


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

def getMonthlyHouseholdPercentage(individualOne: Individual, individualTwo: Individual):
    # try to only change the coefficient
    coefficient = 0.05
    target = 45
    return coefficient * (individualOne.income + individualTwo.income) ** (1 / 2.5) - 0.075 * abs(target - (individualOne.age + individualTwo.age) / 2)

def formHousehold(population: list[Individual], individual: Individual):
    # check is they have a job or already in household or below 18
    if individual.income == 0 or individual.inHousehold or individual.age < 18:
        return None

    candidate = random.choice(population)

    # check if self
    # check if they have a job
    # check if they are in a household
    # check if they are 18
    if (
        candidate == individual or
        candidate.income == 0 or
        candidate.inHousehold or
        candidate.age < 18
    ):
        return None

    if random.uniform(0, 100) < getMonthlyHouseholdPercentage(individual, candidate):
        return candidate

    else:
        return None

population: list[Individual] = []

for i in range(1000):
    population.append(Individual(age=random.randint(0,10), income = round(random.triangular(1700, 4000))))

householdFormed = 0
formingAge = 0

for year in range(100):
    for month in range(12):
        if len(population) == 0: break

        for individual in population:
            candidate = formHousehold(population, individual)
            if candidate != None:
                a = Household([individual, candidate])
                print(a.members, individual.age, candidate.age)
                individual.inHousehold = True
                candidate.inHousehold = True
                
                householdFormed += 1
                formingAge += individual.age
                formingAge += candidate.age

            if individual.isDead():
                population.remove(individual)
                
    for individual in population:
        individual.age += 1

print("Households formed: ", householdFormed)
print("Average forming age: ", formingAge / (householdFormed * 2))