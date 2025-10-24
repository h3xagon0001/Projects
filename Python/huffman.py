import json

class treeNode:
    def __init__(self, data: tuple[str, int, str]):
        self.data = data
        self.left = None
        self.right = None

def printTree(node, depth=0):
    if node == None:
        return
    string = ""
    for i in range(depth): string += "|   "
    print("{}{}".format(string, node.data))
    printTree(node.left, depth + 1)
    # print("{}{}".format(string, node.data))
    printTree(node.right, depth + 1)
    # print("{}{}".format(string, node.data))

def assignKeys(node, key, keyDict):
    if node == None:
        return
    
    node.data = (
        node.data[0],
        node.data[1],
        key
    )

    if node.left == None and node.right == None:
        keyDict[key] = node.data[0]

    assignKeys(node.left, key + "0", keyDict)
    assignKeys(node.right, key + "1", keyDict)

string = ""
with open("input.txt", "rt") as file:
    string = file.read()

charSet = set(string)
charNodes = []
for currentChar in charSet:
    frequency = 0
    for char in list(string):
        if char == currentChar:
            frequency += 1
    charNodes.append(treeNode((currentChar, frequency, "0")))

while len(charNodes) != 1:
    charNodes.sort(key=lambda treeNode: treeNode.data[1])
    node = treeNode((
            charNodes[0].data[0] + charNodes[1].data[0],
            charNodes[0].data[1] + charNodes[1].data[1],
            "0"
        ))
    
    node.left = charNodes[0]
    node.right = charNodes[1]

    charNodes.append(node)

    charNodes.pop(0)
    charNodes.pop(0)

rootNode = charNodes[0]
keyDict = {}
assignKeys(rootNode, rootNode.data[2], keyDict)

encodedData = ""
for char in string:
    for key in keyDict:
        if char == keyDict[key]:
            encodedData += key
            break

padding = 8 - (len(encodedData) % 8)
if len(encodedData) % 8 != 0:
    for i in range(8 - (len(encodedData) % 8)):
        encodedData += "0"
    
keyDict["padding"] = padding

with open("encoded.bin", "wb") as file:
    for i in range(0, len(encodedData), 8):
        file.write(bytes([int(encodedData[i:i+8], 2)]))


with open("keys.json", "wt") as file:
    file.write(json.dumps(keyDict))