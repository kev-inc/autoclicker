import pyautogui as pt
import time
import random
import os

pt.FAILSAFE = True
target_png = 'target.png'

def nav_to_image():
    position = pt.locateCenterOnScreen(target_png, grayscale=True, confidence=0.7)
    print(position)
    pt.doubleClick(position[0] + random.uniform(-5, 5) , position[1] + random.uniform(-5, 5))

print("Starting in 3 seconds... Please ensure that the whole game is visible on screen.")
time.sleep(3)
print("Autoclicker has started.")
while True:
    try:
        nav_to_image()
    except:
        pass
    finally:
        time.sleep(random.uniform(3,5))