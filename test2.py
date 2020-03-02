import os.path
import numpy as np
import game as g

hWidth = 4
hDepth = 0

def sigmoid(x):
    return 1/(1+np.exp(-x))

# np.random.seed(1)

# Get output from input
def getOutput(game,w):
    a = game.board
    for i in range(hDepth+1):
        a = sigmoid(np.dot(a.flatten(),w[i]))

    a.shape = 4,4
    return sigmoid(np.sum(a,0))

def train(epochSize, iterations):
    p = 0
    while os.path.exists("log"+str(p)+".txt"):
        p += 1
    f = open("log"+str(p)+".txt", 'w')
    w = np.ones((hDepth+1,hWidth**2,hWidth**2))
    wList = np.array([])
    for j in range(iterations):
        scores = np.array([],int)
        game = g.Game()
        o = getOutput(game,w)

        for i in range(epochSize):
            game = g.Game()
            # print(game.board)
            game.verbose = False
            if j >= 1:
                w = wList[i]
            while not game.gameEnd:
                if np.max(o) == o[0]:
                    if not game.move(0):
                        break
                if np.max(o) == o[1]:
                    if not game.move(1):
                        break
                if np.max(o) == o[2]:
                    if not game.move(2):
                        break
                if np.max(o) == o[3]:
                    if not game.move(3):
                        break
                o = getOutput(game,w)
            scores = np.append(scores, game.score)
            if j < 1:
                wList = np.append(wList, w)
        print("Generation: ",j)
        print("Worst: ",np.sort(scores)[0])
        print("Best: ",np.sort(scores)[-1])
        print("Average: ",np.average(scores))
        print("====================")
        f.write(str(j)+"\t"+str(np.sort(scores)[0])+"\t"+str(np.sort(scores)[-1])+"\t"+str(np.average(scores))+"\n")
        wList = improve(epochSize, wList, scores, 10)
    f.close()
    # print("\n\nFinal weights:\n",wList)
    np.save("model"+str(p)+".npy", wList)

def improve(epochSize, wList, scores, threshold):
    wList.shape = epochSize,hDepth+1,hWidth**2,hWidth**2
    bestList = np.array([])
    for i in range(int(epochSize*(threshold/100))):
        scores[[np.argmax(scores)][0]] = -1
        bestList = np.append(bestList, [np.argmax(scores)][0])
    bestList = np.repeat(bestList, 100//threshold)
    for i in range(epochSize):
        if scores[i] != -1:
                wList[i] = wList[int(bestList[i])] + wList[int(bestList[i])]*2*np.random.random((hDepth+1,hWidth**2,hWidth**2)) - 1
    return wList
train(1000,10000)
