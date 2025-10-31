import random

class Person:
    def __init__(self, age: int):
        self.age = age

    def isDead(self) -> bool:
        # when using this method make sure to roll
        # 12 times before increasing the age by 1
        monthlyDeathPercentage = 0.0006 * 1.0845 ** self.age
        if random.uniform(0, 100) < monthlyDeathPercentage:
            return True
        else:
            return False

class Household:
    def __init__(self):
        pass