import pyautogui
import time

time.sleep(2)
pyautogui.hotkey("win","3")
time.sleep(2)
pyautogui.press("browsersearch")
pyautogui.typewrite("facebook.com",1)
pyautogui.press("enter")
time.sleep(3)
# pyautogui.click(243,292,1,0,"left")
# time.sleep(5)
# pyautogui.click(440,247,1,0,"left")


# print(pyautogui.position())