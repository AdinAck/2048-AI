import numpy as np
import random

class Game:
    def __init__(self):
        self.board = np.zeros((4,4),np.float64)
        self.score = 0
        self.gameEnd = False
        self.moves = 0
        self.verbose = False
        self.genRandomBlock()
        self.genRandomBlock()

    def genRandomBlock(self):
        zeroList = np.array([])
        for i in range(4):
            for j in range(4):
                if self.board[i,j] == 0:
                    zeroList = np.append(zeroList, [i,j])
        try:
            zeroList.shape = np.size(zeroList)//2,2
            newBlockPos = zeroList[random.randint(0,np.size(zeroList,0)-1)]
            self.board[int(newBlockPos[0]),int(newBlockPos[1])] = int(1+random.randint(6,10)/10)
        except ValueError:
            print("This should not happen, attempted to place random block in board with no zeros?")

        return zeroList

    def move(self, direction):
        preboard = np.array(self.board)
        mergedList = []
        if direction == 0:
            if self.verbose:
                print("Up")
            for i in [1,2,3]:
                for j in range(4):
                    if i == 1:
                        if self.board[i-1,j] == 0:
                            self.board[i-1,j] = self.board[i,j]
                            self.board[i,j] = 0
                        if self.board[i,j] == self.board[i-1,j] and self.board[i,j] != 0 and [i-1,j] not in mergedList:
                            self.board[i-1,j] = self.board[i-1,j]+1
                            self.board[i,j] = 0
                            self.score += 2**(self.board[i-1,j])
                            mergedList.append([i-1,j])
                    if i == 2:
                        for p in range(i):
                            if self.board[i-p-1,j] == 0:
                                self.board[i-p-1,j] = self.board[i-p,j]
                                self.board[i-p,j] = 0
                            else: break
                        if self.board[i-p,j] == self.board[i-p-1,j] and self.board[i-p,j] != 0 and [i-p-1,j] not in mergedList:
                            self.board[i-p-1,j] = self.board[i-p-1,j]+1
                            self.board[i-p,j] = 0
                            self.score += 2**(self.board[i-p-1,j])
                            mergedList.append([i-p-1,j])
                    if i == 3:
                        for p in range(i):
                            if self.board[i-p-1,j] == 0:
                                self.board[i-p-1,j] = self.board[i-p,j]
                                self.board[i-p,j] = 0
                            else: break
                        if self.board[i-p,j] == self.board[i-p-1,j] and self.board[i-p,j] != 0 and [i-p-1,j] not in mergedList:
                            self.board[i-p-1,j] = self.board[i-p-1,j]+1
                            self.board[i-p,j] = 0
                            self.score += 2**(self.board[i-p-1,j])
                            mergedList.append([i-p-1,j])
        if direction == 1:
            if self.verbose:
                print("Down")
            for i in [2,1,0]:
                for j in range(4):
                    if i == 2:
                        if self.board[i+1,j] == 0:
                            self.board[i+1,j] = self.board[i,j]
                            self.board[i,j] = 0
                        if self.board[i,j] == self.board[i+1,j] and self.board[i,j] != 0 and [i+1,j] not in mergedList:
                            self.board[i+1,j] = self.board[i+1,j]+1
                            self.board[i,j] = 0
                            self.score += 2**(self.board[i+1,j])
                            mergedList.append([i+1,j])
                    if i == 1:
                        for p in range(2):
                            if self.board[i+p+1,j] == 0:
                                self.board[i+p+1,j] = self.board[i+p,j]
                                self.board[i+p,j] = 0
                            else: break
                        if self.board[i+p,j] == self.board[i+p+1,j] and self.board[i+p,j] != 0 and [i+p+1,j] not in mergedList:
                            self.board[i+p+1,j] = self.board[i+p+1,j]+1
                            self.board[i+p,j] = 0
                            self.score += 2**(self.board[i+p+1,j])
                            mergedList.append([i+p+1,j])
                    if i == 0:
                        for p in range(3):
                            if self.board[i+p+1,j] == 0:
                                self.board[i+p+1,j] = self.board[i+p,j]
                                self.board[i+p,j] = 0
                            else: break
                        if self.board[i+p,j] == self.board[i+p+1,j] and self.board[i+p,j] != 0 and [i+p+1,j] not in mergedList:
                            self.board[i+p+1,j] = self.board[i+p+1,j]+1
                            self.board[i+p,j] = 0
                            self.score += 2**(self.board[i+p+1,j])
                            mergedList.append([i+p+1,j])
        if direction == 2:
            if self.verbose:
                print("Left")
            for j in [1,2,3]:
                for i in range(4):
                    if j == 1:
                        if self.board[i,j-1] == 0:
                            self.board[i,j-1] = self.board[i,j]
                            self.board[i,j] = 0
                        if self.board[i,j] == self.board[i,j-1] and self.board[i,j] != 0 and [i,j-1] not in mergedList:
                            self.board[i,j-1] = self.board[i,j-1]+1
                            self.board[i,j] = 0
                            self.score += 2**(self.board[i,j-1])
                            mergedList.append([i,j-1])
                    if j == 2:
                        for p in range(j):
                            if self.board[i,j-p-1] == 0:
                                self.board[i,j-p-1] = self.board[i,j-p]
                                self.board[i,j-p] = 0
                            else: break
                        if self.board[i,j-p] == self.board[i,j-p-1] and self.board[i,j-p] != 0 and [i,j-p-1] not in mergedList:
                            self.board[i,j-p-1] = self.board[i,j-p-1]+1
                            self.board[i,j-p] = 0
                            self.score += 2**(self.board[i,j-p-1])
                            mergedList.append([i,j-p-1])
                    if j == 3:
                        for p in range(j):
                            if self.board[i,j-p-1] == 0:
                                self.board[i,j-p-1] = self.board[i,j-p]
                                self.board[i,j-p] = 0
                            else: break
                        if self.board[i,j-p] == self.board[i,j-p-1] and self.board[i,j-p] != 0 and [i,j-p-1] not in mergedList:
                            self.board[i,j-p-1] = self.board[i,j-p-1]+1
                            self.board[i,j-p] = 0
                            self.score += 2**(self.board[i,j-p-1])
                            mergedList.append([i,j-p-1])
        if direction == 3:
            if self.verbose:
                print("Right")
            for j in [2,1,0]:
                for i in range(4):
                    if j == 2:
                        if self.board[i,j+1] == 0:
                            self.board[i,j+1] = self.board[i,j]
                            self.board[i,j] = 0
                        if self.board[i,j] == self.board[i,j+1] and self.board[i,j] != 0 and [i,j+1] not in mergedList:
                            self.board[i,j+1] = self.board[i,j+1]+1
                            self.board[i,j] = 0
                            self.score += 2**(self.board[i,j+1])
                            mergedList.append([i,j+1])
                    if j == 1:
                        for p in range(2):
                            if self.board[i,j+p+1] == 0:
                                self.board[i,j+p+1] = self.board[i,j+p]
                                self.board[i,j+p] = 0
                            else: break
                        if self.board[i,j+p] == self.board[i,j+p+1] and self.board[i,j+p] != 0 and [i,j+p+1] not in mergedList:
                            self.board[i,j+p+1] = self.board[i,j+p+1]+1
                            self.board[i,j+p] = 0
                            self.score += 2**(self.board[i,j+p+1])
                            mergedList.append([i,j+p+1])
                    if j == 0:
                        for p in range(3):
                            if self.board[i,j+p+1] == 0:
                                self.board[i,j+p+1] = self.board[i,j+p]
                                self.board[i,j+p] = 0
                            else: break
                        if self.board[i,j+p] == self.board[i,j+p+1] and self.board[i,j+p] != 0 and [i,j+p+1] not in mergedList:
                            self.board[i,j+p+1] = self.board[i,j+p+1]+1
                            self.board[i,j+p] = 0
                            self.score += 2**(self.board[i,j+p+1])
                            mergedList.append([i,j+p+1])

        if not np.array_equal(preboard,self.board):
            self.moves += 1
            zeroList = self.genRandomBlock()
            if self.verbose:
                print(self.board)
                print("Score: {0}".format(self.score))
            if np.size(zeroList,0) == 1:
                self.gameEnd = True
                for i in [1,2]:
                    for j in range(4):
                        if self.board[i,j] == self.board[i-1,j] or self.board[i,j] == self.board[i+1,j]:
                            self.gameEnd = False
                for j in [1,2]:
                    for i in range(4):
                        if self.board[i,j] == self.board[i,j-1] or self.board[i,j] == self.board[i,j+1]:
                            self.gameEnd = False
        else: return False
        return True
        #comment
# # Key listening
# def on_press(key):
#     global self.board
#     if not self.gameEnd:
#         if "up" in str(key):
#             move(self.board, 0)
#         if "down" in str(key):
#             move(self.board, 1)
#         if "left" in str(key):
#             move(self.board, 2)
#         if "right" in str(key):
#             move(self.board, 3)
#
# # Collect events until released
# with keyself.board.Listener(on_press=on_press) as listener:
#     listener.join()
#
# # ...or, in a non-blocking fashion:
# listener = keyself.board.Listener(on_press=on_press)
# listener.start()
