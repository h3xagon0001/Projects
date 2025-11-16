from time import sleep
import pyautogui
import pydirectinput
from random import choice

def click(targetImg: str, successImg: str, confidence: float = 0.9):
    try: # try to check for success target
        pyautogui.locateCenterOnScreen(successImg, grayscale=True, confidence=confidence) # type: ignore
        return

    except Exception as successException:
        try: # tries to click on target image
            targetPos = pyautogui.locateCenterOnScreen(targetImg, grayscale=True, confidence=confidence) # type: ignore
            pyautogui.click(targetPos)
            return

        except Exception as targetException:
            print("successImg: ", successImg, type(targetException))
            print("targetImg: ", targetImg, type(successException))
            click(targetImg, successImg, confidence)

sleep(3)

while True:
    click("play.png", "back.png") # play button
    click("expert.png", "infernal.png") # navigate to infernal map
    click("infernal.png", "easy.png") # select infernal
    click("easy.png", "deflation.png") # select easy
    click("deflation.png", "ok_popup.png") # select deflation
    click("ok_popup.png", "ok_popup.png") # wait for popup
    click("ok.png", "map_visible.png") # click ok
    click("map_visible.png", "map_visible.png", 0.5) # wait for popup to close

    # place village
    click("village.png", "village_placed.png", 0.8)
    sleep(0.1)
    pydirectinput.press("k")
    sleep(0.1)
    pyautogui.click()
    sleep(0.1)
    pyautogui.click()
    pydirectinput.write("//,,", interval=0.1)
    sleep(0.1)

    # place sniper
    click("sniper.png", "sniper_placed.png", 0.8)
    sleep(0.1)
    pydirectinput.press("z")
    sleep(0.1)
    pyautogui.click()
    sleep(0.1)
    pyautogui.click()
    pydirectinput.write("..////", interval=0.1)
    sleep(0.1)

    # place alchemist
    click("alchemist.png", "alchemist_placed.png", 0.8)
    sleep(0.1)
    pydirectinput.press("f")
    sleep(0.1)
    pyautogui.click()
    sleep(0.1)
    pyautogui.click()
    pydirectinput.write(",,,,..", interval=0.1)
    sleep(0.1)
    
    # place misc towers
    for locations in ["misc_4.png", "misc_1.png", "misc_3.png", "misc_2.png", "misc_5.png", "misc_6.png"]:
        click(locations, "placeholder.png", 0.7) # placeholder is used to always click
        sleep(0.1)
        pydirectinput.press(choice(["y", "alt", "i"]))
        sleep(0.1)
        pyautogui.click()
        sleep(0.1)
    
    # start round
    pydirectinput.press("space")
    sleep(0.1)
    pydirectinput.press("space")
    sleep(0.1)
    
    # click to close level up screens
    while True:
        try:
            pyautogui.locateCenterOnScreen("next.png", grayscale=True, confidence=0.9) # type: ignore
            break

        except Exception as successException:
            pyautogui.click(pyautogui.size()[0] / 2, pyautogui.size()[1] / 2)
            sleep(0.5)
            pyautogui.click(pyautogui.size()[0] / 2, pyautogui.size()[1] / 2)

        sleep(3)

    # return to menu
    click("next.png", "home.png")
    click("home.png", "play.png") # click home