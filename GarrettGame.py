import os
import numpy as np
import random
import pygame
import math

width = 6
height = 4

board = np.zeros((height,width),int)
score = 0
gameEnd = False

def genRandomBlock(board):
    zeroList = np.array([])
    for i in range(height):
        for j in range(width):
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
# print(board)
# print("Score: {0}".format(score))

def move(direction, board):
    global gameEnd
    global score
    preboard = np.array(board)
    if direction == 0: #UP
        xRange = np.arange(0,width)
        for x in xRange:
            lastNumber = board[0,x]
            lastNumIndex = 0
            yRange = np.arange(1,height)

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
        xRange = np.arange(0,width)
        for x in xRange:
            lastNumber = board[height-1,x]
            lastNumIndex = height-1
            yRange = np.arange(height-2,-1,-1)
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
        yRange = np.arange(0,height)
        for y in yRange:
            lastNumber = board[y,0]
            lastNumIndex = 0
            xRange = np.arange(1,width)
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
        yRange = np.arange(0,height)
        for y in yRange:
            lastNumber = board[y,width-1]
            lastNumIndex = width-1
            xRange = np.arange(width-2,-1,-1)
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
        # print(board)
        # print("Score: {0}".format(score))
        gameTest = True
        for y in range(0,height):
            for x in range(0,width):
                if x != width-1:
                    if board[y,x] == board[y,x+1]:
                        gameTest = False
                if y != height-1:
                    if board[y,x] == board[y+1,x]:
                        gameTest = False
        if gameTest:
            gameEnd = True

pygame.init()

win = pygame.display.set_mode(size=(1280,720),flags=pygame.RESIZABLE)
pygame.display.set_caption("2048")

defaultScheme = np.array([["roboto","roboto"],               # Font 1 and 2
                          [(187,173,160),(205,193,179)],     # Board color and square color
                          [(238,228,218),(54, 53, 55)],      # 2 tile block color and text color
                          [(236,224,202),(54, 53, 55)],      # 4 tile block color and text color
                          [(243,176,123),(253, 253, 255)],   # etc...
                          [(245,149,99),(253, 253, 255)],
                          [(239,128,94),(253, 253, 255)],
                          [(247,93,57),(253, 253, 255)],
                          [(236,207,113),(253, 253, 255)],
                          [(168,227,20),(253, 253, 255)],
                          [(43,168,74),(253, 253, 255)],
                          [(15,139,141),(253, 253, 255)],
                          [(41,50,65),(253, 253, 255)],
                          [(4,15,15),(253, 253, 255)]])

schemeList = np.array([defaultScheme])

scheme = schemeList[0]

fontFace1 = scheme[0][0]
fontFace2 = scheme[0][1]

boardColor = scheme[1][0]
squareColor = scheme[1][1]

run = True
while run:
    # Close window when X is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode(size=(event.w,event.h),flags=pygame.RESIZABLE)

    boardSizeX = int((pygame.display.get_surface().get_size()[0]**2+pygame.display.get_surface().get_size()[1]**2)**(1/2)*(width/height)//2.5)
    bufferSize = boardSizeX//width//12
    boardSizeX = boardSizeX-bufferSize
    squareSize = (boardSizeX-(bufferSize*(width+1)))//width
    boardSizeX = squareSize*width+bufferSize*(width+1)
    boardSizeY = bufferSize*(height+1)+(squareSize*height)
    squareCoord = pygame.display.get_surface().get_size()[0]//2-boardSizeX//2+bufferSize,pygame.display.get_surface().get_size()[1]//2-boardSizeY//2+bufferSize

    win.fill((255,255,255))
    pygame.draw.rect(win, boardColor, (squareCoord[0]-bufferSize,squareCoord[1]-bufferSize,boardSizeX,boardSizeY))

    font = pygame.font.SysFont(fontFace2, 48)
    text = font.render("Score: "+str(score), True, boardColor)
    win.blit(text,(squareCoord[0]-bufferSize,squareCoord[1]-bufferSize-text.get_height()))



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

    if keys[pygame.K_SPACE]:
        move(0, board)
        move(3, board)
        move(1, board)
        move(2, board)

    for i in range(height):
        for j in range(width):
            pygame.draw.rect(win, (205,193,179), (squareCoord[0]+j*(bufferSize+squareSize),squareCoord[1]+i*(bufferSize+squareSize),squareSize,squareSize))

    for i in range(height):
        for j in range(width):
            if board[i,j] != 0:
                if board[i,j] == 1:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 2:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 3:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 4:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 5:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 6:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 7:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 8:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 9:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 10:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] == 11:
                    blockColor = scheme[board[i,j]+1][0]
                    textColor = scheme[board[i,j]+1][1]
                if board[i,j] > 11:
                    blockColor = scheme[-1][0]
                    textColor = scheme[-1][1]
                pygame.draw.rect(win, blockColor, (squareCoord[0]+j*(bufferSize+squareSize),squareCoord[1]+i*(bufferSize+squareSize),squareSize,squareSize))
                font = pygame.font.SysFont(fontFace1, int(squareSize/(1+(len(str(2**board[i,j]))*.5))))
                text = font.render(str(2**board[i,j]), True, textColor)
                win.blit(text,(squareCoord[0]+j*(bufferSize+squareSize)+squareSize//2 - text.get_width() // 2, squareCoord[1]+i*(bufferSize+squareSize)+squareSize//2 - text.get_height() // 2))

    if gameEnd:
        s = pygame.Surface((boardSizeX,boardSizeY))
        s.set_alpha(150)
        s.fill((boardColor))
        win.blit(s, (squareCoord[0]-bufferSize,squareCoord[1]-bufferSize))
        font = pygame.font.SysFont(fontFace2, 48)
        text = font.render("Oops! Game Over!", True, scheme[2][1])
        win.blit(text,(pygame.display.get_surface().get_size()[0]//2-text.get_width()//2,pygame.display.get_surface().get_size()[1]//2-text.get_height()//2))

    pygame.display.update()

pygame.quit()
exit()
