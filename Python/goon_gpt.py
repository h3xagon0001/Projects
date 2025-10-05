import requests
from bs4 import BeautifulSoup
import json
import random

# STEP 0 - Setup
print("STEP 0 - Setup")

with open("input.txt", "wt") as inputFile:
    inputFile.close()

print("input.txt created successfully.")



# STEP 1 - Dataset
print("STEP 1 - Dataset")
    
# extract text from sites
while True:
    url = input("Enter url (leave empty to for next step): ")
    if url != "":
        r = requests.get(url, headers = { 'user-agent': 'Mozilla/5.0' })
        
        with open("input.txt", "at", encoding="utf-8") as inputFile:
            inputFile.write(BeautifulSoup(r.text, features="html.parser").get_text(" ", strip=True) + "\n")

    else:
        break

input("Check input.txt manually. (enter to continue)")

# make input.txt a continous string without newlines and unwanted characters
content = ""
with open("input.txt", "rt", encoding="utf-8") as inputFile:
    content = inputFile.read()

# lowercase text and remove newlines
content = content.lower()
content = content.replace("\n", " ")

# excluded characters
content = content.replace("'", "")
content = content.replace('"', "")
content = content.replace("{", "")
content = content.replace("}", "")
content = content.replace("(", "")
content = content.replace(")", "")
content = content.replace("[", "")
content = content.replace("]", "")

# space out characters
content = content.replace(".", " . ")
content = content.replace(",", " , ")
content = content.replace("?", " ? ")
content = content.replace("!", " ! ")
content = content.replace(":", " : ")
content = content.replace(";", " ; ")
content = content.replace("%", " % ")
content = content.replace("&", " & ")
content = content.replace("$", " $ ")
content = content.replace("/", " / ")

# make into list and remove spaces
content = content.split(" ")
wordList = []
for word in content:
    if word != " " and word != "":
        wordList.append(word)

# write list as json to word_list.txt
with open("word_list.json", "wt", encoding="utf-8") as file:
    file.write(json.dumps(wordList))

# create word_index.txt that contains only one instance of each word in a list
wordIndex = []
for word in wordList:
    if word not in wordIndex:
        wordIndex.append(word)

with open("word_index.json", "wt", encoding="utf-8") as file:
    file.write(json.dumps(wordIndex))

# STEP 2 - Assignment
print("STEP 2 - Assignment")

# add every word, occurence, weight to every word
wordIndex = []
with open("word_index.json", "rt", encoding="utf-8") as file:
    wordIndex = json.loads(file.read())

print("Generating wordDataIndex")
wordDataIndex = []
for word in wordIndex:
    wordData = {
        "word": word,
        "nextWord": [] # list of dict
    }

    for word in wordIndex:
        wordData["nextWord"].append({
            "word": word,
            "count": 0,
            "weight": 1.0
        })

    wordDataIndex.append(wordData)

with open("word_data_index.json", "wt", encoding="utf-8") as file:
    file.write(json.dumps(wordDataIndex, indent=2))

print("Counting nextWord")
# count next word occurrences
with open("word_data_index.json", "rt", encoding="utf-8") as file:
    wordDataIndex = json.loads(file.read())

with open("word_list.json", "rt", encoding="utf-8") as file:
    wordList = json.loads(file.read())

for i in range(len(wordList) - 1):
    currentWord = wordList[i]
    nextWord = wordList[i+1]

    # increment the currentWord's wordData of nextWord's count by 1

    # search for currentWord
    for j in range(len(wordDataIndex)):
        if wordDataIndex[j]["word"] == currentWord:
            # search for nextWord in currentWord data
            for k in range(len(wordDataIndex[j]["nextWord"])):
                if wordDataIndex[j]["nextWord"][k]["word"] == nextWord:
                    wordDataIndex[j]["nextWord"][k]["count"] += 1

with open("word_data_index.json", "wt", encoding="utf-8") as file:
    file.write(json.dumps(wordDataIndex, indent=1))

# STEP 2.5 - Cleaning
print("STEP 2.5 - Cleaning")

# remove all nextWord's with weight of 0.0
with open("word_data_index.json", "rt", encoding="utf-8") as file:
    wordDataIndex = json.loads(file.read())

for i in range(len(wordDataIndex)):
    wordDataIndex[i]["nextWord"] = [
        item for item in wordDataIndex[i]["nextWord"] if item["count"] != 0.0
    ]

with open("word_data_index.json", "wt", encoding="utf-8") as file:
    file.write(json.dumps(wordDataIndex, indent=1))



# STEP 3 - Random Noise and Normalisation
print("STEP 3 - Random Noise and Normalisation")

with open("word_data_index.json", "rt", encoding="utf-8") as file:
    wordDataIndex = json.loads(file.read())

print("Adding noise to weights.")
for i in range(len(wordDataIndex)):
    for j in range(len(wordDataIndex[i]["nextWord"])):
        # add noise to each nextWord
        wordDataIndex[i]["nextWord"][j]["weight"] = wordDataIndex[i]["nextWord"][j]["weight"] + random.uniform(-0.1, 0.1)

print("Calculating weight product.")
for i in range(len(wordDataIndex)):
    for j in range(len(wordDataIndex[i]["nextWord"])):
        # add noise to each nextWord
        wordDataIndex[i]["nextWord"][j]["weight"] = wordDataIndex[i]["nextWord"][j]["weight"] * wordDataIndex[i]["nextWord"][j]["count"]

print("Normalising weights.")
for i in range(len(wordDataIndex)):
    # total weight of word
    totalWeight = 0
    for j in range(len(wordDataIndex[i]["nextWord"])):
        totalWeight += wordDataIndex[i]["nextWord"][j]["weight"]

    # calculate and assign normalised weight
    for j in range(len(wordDataIndex[i]["nextWord"])):
        wordDataIndex[i]["nextWord"][j]["weight"] = wordDataIndex[i]["nextWord"][j]["weight"] / totalWeight

with open("word_data_index.json", "wt", encoding="utf-8") as file:
    file.write(json.dumps(wordDataIndex, indent=1))



# STEP 4 - Generation
print("STEP 4 - Generation")

with open("word_data_index.json", "rt", encoding="utf-8") as file:
    wordDataIndex = json.loads(file.read())

# search for the current word
# create a list of the next word
# and a list of weights
# generate and set it as the current word
currentWord = "."
outString = ""
for i in range(100):
    currentWordData = {}
    for j in range(len(wordDataIndex)):
        if wordDataIndex[j]["word"] == currentWord:
            currentWordData = wordDataIndex[j]

    nextWordList = []
    nextWordWeights = []

    for j in range(len(currentWordData["nextWord"])):
        nextWordList.append(currentWordData["nextWord"][j]["word"])
        nextWordWeights.append(currentWordData["nextWord"][j]["weight"])

    currentWord = random.choices(nextWordList, weights=nextWordWeights)[0]
    
    if currentWord not in [".", ",", "?", "!"]:
        outString += " "

    outString += currentWord

print(outString)     