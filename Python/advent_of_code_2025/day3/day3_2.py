bankList = []
total = 0

with open("banks.txt", "rt") as file:
    bankList = file.read().split("\n")

for bank in bankList:
    joltString = ""
    firstIndex = -1

    for i in range(12):
        
        lastIndex = len(bank) - 11 + i
        jolts = 0

        for x in range(firstIndex + 1, lastIndex):
            if int(bank[x]) > jolts:
                jolts = int(bank[x])
                firstIndex = x

        joltString += str(jolts)
    
    total += int(joltString)


print(total)
        # print(i, bank[len(bank)- 12 + i], len(bank)- 12 + i)