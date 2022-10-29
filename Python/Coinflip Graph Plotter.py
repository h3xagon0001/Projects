import matplotlib.pyplot as plt
import numpy as np
import random


coinflipAmount = int(input("Amount of flips: "))

headsAndTails = 0
xarray = []

for x in range(coinflipAmount):
    if random.randint(0, 1) == 1:
        headsAndTails += 1
        xarray.append(headsAndTails)
    
    else:
        headsAndTails -= 1
        xarray.append(headsAndTails)        



xpoints = np.array(range(coinflipAmount))
ypoints = np.array(xarray)






plt.plot(xpoints, ypoints, linewidth="0.75")
plt.show()