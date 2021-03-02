import pyautogui
import time
print(pyautogui.position())


pyautogui.move(250, 500)     # x, y
pyautogui.move(250, 1000, 2)  # x , y , interval → random화
pyautogui.moveRel(0, 300, 2)  # x, y , interval (Relative)

pyautogui.click() # x, y, clicks, interval, button, duration, tween, logScreenshot
pyautogui.click(clicks=2, interval=2)

# doubleClick 과 click 함수 + interval은 다르다.

pyautogui.doubleClick()

time.sleep(3)

pyautogui.typewrite("Hello")  
pyautogui.typewrite("enter")
pyautogui.typewrite(['enter'])
pyautogui.typewrite(['a','b','c','enter'])           # list형태로 넣을때는 실제로 키보드에 있는 key를 Tmsek.
# pyautogui.typewrite(['abc','enter'])  # abc key는 없기때문에 enter key만 누르게 됨