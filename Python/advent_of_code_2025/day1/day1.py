current = 50
rotations = []
i = 0
with open("rotations.txt", "rt") as file:
    rotations = file.read().split("\n")

for rotation in rotations:
    rotation = (rotation[0], int(rotation[1:]))

    if rotation[0] == "R":
        for x in range(rotation[1]):
            current += 1
            if current == 100:
                current = 0
                i += 1

    elif rotation[0] == "L":
        for x in range(rotation[1]):
            current -= 1
            if current == 0:
                i += 1
            if current == -1:
                current = 99

print(i)