bankList = []
bankJoltage = []

with open("banks.txt", "rt") as file:
    bankList = file.read().split("\n")

for bank in bankList:
    temp = []

    for joltage in bank:
        temp.append(int(joltage))

    bank = temp

    firstLargest = {"jolts": 0, "index": 0}
    secondLargest = {"jolts": 0, "index": 1}

    for i in range(len(bank)):
        if bank[i] > firstLargest["jolts"]:
            firstLargest["jolts"] = bank[i]
            firstLargest["index"] = i
            
    for i in range(len(bank)):
        if bank[i] > secondLargest["jolts"] and i > firstLargest["index"]:
            secondLargest["jolts"] = bank[i]
            secondLargest["index"] = i

    if secondLargest["jolts"] == 0:
        for i in range(len(bank)):
            if bank[i] > secondLargest["jolts"] and i != firstLargest["index"]:
                secondLargest["jolts"] = bank[i]
                secondLargest["index"] = i

    if firstLargest["index"] < secondLargest["index"]:
        bankJoltage.append(int(str(firstLargest["jolts"]) + str(secondLargest["jolts"])))

    else:
        bankJoltage.append(int(str(secondLargest["jolts"]) + str(firstLargest["jolts"])))

    print(len(bankJoltage), ": ", bankJoltage[len(bankJoltage) - 1], (firstLargest["jolts"], secondLargest["jolts"]))


total = 0

for joltage in bankJoltage:
    total += joltage

print(total)