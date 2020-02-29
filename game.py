import numpy as np
import random
from pynput import keyboard

board = np.array([[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]])
score = 0
gameEnd = False
moves = 0

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

def move(board, direction):
    global score
    global moves
    preBoard = np.array(board)
    mergedList = []
    if direction == 0:
        for i in [1,2,3]:
            for j in range(4):
                if i == 1:
                    if board[i-1,j] == 0:
                        board[i-1,j] = board[i,j]
                        board[i,j] = 0
                    if board[i,j] == board[i-1,j] and board[i,j] != 0 and [i-1,j] not in mergedList:
                        board[i-1,j] = board[i-1,j]+1
                        board[i,j] = 0
                        score += 2**(board[i-1,j])
                        mergedList.append([i-1,j])
                if i == 2:
                    for p in range(i):
                        if board[i-p-1,j] == 0:
                            board[i-p-1,j] = board[i-p,j]
                            board[i-p,j] = 0
                        else: break
                    if board[i-p,j] == board[i-p-1,j] and board[i-p,j] != 0 and [i-p-1,j] not in mergedList:
                        board[i-p-1,j] = board[i-p-1,j]+1
                        board[i-p,j] = 0
                        score += 2**(board[i-p-1,j])
                        mergedList.append([i-p-1,j])
                if i == 3:
                    for p in range(i):
                        if board[i-p-1,j] == 0:
                            board[i-p-1,j] = board[i-p,j]
                            board[i-p,j] = 0
                        else: break
                    if board[i-p,j] == board[i-p-1,j] and board[i-p,j] != 0 and [i-p-1,j] not in mergedList:
                        board[i-p-1,j] = board[i-p-1,j]+1
                        board[i-p,j] = 0
                        score += 2**(board[i-p-1,j])
                        mergedList.append([i-p-1,j])
    if direction == 1:
        for i in [2,1,0]:
            for j in range(4):
                if i == 2:
                    if board[i+1,j] == 0:
                        board[i+1,j] = board[i,j]
                        board[i,j] = 0
                    if board[i,j] == board[i+1,j] and board[i,j] != 0 and [i+1,j] not in mergedList:
                        board[i+1,j] = board[i+1,j]+1
                        board[i,j] = 0
                        score += 2**(board[i+1,j])
                        mergedList.append([i+1,j])
                if i == 1:
                    for p in range(2):
                        if board[i+p+1,j] == 0:
                            board[i+p+1,j] = board[i+p,j]
                            board[i+p,j] = 0
                        else: break
                    if board[i+p,j] == board[i+p+1,j] and board[i+p,j] != 0 and [i+p+1,j] not in mergedList:
                        board[i+p+1,j] = board[i+p+1,j]+1
                        board[i+p,j] = 0
                        score += 2**(board[i+p+1,j])
                        mergedList.append([i+p+1,j])
                if i == 0:
                    for p in range(3):
                        if board[i+p+1,j] == 0:
                            board[i+p+1,j] = board[i+p,j]
                            board[i+p,j] = 0
                        else: break
                    if board[i+p,j] == board[i+p+1,j] and board[i+p,j] != 0 and [i+p+1,j] not in mergedList:
                        board[i+p+1,j] = board[i+p+1,j]+1
                        board[i+p,j] = 0
                        score += 2**(board[i+p+1,j])
                        mergedList.append([i+p+1,j])
    if direction == 2:
        for j in [1,2,3]:
            for i in range(4):
                if j == 1:
                    if board[i,j-1] == 0:
                        board[i,j-1] = board[i,j]
                        board[i,j] = 0
                    if board[i,j] == board[i,j-1] and board[i,j] != 0 and [i,j-1] not in mergedList:
                        board[i,j-1] = board[i,j-1]+1
                        board[i,j] = 0
                        score += 2**(board[i,j-1])
                        mergedList.append([i,j-1])
                if j == 2:
                    for p in range(j):
                        if board[i,j-p-1] == 0:
                            board[i,j-p-1] = board[i,j-p]
                            board[i,j-p] = 0
                        else: break
                    if board[i,j-p] == board[i,j-p-1] and board[i,j-p] != 0 and [i,j-p-1] not in mergedList:
                        board[i,j-p-1] = board[i,j-p-1]+1
                        board[i,j-p] = 0
                        score += 2**(board[i,j-p-1])
                        mergedList.append([i,j-p-1])
                if j == 3:
                    for p in range(j):
                        if board[i,j-p-1] == 0:
                            board[i,j-p-1] = board[i,j-p]
                            board[i,j-p] = 0
                        else: break
                    if board[i,j-p] == board[i,j-p-1] and board[i,j-p] != 0 and [i,j-p-1] not in mergedList:
                        board[i,j-p-1] = board[i,j-p-1]+1
                        board[i,j-p] = 0
                        score += 2**(board[i,j-p-1])
                        mergedList.append([i,j-p-1])
    if direction == 3:
        for j in [2,1,0]:
            for i in range(4):
                if j == 2:
                    if board[i,j+1] == 0:
                        board[i,j+1] = board[i,j]
                        board[i,j] = 0
                    if board[i,j] == board[i,j+1] and board[i,j] != 0 and [i,j+1] not in mergedList:
                        board[i,j+1] = board[i,j+1]+1
                        board[i,j] = 0
                        score += 2**(board[i,j+1])
                        mergedList.append([i,j+1])
                if j == 1:
                    for p in range(2):
                        if board[i,j+p+1] == 0:
                            board[i,j+p+1] = board[i,j+p]
                            board[i,j+p] = 0
                        else: break
                    if board[i,j+p] == board[i,j+p+1] and board[i,j+p] != 0 and [i,j+p+1] not in mergedList:
                        board[i,j+p+1] = board[i,j+p+1]+1
                        board[i,j+p] = 0
                        score += 2**(board[i,j+p+1])
                        mergedList.append([i,j+p+1])
                if j == 0:
                    for p in range(3):
                        if board[i,j+p+1] == 0:
                            board[i,j+p+1] = board[i,j+p]
                            board[i,j+p] = 0
                        else: break
                    if board[i,j+p] == board[i,j+p+1] and board[i,j+p] != 0 and [i,j+p+1] not in mergedList:
                        board[i,j+p+1] = board[i,j+p+1]+1
                        board[i,j+p] = 0
                        score += 2**(board[i,j+p+1])
                        mergedList.append([i,j+p+1])

    if not np.array_equal(preBoard,board):
        moves += 1
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

# Key listening
def on_press(key):
    global board
    if not gameEnd:
        if "up" in str(key):
            move(board, 0)
        if "down" in str(key):
            move(board, 1)
        if "left" in str(key):
            move(board, 2)
        if "right" in str(key):
            move(board, 3)

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press)
listener.start()
