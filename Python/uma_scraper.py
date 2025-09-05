import requests
import re
import selectolax
import json

ONE_STAR_URL    = 'https://game8.co/games/Umamusume-Pretty-Derby/archives/536282'
TWO_STAR_URL    = 'https://game8.co/games/Umamusume-Pretty-Derby/archives/536283'
THREE_STAR_URL  = 'https://game8.co/games/Umamusume-Pretty-Derby/archives/536284'

umaData = []
supportCardData = []

def getTable(html: str):
    htmlLines: list[str] = html.split("\n")

    while True:
        if htmlLines[0] != "<table class='a-table a-table top center a-table' style=''>":
            htmlLines.pop(0)
        else:
            break

    foundTableEnd = False

    for i in range(len(htmlLines)):
        if foundTableEnd:
            htmlLines[i] = ""

        if htmlLines[i] == "</table>":
            foundTableEnd = True
        else:
            pass

    table = ""

    for i in range(len(htmlLines)):
        if htmlLines[i] == "":
            pass
        else:
            table += htmlLines[i] + "\n"


    return table

def getLinks(table: str):
    searchResult = re.findall("(<a class='a-link' href=)(.*)(><img)", table)

    for i in range(len(searchResult)):
        searchResult[i] = searchResult[i][1]

    return searchResult

def getUmaInfo(url: str):
    r = requests.get(url)

    htmlLines: list[str] = r.text.split("\n")

    while True:
        if htmlLines[0] != "<table class='a-table a-table table--fixed a-table' style=''>":
            htmlLines.pop(0)
        else:
            break

    foundContentEnd = False

    for i in range(len(htmlLines)):
        if foundContentEnd:
            htmlLines[i] = ""

        if htmlLines[i] == "<h2 class='a-header--2' id='hl_6'>King Halo Profile</h2><h3 class='a-header--3' id='hm_11'>Basic Information</h3>":
            foundContentEnd = True
        else:
            pass
    
    content = ""

    for i in range(len(htmlLines)):
        line = htmlLines[i].strip()

        if line in ["", "<tr>", "</tr>", "</th>", "<td>", "</td>", "</table>"]:
            pass

        elif line[:4] == "<img":
            pass        

        else:
            content += line + "\n"

    htmlLines = content.split("\n")

    extractedContent = {
        "name": "",
        "training_tips": [],
        "build": {
            "speed": 0,
            "stamina": 0,
            "power": 0,
            "guts": 0,
            "wit": 0
        },
        "support_cards": {
            "best": [],
            "alternate": []
        },
        "sparks": {
            "stats": "",
            "aptitude": ""
        },
        "skills": [],
        "events": ""
    }

    # name
    targetString = '<th class="center" colspan=20>'
    while True:
        if htmlLines[0][:len(targetString)] == targetString:
            break
        else:
            htmlLines.pop(0)

    extractedContent["name"] = htmlLines[0][30:]

    # training tips
    targetString = "<th>Training Tips</th>"
    while True:
        if htmlLines[0][:len(targetString)] == targetString:
            htmlLines.pop(0)
            break
        else:
            htmlLines.pop(0)

    targetString = "<h3"
    while True:
        if htmlLines[0][:len(targetString)] == targetString:
            htmlLines.pop(0)
            break
        else:
            tip = re.findall("(href=#hm_...>)(.*)(</a>)", htmlLines[0])
            extractedContent["training_tips"].append(tip[0][1])
            htmlLines.pop(0)

    # build
    targetString = "<table class='a-table a-table center a-table' style=''>"
    while True:
        if htmlLines[0][:len(targetString)] == targetString:
            htmlLines.pop(0)
            break
        else:
            htmlLines.pop(0)

    for i in range(5):
        htmlLines.pop(0)

    extractedContent["build"]["speed"] = re.findall("(<td><b class='a-bold'>)(.*)(</b></td>)", htmlLines[0])[0][1]
    extractedContent["build"]["stamina"] = re.findall("(<td><b class='a-bold'>)(.*)(</b></td>)", htmlLines[1])[0][1]
    extractedContent["build"]["power"] = re.findall("(<td><b class='a-bold'>)(.*)(</b></td>)", htmlLines[2])[0][1]
    extractedContent["build"]["guts"] = re.findall("(<td><b class='a-bold'>)(.*)(</b></td>)", htmlLines[3])[0][1]
    extractedContent["build"]["wit"] = re.findall("(<td><b class='a-bold'>)(.*)", htmlLines[4])[0][1]

    # support cards (best)
    targetString = "Recommended Support Cards"
    while True:
        if htmlLines[0][:len(targetString)] == targetString:
            htmlLines.pop(0)
            htmlLines.pop(0)
            break
        else:
            htmlLines.pop(0)

    targetString = "<p class='a-paragraph'>"
    while True:
        if "</tr><tr>" in htmlLines[0] or "<td" in htmlLines[0]:
            htmlLines.pop(0)

        else:
            if htmlLines[0][:len(targetString)] == targetString:
                htmlLines.pop(0)
                break
            else:
                cardName = re.findall("(/>)(.*)(</a>)", htmlLines[0])[0][1]
                extractedContent["support_cards"]["best"].append(cardName)
                htmlLines.pop(0)

    # support cards (alternate)
    targetString = "<th colspan=3>Alternate Cards</th>"
    while True:
        if htmlLines[0][:len(targetString)] == targetString:
            htmlLines.pop(0)
            htmlLines.pop(0)
            break
        else:
            htmlLines.pop(0)

    targetString = "<th colspan=2></th>"

    while True:
        if "</tr><tr>" in htmlLines[0] or "<td" in htmlLines[0] or "<hr" in htmlLines[0]:
            htmlLines.pop(0)

        else:
            if htmlLines[0][:len(targetString)] == targetString:
                htmlLines.pop(0)
                break
            else:
                try:
                    cardName = re.findall("(<template class='js-tooltip-content'>)(.*)( <br>)", htmlLines[0])[0][1]
                    extractedContent["support_cards"]["alternate"].append(cardName.strip())
                    htmlLines.pop(0)
                except:
                    print(Exception.__traceback__)
                    break

    # sparks
    targetString = '<th width="70%">Recommended</th>'
    while True:
        if htmlLines[0][:len(targetString)] == targetString:
            htmlLines.pop(0)
            htmlLines.pop(0)
            break
        else:
            htmlLines.pop(0)

    targetString = "<p class='a-paragraph'>"
    while True:
        if "</tr><tr>" in htmlLines[0] or "<hr" in htmlLines[0] or "<th><div class='align'>" in htmlLines[0]:
            htmlLines.pop(0)

        else:
            if htmlLines[0][:len(targetString)] == targetString:
                htmlLines.pop(0)
                break
            else:
                htmlLines[0] = htmlLines[0].replace("<td>", "").replace("<br>", "~").replace("</td>", "").replace('<hr class="a-table__line">', "~")
                htmlLines[2] = htmlLines[2].replace("<td>", "").replace("<br>", "~").replace("</td>", "").replace('<hr class="a-table__line">', "~")
                
                extractedContent["sparks"]["stats"] = htmlLines[0].split("~")
                extractedContent["sparks"]["aptitude"] = htmlLines[2].split("~")
                
                htmlLines.pop(0)
                htmlLines.pop(0)
                htmlLines.pop(0)
    
    # skills
    targetString = 'Recommended Skills'
    while True:
        if htmlLines[0][:len(targetString)] == targetString:
            htmlLines.pop(0)
            htmlLines.pop(0)
            break
        else:
            htmlLines.pop(0)

    targetString = "<p class='a-paragraph'>"
    while True:
        if "</tr><tr>" in htmlLines[0] or "<td" in htmlLines[0]:
            htmlLines.pop(0)

        else:
            if htmlLines[0][:len(targetString)] == targetString:
                htmlLines.pop(0)
                break
            else:
                skill = re.findall("( />)(.*)(</a>)", htmlLines[0])
                extractedContent["skills"].append(skill[0][1])
                htmlLines.pop(0)

    # events
    parsedHTMLList = selectolax.parser.HTMLParser(r.text).text().split("\n")
    parsedHTML = ""
    for i in range(len(parsedHTMLList)):
        if parsedHTMLList[i] != "":
            parsedHTML += parsedHTMLList[i] + "\n"

    parsedHTMLList = parsedHTML.replace("Choice\nOutcome\n", "").split("\n")

    targetString = "Race Events"
    while True:
        if parsedHTMLList[0] == targetString:
            parsedHTMLList.pop(0)
            parsedHTMLList.pop(0)
            parsedHTMLList.pop(0)
            break
        else:
            parsedHTMLList.pop(0)

    lineIndex = len(parsedHTMLList) - 1
    while lineIndex != -1:
        if parsedHTMLList[lineIndex] == "Choice 1":
            parsedHTMLList.insert(lineIndex - 1, "")
        lineIndex -= 1

    targetString = "Event Choice Checker"
    while True:
        try:
            if parsedHTMLList[0] == targetString:
                parsedHTMLList.pop(0)
                break
            else:
                extractedContent["events"] += parsedHTMLList[0] + "\n"
                parsedHTMLList.pop(0)    
        except Exception:
            print(Exception.__traceback__)
            break            

    return extractedContent

def readData(extractedContent: dict):
    output = ""
    output += f"Name: {extractedContent["name"]}\n\n"

    output += "Training tips:\n"
    for i in range(len(extractedContent["training_tips"])):
        output += extractedContent["training_tips"][i] + "\n"
    output += "\n"

    output += "Reccomended build:\n"
    output += f"Speed: {extractedContent["build"]["speed"]}\n"
    output += f"Stamina: {extractedContent["build"]["stamina"]}\n"
    output += f"Power: {extractedContent["build"]["power"]}\n"
    output += f"Guts: {extractedContent["build"]["guts"]}\n"
    output += f"Wit: {extractedContent["build"]["wit"]}\n"
    output += "\n"

    output += "Support cards:\n"
    output += "Best:\n"
    for card in extractedContent["support_cards"]["best"]:
        output += card + "\n"
    output += "\n"
    output += "Alternate:\n"
    for card in extractedContent["support_cards"]["alternate"]:
        output += card + "\n"
    output += "\n"

    output += "Sparks:\n"
    output += "Stats:\n"
    for spark in extractedContent["sparks"]["stats"]:
        output += spark + "\n"
    output += "\n"
    output += "Aptitude:\n"
    for spark in extractedContent["sparks"]["aptitude"]:
        output += spark + "\n"
    output += "\n"

    output += "Reccomended skills:\n"
    for skill in extractedContent["skills"]:
        output += f"{skill}\n"
    output += "\n"

    output += "Trainee events:\n"
    output += extractedContent["events"]

    output += "\n\n\n"

    return output




one_star_request = requests.get(ONE_STAR_URL)
two_star_request = requests.get(TWO_STAR_URL)
three_star_request = requests.get(THREE_STAR_URL)


for url in getLinks(getTable(one_star_request.text)):
    umaData.append(getUmaInfo(url))

for url in getLinks(getTable(two_star_request.text)):
    umaData.append(getUmaInfo(url))

for url in getLinks(getTable(three_star_request.text)):
    umaData.append(getUmaInfo(url))    

data = ""

for uma in umaData:
    data += readData(uma)

with open("data.txt", "wt", encoding="utf-8") as file:
    file.write(data)