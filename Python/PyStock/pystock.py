import random
import matplotlib.pyplot as plt

history = [[],[]]

stockPrice = 100.0

quarterChance = 100.0 / 16
monthChance = 100.0 / 32
dayChance = 100.0 / 64

quarterMult = 0
monthMult = 0
dayMult = 0

upChance = 50.0

random.seed()
graph = plt.plot()

for minute in range(365 * 24 * 60):
    if minute % 131400 == 0:
        quarterMult = random.choice([-1, 1])
    if minute % 43800 == 0:
        monthMult = random.choice([-1, 1])
    if minute % 1440 == 0:
        dayMult = random.choice([-1, 1])
    
    upChance = 50.0

    if quarterMult == 1:
        upChance += quarterChance
    else:
        upChance -= quarterChance

    if monthMult == 1:
        upChance += monthChance
    else:
        upChance -= monthChance

    if dayMult == 1:
        upChance += dayChance
    else:
        upChance -= dayChance


    if random.uniform(0.0, 100.0) < upChance:
        stockPrice += random.uniform(0.0, 1.0)
    else:
        stockPrice -= random.uniform(0.0, 1.0)
        if stockPrice < 0.0:
            stockPrice = 0.0

    history[0].append(minute)
    history[1].append(stockPrice)
    

    """
    print("Quarter: ", quarterMult)
    print("Month: ", monthMult)
    print("Day: ", dayMult)
    print("Up chance: ", upChance)
    print("Stock price: ", stockPrice)
    input()
    """

graph = plt.plot(history[0], history[1], "-g")
plt.show()
      