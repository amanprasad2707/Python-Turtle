import pyautogui as auto
import time
time.sleep(10)
for i in range(200):
    auto.write("hello world")
    auto.press("enter")