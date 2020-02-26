import numpy as np
import pyautogui
import pyscreenshot
from PIL import Image
import fromModel
import tkinter as tk
import time

size = pyautogui.size()

x1 = size[0]/2-275
y1 = size[1]/2-180
x2 = size[0]-700
y2 = size[1]-185

coords = [x1,y1,x2-x1,y2-y1]

def action():
    time.sleep(wait)
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

def stuckAction(predict):
    big = max(predict)
    if big == predict[0]:
        predict[0] = 0
    if big == predict[1]:
        predict[1] = 0
    if big == predict[2]:
        predict[2] = 0
    if big == predict[3]:
        predict[3] = 0
    action()

yeet = input("Press enter to start...\n")
previous = 0
stuck = 0
wait = .1
time.sleep(1)
run = True
while run:
    im = pyscreenshot.grab()
    im = im.crop((x1,y1,x2,y2))
    predict = fromModel.getPrediction(im)[0]
    if np.all(predict) != np.all(previous):
        action()
    else:
        stuck += 1
        if stuck == 1:
            stuckAction(predict)
        if stuck == 2:
            stuckAction(predict)
            stuckAction(predict)
        if stuck == 3:
            stuckAction(predict)
            stuckAction(predict)
            stuckAction(predict)
            stuck = 0
    previous = predict
