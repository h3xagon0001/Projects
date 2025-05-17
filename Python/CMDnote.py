# features I might add:
# scrollable terminal
# delete key
# open/load existing file

import blessed
import os
import pyautogui

terminal = blessed.Terminal()

content = [
    ""
]

filename = "untitled"
terminalWidth = 0
terminalHeight = 0
cursorX = 0
cursorY = 0
lineColumnCounter = f"Ln {cursorY + 1}, Col {cursorX + 1}"
mode = "edit"



def refreshTerminal():
    global filename
    global mode

    # clear screen, idk what this does tbh
    os.system("cls")
    print(terminal.home + terminal.clear)

    # show filename
    print(terminal.black_on_white(terminal.center(filename)) + terminal.normal)
    print()

    # iterate through each line in content
    for line in range(len(content)):
        text = ""
        number = ""

        # display line number
        totalLineCount = len(content)
        lineNumber = line + 1
        padding = len(str(totalLineCount)) - len(str(lineNumber)) + 1 # padding from window border

        for space in range(padding):
            number += " "

        number += str(lineNumber) + " " # padding between number and content

        # append line number to start of line
        text += number

        # add character to line for display
        for character in range(len(content[line])):
            # check if character is at cursor pos
            if (character == cursorX) and (line == cursorY):
                text += terminal.black_on_white(content[line][character])

            else:
                text += content[line][character]

        # check if no character
        if (cursorX == len(content[line])) and (line == cursorY):
            text += terminal.black_on_white(" ")

        print(text)

    if mode == "edit":
        # show line column counter and keybinds
        lineColumnCounter = f"Ln {cursorY + 1}, Col {cursorX + 1}"

        print(
            terminal.move_xy(0, terminal.height) + "F1 Save    F2 Exit" +
            terminal.move_xy(terminal.width - len(lineColumnCounter), terminal.height) + lineColumnCounter
        )

    elif mode == "save":
        filename = input(terminal.move_xy(0, terminal.height) + "File name: ")
        with open(filename, "wt") as file:
            for lines in range(len(content)):
                file.write(content[lines])

                if lines != len(content) - 1:
                    file.write("\n")

        mode = "edit"
        refreshTerminal()
   
def lastCharacterIndex(line):
    index = len(content[line])
    return index

while True:
    
    if (terminalWidth != terminal.width) or (terminalHeight != terminal.height):
        terminalHeight = terminal.height
        terminalWidth = terminal.width

        refreshTerminal()

    with terminal.cbreak():
            keyPressed = terminal.inkey()
            
            if keyPressed.is_sequence:
                # check for enter newline
                if keyPressed.name == "KEY_ENTER":
                    if cursorX == lastCharacterIndex(cursorY):
                        cursorY += 1
                        cursorX = 0
                        content.insert(cursorY, "")
                        refreshTerminal()

                    elif cursorX == 0:
                        cursorY += 1
                        content.insert(cursorY - 1, "")
                        refreshTerminal()

                    else:
                        content.insert(cursorY + 1, "")

                        string = []

                        for character in range(cursorX + 1, lastCharacterIndex(cursorY) + 1):
                            string += content[cursorY][character - 1]
                        
                        for character in string:
                            content[cursorY + 1] += character

                        string = []

                        for character in range(0, cursorX):
                            string += content[cursorY][character]

                        content[cursorY] = ""

                        for character in string:
                            content[cursorY] += character

                        cursorX = 0
                        cursorY += 1
                        
                        refreshTerminal()

                elif keyPressed.name == "KEY_UP" and cursorY > 0:
                    cursorY -= 1
                    
                    if cursorX > lastCharacterIndex(cursorY):
                        cursorX = lastCharacterIndex(cursorY)

                    refreshTerminal()

                elif keyPressed.name == "KEY_DOWN" and cursorY < (len(content) - 1):
                    cursorY += 1
                    
                    if cursorX > lastCharacterIndex(cursorY):
                        cursorX = lastCharacterIndex(cursorY)

                    refreshTerminal()
                    
                elif keyPressed.name == "KEY_LEFT":
                    if cursorX == 0 and cursorY == 0:
                        pass

                    elif cursorX == 0 and cursorY != 0:
                        cursorY -= 1
                        cursorX = lastCharacterIndex(cursorY)

                        refreshTerminal()

                    elif cursorX != 0:
                        cursorX -= 1
                        refreshTerminal()

                elif keyPressed.name == "KEY_RIGHT":
                    if cursorX == lastCharacterIndex(cursorY) and cursorY == len(content) - 1:
                        pass

                    elif cursorX == lastCharacterIndex(cursorY) and cursorY != len(content) - 1:
                        cursorY += 1
                        cursorX = 0

                        refreshTerminal()

                    elif cursorX != lastCharacterIndex(cursorY):
                        cursorX += 1
                        refreshTerminal()

                elif keyPressed.name == "KEY_BACKSPACE":
                    if cursorX == 0 and cursorY == 0:
                        pass
                    
                    elif cursorX == 0 and cursorY != 0:
                        cursorY -= 1
                        cursorX = lastCharacterIndex(cursorY)

                        content[cursorY] += content[cursorY + 1]
                        content.pop(cursorY + 1)

                        refreshTerminal()

                    elif cursorX != 0:
                        string = []

                        for character in content[cursorY]:
                            string += character

                        string.pop(cursorX - 1)
                        
                        content[cursorY] = ""
                        for character in string:
                            content[cursorY] += character
                        
                        cursorX -= 1
                        refreshTerminal()

                elif keyPressed.name == "KEY_F1":
                    mode = "save"
                    refreshTerminal()

                elif keyPressed.name == "KEY_F2":
                    exit()

                


            elif keyPressed:
                string = []

                for character in content[cursorY]:
                    string += character

                string.insert(cursorX, keyPressed)
                
                content[cursorY] = ""
                for character in string:
                    content[cursorY] += character
                
                cursorX += 1
                refreshTerminal()