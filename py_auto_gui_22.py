import pyautogui
import time
time.sleep(2)
print("start")
data='space'
time.sleep(2)
while True:
    if "space" in data:
        print("space")
    pyautogui.keyDown('space')
    time.sleep(4    )
    pyautogui.press('space')
print("done")

