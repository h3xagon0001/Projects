import time

tape: str = ""
for i in range((4098+8191)*2): tape += "0"
pointer: int = round(len(tape) / 2)
state: str = "A"
table: list[dict[str, list[str]]] = [
    # symbol 0
    {
        "A": ["1", "R", "B"],
        "B": ["1", "R", "C"],
        "C": ["1", "R", "D"],
        "D": ["1", "L", "A"],
        "E": ["1", "R", "HALT"],
    },
    # symbol 1
    {
        "A": ["1", "L", "C"],
        "B": ["1", "R", "B"],
        "C": ["0", "L", "E"],
        "D": ["1", "L", "D"],
        "E": ["0", "L", "A"],
    }
]
stepCount = 0
    
startTime = time.time()

while True:
    """
    print(tape)
    whitespace = ""
    for i in range(pointer - 1):
        whitespace += " "
    print(whitespace, "^")
    print(f"Step: {stepCount}")
    print()
    """
    #input()
    stepCount += 1

    instruction = table[int(tape[pointer])][state]


    tapeList = list(tape)
    tapeList[pointer] = instruction[0]
    tape = "".join(tapeList)

    if instruction[1] == "R": pointer += 1
    elif instruction[1] == "L": pointer -= 1

    state = instruction[2]

    if stepCount % 100000 == 0:
        print(stepCount)

    if state == "HALT":
        endTime = time.time()
        
        print(tape)
        whitespace = ""
        for i in range(pointer - 1):
            whitespace += " "
        print(whitespace, "^")
        print(f"Step: {stepCount}")
        print(f"Time taken: {endTime - startTime} seconds")
        input("Program over")