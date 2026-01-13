with open("homework.txt", "rt") as file:
    content = file.read().split("\n")

rows = []
for row in content:
    row = row.split(" ")
    temp = []
    for item in row:
        if item != "":
            if item == "+" or item == "*":
                temp.append(item)
            else:
                temp.append(int(item))

    rows.append(temp)
    print(temp)

total = 0

for columnIndex in range(len(rows[0])):
    currentValue = 0
    if rows[len(rows) - 1][columnIndex] == "+":
        currentValue = 0
        for rowIndex in range(len(rows) - 1):
            currentValue += rows[rowIndex][columnIndex]

    if rows[len(rows) - 1][columnIndex] == "*":
        currentValue = 1
        for rowIndex in range(len(rows) - 1):
            currentValue *= rows[rowIndex][columnIndex]

    total += currentValue
    print(currentValue)

print(total)