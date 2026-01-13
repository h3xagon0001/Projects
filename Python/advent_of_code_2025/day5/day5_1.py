with open("ids.txt") as file:
    content = file.read().split("\n\n")

freshRanges = []
availableID = content[1].split("\n")

for range in content[0].split("\n"):
    freshRanges.append((
        int(range.split("-")[0]),
        int(range.split("-")[1])
    ))

freshCount = 0

for id in availableID:
    for range in freshRanges:
        if range[0] <= int(id) <= range[1]:
            freshCount += 1
            break

print(freshCount)