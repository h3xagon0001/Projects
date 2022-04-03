import random
import matplotlib.pyplot as plot
import numpy

stockPrice = 600
stockStatus = 1
stockMultiplier = 1
stockTicks = 0
stockArray = []


for x in range(700):
    stockMultiplier = random.randint(1, 10)
    if stockMultiplier <= 1: # 1/10
        stockMultiplier = random.uniform(1, 2) * 3

    elif stockMultiplier <= 2: # 1/10
        stockMultiplier = random.uniform(1, 2) * 2.5

    elif stockMultiplier <= 3: # 1/10
        stockMultiplier = random.uniform(1, 2) * 2

    elif stockMultiplier <= 7: # 3/10
        stockMultiplier = random.uniform(1, 2) * 1.5

    elif stockMultiplier <= 10: # 4/10
        stockMultiplier = random.uniform(1, 2) * 1

    stockTicks = random.randint(1, 2)
    stockStatus = random.uniform(-1, 1.05)

    for y in range(stockTicks):
        stockPrice += stockMultiplier * stockStatus
        stockArray.append(round(stockPrice, 2))


ypoints = numpy.array(stockArray)

plot.plot(ypoints)
plot.title("BC Industries Stock Price", loc="left")
plot.xlabel("Time (Hours)")
plot.ylabel("Price (USD)")
plot.grid()
plot.show()