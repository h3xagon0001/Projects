with open("ids.txt") as file:
    content = file.read().split("\n\n")

freshRanges = []

for range in content[0].split("\n"):
    freshRanges.append([
        int(range.split("-")[0]),
        int(range.split("-")[1])
    ])

while True:
    foundOverlap = False

    for range in freshRanges:
        for targetRange in freshRanges:
            if range != targetRange:
                if targetRange[0] <= range[0] and range[0] <= targetRange[1] <= range[1]: # { ( } )
                    range[0] = targetRange[0]
                    targetRange[1] = range[1]
                    foundOverlap = True
                if range[0] <= targetRange[0] <= range[1] and targetRange[1] >= range[1]: #  ( { ) }
                    targetRange[0] = range[0]
                    range[1] = targetRange[1]
                    foundOverlap = True
                if range[0] <= targetRange[0] and targetRange[1] <= range[1]: # ( { } )
                    targetRange[0] = range[0]
                    targetRange[1] = range[1]
                    foundOverlap = True
                if range[0] >= targetRange[0] and targetRange[1] >= range[1]: # { ( ) }
                    range[0] = targetRange[0]
                    range[1] = targetRange[1]
                    foundOverlap = True

    if foundOverlap == False:
        break

freshSet = set()
for range in freshRanges:
    freshSet.add(str(range))

freshRanges = []
for range in freshSet:
    freshRanges.append(range[1:len(range) - 1])

total = 0

for range in freshRanges:
    total += (int(range.split(", ")[1]) + 1) - int(range.split(", ")[0])

print(total)