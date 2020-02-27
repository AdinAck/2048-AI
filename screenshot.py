import os.path
import pyautogui
import pyscreenshot
from pynput import keyboard
import time

i = 1
while os.path.exists("up/up"+str(i)+".png"):
    i += 1
print(i-1)
upNum = i

i = 1
while os.path.exists("down/down"+str(i)+".png"):
    i += 1
print(i-1)
downNum = i - 1

i = 1
while os.path.exists("left/left"+str(i)+".png"):
    i += 1
print(i-1)
leftNum = i - 1

i = 1
while os.path.exists("right/right"+str(i)+".png"):
    i += 1
print(i-1)
rightNum = i - 1

size = pyautogui.size()

x1 = size[0]/2-275
y1 = size[1]/2-180
x2 = size[0]-700
y2 = size[1]-185

coords = [x1,y1,x2-x1,y2-y1]

yeet = input("Press enter to start...\n")

im = pyscreenshot.grab()
im = im.crop((x1,y1,x2,y2))

def up():
    global upNum
    upNum += 1
    im.save("up/up"+str(upNum)+".png")

def down():
    global downNum
    downNum += 1
    im.save("down/down"+str(downNum)+".png")

def left():
    global leftNum
    leftNum += 1
    im.save("left/left"+str(leftNum)+".png")

def right():
    global rightNum
    rightNum += 1
    im.save("right/right"+str(rightNum)+".png")

def on_press(key):
    global im
    if "up" in str(key):
        up()
    if "down" in str(key):
        down()
    if "left" in str(key):
        left()
    if "right" in str(key):
        right()
    try:
        print('{0} pressed'.format(key.char))
    except AttributeError:
        print('{0} pressed'.format(key))
    time.sleep(.1)
    im = pyscreenshot.grab()
    im = im.crop((x1,y1,x2,y2))

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press)
listener.start()
