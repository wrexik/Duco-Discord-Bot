import pyautogui
import cv2 as cv
from PIL import ImageGrab, Image
import os
import time as t

#im.getpixel((385, 831))

print("Getting Ready! Starting in 5s")
pyautogui.sleep(5)
print("Starting Now!")

color = (255, 0, 0)
Inf = 1
Bet = 1

while Inf == 1:
    pyautogui.sleep(2)                 #wait till discord refreshes
    im = pyautogui.screenshot()
    pixel = im.getpixel((385, 831))    #getting pixel color
    print(pixel)                       #prints the color
    pyautogui.sleep(3)

    if pixel == (color):               #loss

        print("Red = loss, Betting", Bet)
        Bet = 1
        pyautogui.write('!g ')
        pyautogui.write(str(Bet))
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        im = 0
    else:                              #win
        
        BetN = 2
        print("Green = win, Betting:", BetN)
        pyautogui.write('!g ')
        pyautogui.write(str(BetN))
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        im = 0