import numpy as np
import random
from pynput import keyboard

# board = np.zeros((4,4))
board = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
# board = np.array([[0,0,0,0],[0,0,0,0],[2,2,2,2],[2,2,2,2]])



def genRandomBlock(board):
    isZero = np.array([])
    for i in range(4):
        for j in range(4):
            if board[i,j] == 0:
                isZero = np.append(isZero, [i,j])
    try:
        isZero.shape = np.size(isZero)//2,2
        newBlockPos = isZero[random.randint(0,np.size(isZero,0)-1)]
        board[int(newBlockPos[0]),int(newBlockPos[1])] = int(1+random.randint(6,10)/10)*2
    except ValueError:
        print("This should not happen, attempted to place random block in board with no zeros?")

genRandomBlock(board)
genRandomBlock(board)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(board)

def move(board, direction):
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
                        board[i-1,j] = board[i-1,j]*2
                        board[i,j] = 0
                        mergedList.append([i-1,j])
                if i == 2:
                    for p in range(i):
                        if board[i-p-1,j] == 0:
                            board[i-p-1,j] = board[i-p,j]
                            board[i-p,j] = 0
                        else: break
                    if board[i-p,j] == board[i-p-1,j] and board[i-p,j] != 0 and [i-p-1,j] not in mergedList:
                        board[i-p-1,j] = board[i-p-1,j]*2
                        board[i-p,j] = 0
                        mergedList.append([i-p-1,j])
                if i == 3:
                    for p in range(i):
                        if board[i-p-1,j] == 0:
                            board[i-p-1,j] = board[i-p,j]
                            board[i-p,j] = 0
                        else: break
                    if board[i-p,j] == board[i-p-1,j] and board[i-p,j] != 0 and [i-p-1,j] not in mergedList:
                        board[i-p-1,j] = board[i-p-1,j]*2
                        board[i-p,j] = 0
                        mergedList.append([i-p-1,j])
    if direction == 1:
        for i in [2,1,0]:
            for j in range(4):
                if i == 2:
                    if board[i+1,j] == 0:
                        board[i+1,j] = board[i,j]
                        board[i,j] = 0
                    if board[i,j] == board[i+1,j] and board[i,j] != 0 and [i+1,j] not in mergedList:
                        board[i+1,j] = board[i+1,j]*2
                        board[i,j] = 0
                        mergedList.append([i+1,j])
                        print("Moved {0} into the mergedList".format([i+1,j]))
                if i == 1:
                    for p in range(2):
                        if board[i+p+1,j] == 0:
                            board[i+p+1,j] = board[i+p,j]
                            board[i+p,j] = 0
                        else: break
                    if board[i+p,j] == board[i+p+1,j] and board[i+p,j] != 0 and [i+p+1,j] not in mergedList:
                        board[i+p+1,j] = board[i+p+1,j]*2
                        board[i+p,j] = 0
                        mergedList.append([i+p+1,j])
                        print("Moved {0} into the mergedList".format([i+1,j]))
                if i == 0:
                    for p in range(3):
                        if board[i+p+1,j] == 0:
                            board[i+p+1,j] = board[i+p,j]
                            board[i+p,j] = 0
                        else: break
                    if board[i+p,j] == board[i+p+1,j] and board[i+p,j] != 0 and [i+p+1,j] not in mergedList:
                        board[i+p+1,j] = board[i+p+1,j]*2
                        board[i+p,j] = 0
                        mergedList.append([i+p+1,j])
                        print("Moved {0} into the mergedList".format([i+1,j]))

    if not np.array_equal(preBoard,board):
        genRandomBlock(board)
        print("\n\n\n")
        print(board)

# Key listening
def on_press(key):
    global board
    if "up" in str(key):
        move(board, 0)
    if "down" in str(key):
        move(board, 1)
    if "left" in str(key):
        move(board, 2)
    if "right" in str(key):
        move(board, 3)
    try:
        # print('{0} pressed'.format(key.char))
        pass
    except AttributeError:
        # print('{0} pressed'.format(key))
        pass

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press)
listener.start()
