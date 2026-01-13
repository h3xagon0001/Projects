shelves: list[list[str]] = []
counter = 0
removed = True

with open("shelves.txt", "rt") as file:
    temp = file.read().split("\n")

for row in temp:
    shelves.append(list(row))

while removed:
    removed = False
    for rowIndex in range(len(shelves)):
        for columnIndex in range(len(shelves[rowIndex])):
            if shelves[rowIndex][columnIndex] == "@":
                rollCount = 0

                # top
                if rowIndex > 0:
                    if shelves[rowIndex - 1][columnIndex] in ["@", "x"]:
                        rollCount += 1

                # bottom
                if rowIndex < len(shelves) - 1:
                    if shelves[rowIndex + 1][columnIndex] in ["@", "x"]:
                        rollCount += 1

                # left
                if columnIndex > 0:
                    if shelves[rowIndex][columnIndex - 1] in ["@", "x"]:
                        rollCount += 1

                # right
                if columnIndex < len(shelves[rowIndex]) - 1:
                    if shelves[rowIndex][columnIndex + 1] in ["@", "x"]:
                        rollCount += 1

                # top left
                if rowIndex > 0 and columnIndex > 0:
                    if shelves[rowIndex - 1][columnIndex - 1] in ["@", "x"]:
                        rollCount += 1

                # top right
                if rowIndex > 0 and columnIndex < len(shelves[rowIndex]) - 1:
                    if shelves[rowIndex - 1][columnIndex + 1] in ["@", "x"]:
                        rollCount += 1

                # bottom left
                if rowIndex < len(shelves) - 1 and columnIndex > 0:
                    if shelves[rowIndex + 1][columnIndex - 1] in ["@", "x"]:
                        rollCount += 1

                # bottom right
                if rowIndex < len(shelves) - 1 and columnIndex < len(shelves[rowIndex]) - 1:
                    if shelves[rowIndex + 1][columnIndex + 1] in ["@", "x"]:
                        rollCount += 1

                if rollCount < 4:
                    removed = True
                    shelves[rowIndex][columnIndex] = "."
                    counter += 1

print(counter)