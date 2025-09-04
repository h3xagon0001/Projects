import pyautogui
import pydirectinput
import time

time.sleep(3)

pydirectinput.press("k")




while True:
    print(pyautogui.position())
    time.sleep(1)