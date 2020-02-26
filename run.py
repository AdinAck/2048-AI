import numpy as np
import pyautogui
import pyscreenshot
from PIL import Image
import fromModel
import tkinter as tk
import time
import random

size = pyautogui.size()

x1 = size[0]/2-275
y1 = size[1]/2-180
x2 = size[0]-700
y2 = size[1]-185

coords = [x1,y1,x2-x1,y2-y1]

yeet = input("Press enter to start...\n")
previous = 0
time.sleep(1)
run = True
while run:
    im = pyscreenshot.grab()
    im = im.crop((x1,y1,x2,y2))
    time.sleep(.5)
    predict = fromModel.getPrediction(im)[0]
    if np.all(predict) != np.all(previous):
        if max(predict) == predict[0]:
            pyautogui.press('up')
            print("Up")
        if max(predict) == predict[1]:
            pyautogui.press('down')
            print("Down")
        if max(predict) == predict[2]:
            pyautogui.press('left')
            print("Left")
        if max(predict) == predict[3]:
            pyautogui.press('right')
            print("Right")
    else:
        r = random.randint(0,3)
        if r == 0:
            pyautogui.press('up')
            print("Up")
        if r == 1:
            pyautogui.press('down')
            print("Down")
        if r == 2:
            pyautogui.press('left')
            print("Left")
        if r == 3:
            pyautogui.press('right')
            print("Right")

    previous = predict
