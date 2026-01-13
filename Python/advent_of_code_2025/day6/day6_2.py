with open("homework.txt", "rt") as file:
    content = file.read()

questionList: list[dict] = []
question: dict = {
    "numberList": [],
    "operation": "",
    "digitLength": 0
}

lines = content.split("\n")
tempLines = []
for line in lines:
    tempLines.append(list(line))
lines = tempLines

operationsOnly = lines[len(lines) - 1]
lines.pop()
temp = []
for char in operationsOnly:
    if char != " ":
        temp.append(char)
operationsOnly = temp


mergedLines = lines[0].copy()
for line in lines:
    for i in range(len(line)):
        if line[i] != " ":
            mergedLines[i] = line[i]

mergedString = ""
for char in mergedLines:
    mergedString += char
mergedLines = mergedString.split(" ")

digitLengths = []
for num in mergedLines:
    digitLengths.append(len(num))

extractedQuestions: list[list[str]] = []
for questionIndex in range(len(operationsOnly)):
    tempQuestion = []
    for lineIndex in range(len(lines)):
        tempString = ""
        for digitIndex in range(digitLengths[questionIndex]):
            tempString += lines[lineIndex].pop(0)

        if questionIndex != len(operationsOnly) - 1:
            lines[lineIndex].pop(0)
            
        tempQuestion.append(tempString)
    extractedQuestions.append(tempQuestion)

rotatedQuestions = []
for numList in extractedQuestions:
    tempNumList = []
    for numIndex in range(len(numList[0])):
        tempNum = ""
        for nums in range(len(numList)):
            if numList[nums][numIndex] != " ":
                tempNum += numList[nums][numIndex]
        tempNumList.append(int(tempNum))
    rotatedQuestions.append(tempNumList)

for questionIndex in range(len(rotatedQuestions)):
    questionList.append({
        "numberList": rotatedQuestions[questionIndex][::-1],
        "operation": operationsOnly[questionIndex]
    })

total = 0

for question in questionList:
    currentValue = 0
    if question["operation"] == "+":
        currentValue = 0
        for num in question["numberList"]:
            currentValue += num

    if question["operation"] == "*":
        currentValue = 1
        for num in question["numberList"]:
            currentValue *= num

    total += currentValue

print(total)