import os
import numpy as np
import random
import pygame

width = 4
height = 4

board = np.zeros((height,width),int)
# board = np.array([[0,0,0,0,0,0],
#                   [0,0,0,0,0,0],
#                   [-1,-1,-1,0,-2,0],
#                   [-1,-1,-1,0,0,0],
#                   [-1,-1,-1,0,0,0]])
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
                if board[y,x] != 0 and board[y,x] != -1 and board[y,x] != -2:
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
                if board[y,x] != 0 and board[y,x] != -1 and board[y,x] != -2:
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
                if board[y,x] != 0 and board[y,x] != -1 and board[y,x] != -2:
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
                if board[y,x] != 0 and board[y,x] != -1 and board[y,x] != -2:
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
        if np.size(zeroList,0) <= 1:
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

defaultScheme = np.array([["Roboto-Bold.ttf","Roboto-Bold.ttf"],               # Font 1 and 2
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

win = pygame.display.set_mode(size=(1280,720))
displaySize = pygame.display.get_surface().get_size()
boardSizeX = int((displaySize[0]**2+displaySize[1]**2)**(1/2)*(width/height)//2.5)
bufferSize = boardSizeX//width//12
boardSizeX = boardSizeX-bufferSize
squareSize = (boardSizeX-(bufferSize*(width+1)))//width
boardSizeX = squareSize*width+bufferSize*(width+1)
boardSizeY = bufferSize*(height+1)+(squareSize*height)
squareCoord = displaySize[0]//2-boardSizeX//2+bufferSize,displaySize[1]//2-boardSizeY//2+bufferSize

zoom = 1
mouseMove = 0,0
menu = True
run = True
while run:
    # Close window when X is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode(size=(event.w,event.h),flags=pygame.RESIZABLE)
            displaySize = pygame.display.get_surface().get_size()
            boardSizeX = int((displaySize[0]**2+displaySize[1]**2)**(1/2)*(width/height)//2.5)
            bufferSize = boardSizeX//width//12
            boardSizeX = boardSizeX-bufferSize
            squareSize = (boardSizeX-(bufferSize*(width+1)))//width
            boardSizeX = squareSize*width+bufferSize*(width+1)
            boardSizeY = bufferSize*(height+1)+(squareSize*height)
            squareCoord = displaySize[0]//2-boardSizeX//2+bufferSize,displaySize[1]//2-boardSizeY//2+bufferSize
        if event.type == pygame.MOUSEBUTTONDOWN and not gameEnd:
            if event.button == 4:
                zoom = 2
                # squareCoord = int(zoom*squareCoord[0])-pygame.mouse.get_pos()[0],int(zoom*squareCoord[1])-pygame.mouse.get_pos()[1]
                squareCoord = int(zoom*squareCoord[0])-displaySize[0]//2,int(zoom*squareCoord[1])-displaySize[1]//2
                boardSizeX = boardSizeX*zoom
                squareSize = squareSize*zoom
                bufferSize = bufferSize*zoom
            if event.button == 5:
                zoom = .5
                # squareCoord = int(zoom*squareCoord[0])+pygame.mouse.get_pos()[0]//2,int(zoom*squareCoord[1])+pygame.mouse.get_pos()[1]//2
                squareCoord = int(zoom*squareCoord[0])+displaySize[0]//4,int(zoom*squareCoord[1])+displaySize[1]//4
                boardSizeX = boardSizeX*zoom
                squareSize = squareSize*zoom
                bufferSize = bufferSize*zoom

    mouseMove = pygame.mouse.get_rel()
    if pygame.mouse.get_pressed()[0] and not gameEnd:
        squareCoord = squareCoord[0]+mouseMove[0],squareCoord[1]+mouseMove[1]

    win.fill((255,255,255))

    if menu:
        button1Size = 100,50
        button1Pos = displaySize[0]//2,displaySize[1]//(3/2)
        if pygame.mouse.get_pos()[0] <= button1Pos[0]+button1Size[0]//2 and pygame.mouse.get_pos()[0] >= button1Pos[0]-button1Size[0]//2 and pygame.mouse.get_pos()[1] <= button1Pos[1]+button1Size[1]//2 and pygame.mouse.get_pos()[1] >= button1Pos[1]-button1Size[1]//2:
            button1Color = scheme[1][1]
            if pygame.mouse.get_pressed()[0]:
                menu = False
        else:
            button1Color = boardColor
        pygame.draw.rect(win, button1Color, (button1Pos[0]-button1Size[0]//2,button1Pos[1]-button1Size[1]//2,button1Size[0],button1Size[1]))
        font = pygame.font.Font(fontFace2, 32)
        text = font.render("PLAY", True, scheme[2][1])
        win.blit(text,(button1Pos[0]-text.get_width()//2,button1Pos[1]-text.get_height()//2))

        font = pygame.font.Font(fontFace2, 60)
        text = font.render("SUPER 2048", True, scheme[2][1])
        win.blit(text,(displaySize[0]//2-text.get_width()//2,displaySize[1]//(3)-text.get_height()//2))

    if not menu:
        font = pygame.font.Font(fontFace2, 48)
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

        if keys[pygame.K_ESCAPE]:
            menu = True

        for i in range(height):
            for j in range(width):
                if board[i,j] != -1:
                    pygame.draw.rect(win, boardColor, (squareCoord[0]-bufferSize+j*(bufferSize+squareSize),squareCoord[1]-bufferSize+i*(bufferSize+squareSize),bufferSize*2+squareSize,bufferSize*2+squareSize))

        for i in range(height):
            for j in range(width):
                if board[i,j] != -1 and board[i,j] != -2:
                    blockColor = squareColor
                if board[i,j] == -1:
                    blockColor = (255,255,255)
                if board[i,j] == -2:
                    blockColor = scheme[2][1]
                pygame.draw.rect(win, blockColor, (squareCoord[0]+j*(bufferSize+squareSize),squareCoord[1]+i*(bufferSize+squareSize),squareSize,squareSize))

        for i in range(height):
            for j in range(width):
                if board[i,j] != 0 and board[i,j] != -1 and board[i,j] != -2:
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
                    font = pygame.font.Font(fontFace1, int(squareSize/(1+(len(str(2**board[i,j]))*.5))))
                    text = font.render(str(2**board[i,j]), True, textColor)
                    win.blit(text,(squareCoord[0]+j*(bufferSize+squareSize)+squareSize//2 - text.get_width() // 2, squareCoord[1]+i*(bufferSize+squareSize)+squareSize//2 - text.get_height() // 2))

        if gameEnd:
            displaySize = pygame.display.get_surface().get_size()
            boardSizeX = int((displaySize[0]**2+displaySize[1]**2)**(1/2)*(width/height)//2.5)
            bufferSize = boardSizeX//width//12
            boardSizeX = boardSizeX-bufferSize
            squareSize = (boardSizeX-(bufferSize*(width+1)))//width
            boardSizeX = squareSize*width+bufferSize*(width+1)
            boardSizeY = bufferSize*(height+1)+(squareSize*height)
            squareCoord = displaySize[0]//2-boardSizeX//2+bufferSize,displaySize[1]//2-boardSizeY//2+bufferSize

            s = pygame.Surface((boardSizeX,boardSizeY))
            s.set_alpha(150)
            s.fill((boardColor))
            win.blit(s, (squareCoord[0]-bufferSize,squareCoord[1]-bufferSize))
            font = pygame.font.Font(fontFace2, 48)
            text = font.render("Oops! Game Over!", True, scheme[2][1])
            win.blit(text,(displaySize[0]//2-text.get_width()//2,displaySize[1]//2-text.get_height()//(1.8/2)))

            button1Size = 200,50
            button1Pos = displaySize[0]//2+button1Size[0]//2+20,displaySize[1]//(1.8)
            if pygame.mouse.get_pos()[0] <= button1Pos[0]+button1Size[0]//2 and pygame.mouse.get_pos()[0] >= button1Pos[0]-button1Size[0]//2 and pygame.mouse.get_pos()[1] <= button1Pos[1]+button1Size[1]//2 and pygame.mouse.get_pos()[1] >= button1Pos[1]-button1Size[1]//2:
                button1Color = scheme[1][1]
                textColor = scheme[2][1]
                if pygame.mouse.get_pressed()[0]:
                    menu = False
                    gameEnd = False
                    score = 0
                    board = np.zeros((height,width),int)
                    genRandomBlock(board)
                    genRandomBlock(board)
            else:
                button1Color = scheme[2][1]
                textColor = (255,255,255)
            pygame.draw.rect(win, button1Color, (button1Pos[0]-button1Size[0]//2,button1Pos[1]-button1Size[1]//2,button1Size[0],button1Size[1]))
            font = pygame.font.Font(fontFace2, 32)
            text = font.render("PLAY AGAIN", True, textColor)
            win.blit(text,(button1Pos[0]-text.get_width()//2,button1Pos[1]-text.get_height()//2))

            button2Size = 200,50
            button2Pos = displaySize[0]//2-button2Size[0]//2-20,displaySize[1]//(1.8)
            if pygame.mouse.get_pos()[0] <= button2Pos[0]+button2Size[0]//2 and pygame.mouse.get_pos()[0] >= button2Pos[0]-button2Size[0]//2 and pygame.mouse.get_pos()[1] <= button2Pos[1]+button2Size[1]//2 and pygame.mouse.get_pos()[1] >= button2Pos[1]-button2Size[1]//2:
                button1Color = scheme[1][1]
                textColor = scheme[2][1]
                if pygame.mouse.get_pressed()[0]:
                    menu = True
                    gameEnd = False
                    score = 0
                    board = np.zeros((height,width),int)
                    genRandomBlock(board)
                    genRandomBlock(board)
            else:
                button1Color = scheme[2][1]
                textColor = (255,255,255)
            pygame.draw.rect(win, button1Color, (button2Pos[0]-button2Size[0]//2,button2Pos[1]-button2Size[1]//2,button2Size[0],button2Size[1]))
            font = pygame.font.Font(fontFace2, 32)
            text = font.render("MAIN MENU", True, textColor)
            win.blit(text,(button2Pos[0]-text.get_width()//2,button2Pos[1]-text.get_height()//2))

    pygame.display.update()

pygame.quit()
exit()
