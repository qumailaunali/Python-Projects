import pyautogui
import time

# comments = ["9:30","ajana"]

time.sleep(2)
a = 34
for i in range(100):
    
    pyautogui.typewrite(f"salman ki sal gira mah {a} min bacha ha")
    pyautogui.typewrite("\n")
    a=a-1
    time.sleep(60)
    
