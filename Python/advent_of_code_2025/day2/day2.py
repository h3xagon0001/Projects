ranges = []
total = 0

with open("ranges.txt", "rt") as file:
    ranges = file.read().split(",")

for idRange in ranges:
    idRange = idRange.split("-")
    idRange = range(int(idRange[0]), int(idRange[1]) + 1)

    for id in idRange:
        n = 1
        idString = str(id)

        while n <= len(idString) / 2:
            searchString = idString[:n]
            temp = idString.replace(searchString, "")
            if temp == "":
                total += id
                print(id)
                break

            n += 1

print(total)