import pyautogui, time
while True:
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    time.sleep(1)
    print(px)