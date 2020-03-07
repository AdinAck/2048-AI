import numpy as np
import random
from pynput import keyboard

board = np.array([[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]])
score = 0
gameEnd = False

def genRandomBlock(board):
    zeroList = np.array([])
    for i in range(4):
        for j in range(4):
            if board[i,j] == 0:
                zeroList = np.append(zeroList, [i,j])
    try:
        zeroList.shape = np.size(zeroList)//2,2
        newBlockPos = zeroList[random.randint(0,np.size(zeroList,0)-1)]
        board[int(newBlockPos[0]),int(newBlockPos[1])] = int(1+random.randint(6,10)/10)
    except ValueError:
        print("This should not happen, attempted to place random block in board with no zeros?")

    return zeroList

genRandomBlock(board)
genRandomBlock(board)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(board)
print("Score: {0}".format(score))

def move(self, direction, board):
    global score
    preboard = np.array(board)
    if direction == 0: #UP
        for x in range(4):
            lastNumber = board[0,x]
            lastNumIndex = 0
            for y in [1,2,3]:
                if board[y,x] != 0:
                    if lastNumber == 0:
                        board[lastNumIndex,x] = board[y,x]
                        board[y,x] = 0
                        lastNumber = board[lastNumIndex,x]
                    elif lastNumber == board[y,x]:
                        board[lastNumIndex,x] = lastNumber+1
                        board[y,x] = 0
                        score += 2**(board[lastNumIndex,x])
                        lastNumIndex +=1
                        lastNumber = board[lastNumIndex,x]
                    else:
                        if  lastNumIndex+1 < y:
                            board[lastNumIndex+1,x] = board[y,x]
                            board[y,x] = 0
                        lastNumIndex +=1
                        lastNumber = board[lastNumIndex,x]
    if direction == 1: #DOWN
        for x in range(4):
            lastNumber = board[3,x]
            lastNumIndex = 3
            for y in [2,1,0]:
                if board[y,x] != 0:
                    if lastNumber == 0:
                        board[lastNumIndex,x] = board[y,x]
                        board[y,x] = 0
                        lastNumber = board[lastNumIndex,x]
                    elif lastNumber == board[y,x]:
                        board[lastNumIndex,x] = board[y,x]+1
                        board[y,x] = 0
                        score += 2**(board[lastNumIndex,x])
                        lastNumIndex -=1
                        lastNumber = board[lastNumIndex,x]
                    else:
                        if lastNumIndex-1 > y:
                            board[lastNumIndex-1,x] = board[y,x]
                            board[y,x] = 0
                        lastNumIndex -=1
                        lastNumber = board[lastNumIndex,x]
    if direction == 2: #LEFT
        for y in range(4):
            lastNumber = board[y,0]
            lastNumIndex = 0
            for x in [1,2,3]:
                if board[y,x] != 0:
                    if lastNumber == 0:
                        board[y,lastNumIndex] = board[y,x]
                        board[y,x] = 0
                        lastNumber = board[y,lastNumIndex]
                    elif lastNumber == board[y,x]:
                        board[y,lastNumIndex] = lastNumber+1
                        board[y,x] = 0
                        score += 2**(board[y,lastNumIndex])
                        lastNumIndex +=1
                        lastNumber = board[y,lastNumIndex]
                    else:
                        if  lastNumIndex+1 < x:
                            board[y,lastNumIndex+1] = board[y,x]
                            board[y,x] = 0
                        lastNumIndex +=1
                        lastNumber = board[y,lastNumIndex]
    if direction == 3: #RIGHT
        for y in range(4):
            lastNumber = board[y,3]
            lastNumIndex = 3
            for x in [2,1,0]:
                if board[y,x] != 0:
                    if lastNumber == 0:
                        board[y,lastNumIndex] = board[y,x]
                        board[y,x] = 0
                        lastNumber = board[y,lastNumIndex]
                    elif lastNumber == board[y,x]:
                        board[y,lastNumIndex] = lastNumber+1
                        board[y,x] = 0
                        score += 2**(board[y,lastNumIndex])
                        lastNumIndex -=1
                        lastNumber = board[y,lastNumIndex]
                    else:
                        if  lastNumIndex-1 > x:
                            board[y,lastNumIndex-1] = board[y,x]
                            board[y,x] = 0
                        lastNumIndex -=1
                        lastNumber = board[y,lastNumIndex]

    if not np.array_equal(preboard,board):
        zeroList = genRandomBlock(board)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(board)
        print("Score: {0}".format(score))
        if np.size(zeroList,0) == 1:
            gameEnd = True
            for i in [1,2]:
                for j in range(4):
                    if board[i,j] == board[i-1,j] or board[i,j] == board[i+1,j]:
                        gameEnd = False
            for j in [1,2]:
                for i in range(4):
                    if board[i,j] == board[i,j-1] or board[i,j] == board[i,j+1]:
                        gameEnd = False
            if gameEnd:
                print("\nGame over!")
                print("====================")
                print("Final score: {0}".format(score))
                print("Number of moves: {0}".format(moves))
    else: return False
    return True

# Key listening
def on_press(key):
    global board
    global score
    if not gameEnd:
        if "up" in str(key):
            move(board, 0, board)
        if "down" in str(key):
            move(board, 1, board)
        if "left" in str(key):
            move(board, 2, board)
        if "right" in str(key):
            move(board, 3, board)

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press)
listener.start()
