from pynput.mouse import Button, Controller
import time

mouse = Controller()

while 1==1:
    time.sleep(0.5)
    mouse.move(1, 0)