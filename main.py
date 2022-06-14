import pyautogui
import time
import os
tab = ["/", "—", "\\", "|"]
i = 0

while True:
    os.system('cls')
    print(f"Wyszukiwanie gry {tab[i]}")
    if not pyautogui.locateOnScreen("img1.png") is None:
        pyautogui.click("img1.png")
        print("Znaleziono mecz!")
        time.sleep(10)

    i = i + 1
    if i == 4:
        i = 0
    time.sleep(5)

print(pyautogui.locateOnScreen("img.png"))