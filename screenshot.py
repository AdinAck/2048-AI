import os.path
import pyautogui
import tkinter as tk

root= tk.Tk()

i = 1
while True:
    if os.path.exists("up/up"+str(i)+".png"):
        i += 1
    else:
        print(i-1)
        upNum = i
        break
i = 1
while True:
    if os.path.exists("down/down"+str(i)+".png"):
        i += 1
    else:
        print(i-1)
        downNum = i - 1
        break
i = 1
while True:
    if os.path.exists("left/left"+str(i)+".png"):
        i += 1
    else:
        print(i-1)
        leftNum = i - 1
        break
i = 1
while True:
    if os.path.exists("right/right"+str(i)+".png"):
        i += 1
    else:
        print(i-1)
        rightNum = i - 1
        break

x1 = 685
y1 = 360
x2 = 1220
y2 = 895

coords = [x1,y1,x2-x1,y2-y1]

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def upClk():
    global upNum
    upNum += 1
    myScreenshot = pyautogui.screenshot(region=coords)
    myScreenshot.save("up/up"+str(upNum)+".png")

def downClk():
    global downNum
    downNum += 1
    myScreenshot = pyautogui.screenshot(region=coords)
    myScreenshot.save("down/down"+str(downNum)+".png")

def leftClk():
    global leftNum
    leftNum += 1
    myScreenshot = pyautogui.screenshot(region=coords)
    myScreenshot.save("left/left"+str(leftNum)+".png")

def rightClk():
    global rightNum
    rightNum += 1
    myScreenshot = pyautogui.screenshot(region=coords)
    myScreenshot.save("right/right"+str(rightNum)+".png")

def testClk():
    myScreenshot = pyautogui.screenshot(region=coords)
    myScreenshot.save("test.png")

up = tk.Button(text='Up', command=upClk, bg='green',fg='white',font= 10)
down = tk.Button(text='Down', command=downClk, bg='green',fg='white',font= 10)
left = tk.Button(text='Left', command=leftClk, bg='green',fg='white',font= 10)
right = tk.Button(text='Right', command=rightClk, bg='green',fg='white',font= 10)
test = tk.Button(text='Test', command=testClk, bg='green',fg='white',font= 10)

canvas1.create_window(150, 50, window=up)
canvas1.create_window(150, 100, window=down)
canvas1.create_window(150, 150, window=left)
canvas1.create_window(150, 200, window=right)
canvas1.create_window(150, 250, window=test)

root.mainloop()
