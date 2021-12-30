import pyautogui as pt
import time
import random
import os

pt.FAILSAFE = True

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def nav_to_image():
    target_png = resource_path('newMapBtn.png')
    position = pt.locateCenterOnScreen(target_png, grayscale=True, confidence=0.9)
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