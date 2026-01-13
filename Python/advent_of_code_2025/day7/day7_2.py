with open("diagram.txt", "rt") as file:
    content = file.read()

diagram = content.split("\n")

temp = []
for row in diagram:
    temp.append(list(row))
diagram = temp

timeline = {"count": 0}

def particleMove(diagram, rowIndex, columnIndex, tl={"count": 0}):
    if rowIndex == len(diagram) - 1:
        timeline["count"] += 1
        return
    
    if diagram[rowIndex + 1][columnIndex] == ".":
        particleMove(diagram, rowIndex + 1, columnIndex)
        # return

    if diagram[rowIndex + 1][columnIndex] == "^":
        particleMove(diagram, rowIndex + 1, columnIndex + 1)
        particleMove(diagram, rowIndex + 1, columnIndex - 1)

particleMove(diagram, 0, diagram[0].index("S"), timeline)

for row in diagram: print(row)
print(timeline)