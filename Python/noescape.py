import os
import time
import pyautogui
import random

content = '''Dim y
y = 0
Do While y = 0
x = MsgBox("There is no escape.",0,"There is no escape.")
Loop
'''
screenWidth, screenHeight = pyautogui.size()

file = open("noescape.vbs", "w")
file.write(content)
file.close()
os.startfile("noescape.vbs")
time.sleep(0.25)
os.remove("noescape.vbs")
pyautogui.click(30, 1050)
pyautogui.write("notepad", interval=0.25)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.hotkey("winleft", "up")
time.sleep(0.5)
pyautogui.moveTo(screenWidth/2, screenHeight/2)
pyautogui.write("There is no escape. :)", interval=0.25)