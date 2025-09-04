import time
import pyautogui
import pydirectinput

time.sleep(3)

while True:
    # navigate menu
    # play
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("play.png", grayscale=True, confidence=0.9)
            pyautogui.click(x, y)
            break
        except Exception as exception:
            print("Play button")
            print(type(exception))
    # expert
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("expert.png", grayscale=True, confidence=0.9)
            pyautogui.click(x, y)
            break
        except Exception as exception:
            print("Expert button")
            print(type(exception))
    # infernal
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("infernal.png", grayscale=True, confidence=0.9)
            pyautogui.click(x, y)
            break
        except Exception as exception:
            print("Infernal map")
            print(type(exception))
    # easy
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("easy.png", grayscale=True, confidence=0.9)
            pyautogui.click(x, y)
            break
        except Exception as exception:
            print("Easy button")
            print(type(exception))
    # deflation
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("deflation.png", grayscale=True, confidence=0.9)
            pyautogui.click(x, y)
            break
        except Exception as exception:
            print("Deflation button")
            print(type(exception))

    # place towers
    time.sleep(10)
    pyautogui.click(1356, 90)
    time.sleep(3)
    
    pyautogui.click(1580, 492)
    time.sleep(0.1)
    pydirectinput.press("k")
    time.sleep(0.1)
    pyautogui.click(1580, 492)
    time.sleep(0.1)
    pyautogui.click(1580, 492)
    time.sleep(0.1)
    pydirectinput.write("//,,", interval=0.1)
    time.sleep(0.1)

    pyautogui.click(1520, 604)
    time.sleep(0.1)
    pydirectinput.press("z")
    time.sleep(0.1)
    pyautogui.click(1520, 604)
    time.sleep(0.1)
    pyautogui.click(1520, 604)
    time.sleep(0.1)
    pydirectinput.write("..////", interval=0.1)
    time.sleep(0.1)

    pyautogui.click(1592, 676)
    time.sleep(0.1)
    pydirectinput.press("f")
    time.sleep(0.1)
    pyautogui.click(1592, 676)
    time.sleep(0.1)
    pyautogui.click(1592, 676)
    time.sleep(0.1)
    pydirectinput.write(",,,,..", interval=0.1)
    time.sleep(0.1)

    pyautogui.click(135, 579)
    time.sleep(0.1)
    pydirectinput.press("alt")
    time.sleep(0.1)
    pyautogui.click(135, 579)
    time.sleep(0.1)
    pyautogui.click(135, 579)
    time.sleep(0.1)
    pydirectinput.write("...//", interval=0.1)
    time.sleep(0.1)

    pydirectinput.press("space")
    time.sleep(0.1)
    pydirectinput.press("space")
    time.sleep(0.1)
    
    # wait until end screen
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("next.png", grayscale=True, confidence=0.9)
            pyautogui.click(x, y)
            break
        except:
            pyautogui.click(1920/2, 1080/2)
            time.sleep(1)

    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("home.png", grayscale=True, confidence=0.9)
            pyautogui.click(x, y)
            break
        except Exception as exception:
            print("Home button")
            print(type(exception))