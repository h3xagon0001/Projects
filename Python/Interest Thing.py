import time
import os

money = 1000
lastGain = 0

print(money)

while True:
	gain = money * 0.05
	money += gain
	difference = gain - lastGain
	
	os.system("cls")

	print(f"Money: {money}")
	print(f"Gain: {gain}")
	print(f"Difference: {difference}")
	
	lastGain = gain

	with open("data.txt", "w") as file:
		file.write("Money: " + str(money) + "\n" + "Gain: " + str(gain) + "\n" + "Difference: " + str(difference))

	time.sleep(0.1)
