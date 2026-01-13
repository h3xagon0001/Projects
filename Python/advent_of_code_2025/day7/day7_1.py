with open("diagram.txt", "rt") as file:
    content = file.read()

diagram = content.split("\n")

temp = []
for row in diagram:
    temp.append(list(row))
diagram = temp

splitCount = 0

for rowIndex in range(len(diagram)):
    if rowIndex == 0:
        pass
    else:
        for columnIndex in range(len(diagram[rowIndex])):
            if diagram[rowIndex - 1][columnIndex] in ["S", "|"]:
                if diagram[rowIndex][columnIndex] == "^":
                    diagram[rowIndex][columnIndex + 1] = "|"
                    diagram[rowIndex][columnIndex - 1] = "|"
                    splitCount += 1
                    
                else:
                    diagram[rowIndex][columnIndex] = "|"

for row in diagram:
    print(row)
print(f"Splits: {splitCount}")