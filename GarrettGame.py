import numpy as np
import random
import pygame

width = 4
height = 4

board = np.zeros((height,width),int)
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

# print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(board)
print("Score: {0}".format(score))

def move(direction, board):
    global score
    preboard = np.array(board)
    if direction == 0: #UP
        xRange = np.arange(0,np.size(board,1))
        for x in xRange:
            lastNumber = board[0,x]
            lastNumIndex = 0
            yRange = np.arange(1,np.size(board, 0))

            for y in yRange:
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
        xRange = list(range(len(board[0])))
        for x in xRange:
            lastNumber = board[3,x]
            lastNumIndex = 3
            yRange = np.arange(np.size(board, 0)-2,-1,-1)
            for y in yRange:
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
        yRange = np.arange(0,np.size(board,0)-1)
        for y in yRange:
            lastNumber = board[y,0]
            lastNumIndex = 0
            xRange = np.arange(1,np.size(board,1))
            for x in xRange:
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
        yRange = np.arange(0,np.size(board, 0))
        print(yRange)
        for y in yRange:
            lastNumber = board[y,3]
            lastNumIndex = 3
            xRange = np.arange(np.size(board,1)-2,-1,-1)
            for x in xRange:
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
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
    else: return False
    return True

pygame.init()

winSizeX = 512
bufferSize = 8
squareCoord = bufferSize,bufferSize
squareSize = (winSizeX-((width+1)*bufferSize))//width
winSizeY = bufferSize*(height+1)+(squareSize*height)
win = pygame.display.set_mode((winSizeX,winSizeY))
pygame.display.set_caption("2048")

run = True
while run:
    # Close window when X is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    if not keys[pygame.K_UP]:
        upKey = False
    if not keys[pygame.K_DOWN]:
        downKey = False
    if not keys[pygame.K_LEFT]:
        leftKey = False
    if not keys[pygame.K_RIGHT]:
        rightKey = False

    if keys[pygame.K_UP] and not upKey:
        move(0, board)
        upKey = True
    if keys[pygame.K_DOWN] and not downKey:
        move(1, board)
        downKey = True
    if keys[pygame.K_LEFT] and not leftKey:
        move(2, board)
        leftKey = True
    if keys[pygame.K_RIGHT] and not rightKey:
        move(3, board)
        rightKey = True

    for i in range(height):
        for j in range(width):
            pygame.draw.rect(win, (255,255,255), (squareCoord[0]+j*(bufferSize+squareSize),squareCoord[1]+i*(bufferSize+squareSize),squareSize,squareSize))
    pygame.display.update()

pygame.quit()
