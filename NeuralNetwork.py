import os.path
import numpy as np
import game as g

hWidth = 4
hDepth = 4


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

def train(epochSize, iterations, threshold, randomFactor):
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
                order = np.zeros(4)
                for k in range(len(order)):
                    if np.max(o) == o[0]:
                        order[k] = 0
                        o[0] = 0
                    elif np.max(o) == o[1]:
                        order[k] = 1
                        o[1] = 0
                    elif np.max(o) == o[2]:
                        order[k] = 2
                        o[2] = 0
                    elif np.max(o) == o[3]:
                        order[k] = 3
                        o[3] = 0
                if not game.move(order[0]):
                    if not game.move(order[1]):
                        if not game.move(order[2]):
                            game.move(order[3])
                o = getOutput(game,w)
            scores = np.append(scores, game.score)
            if j < 1:
                wList = np.append(wList, w)
        print("Epoch: ",j)
        print("Worst: ",np.sort(scores)[0])
        print("Best: ",np.sort(scores)[-1])
        print("Average: ",np.average(scores))
        print("====================")
        f.write(str(j)+"\t"+str(np.sort(scores)[0])+"\t"+str(np.sort(scores)[-1])+"\t"+str(np.average(scores))+"\n")
        wList = improve(epochSize, wList, scores, threshold, randomFactor)
    f.close()
    np.save("model"+str(p)+".npy", wList)

def trainFromModel(modelName,epochSize, iterations, threshold, randomFactor):
    p = 0
    while os.path.exists("log"+str(p)+".txt"):
        p += 1
    f = open("log"+str(p)+".txt", 'w')
    w = np.ones((hDepth+1,hWidth**2,hWidth**2))
    wList = np.load(modelName)
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
                order = np.zeros(4)
                for k in range(len(order)):
                    if np.max(o) == o[0]:
                        order[k] = 0
                        o[0] = 0
                    elif np.max(o) == o[1]:
                        order[k] = 1
                        o[1] = 0
                    elif np.max(o) == o[2]:
                        order[k] = 2
                        o[2] = 0
                    elif np.max(o) == o[3]:
                        order[k] = 3
                        o[3] = 0
                if not game.move(order[0]):
                    if not game.move(order[1]):
                        if not game.move(order[2]):
                            game.move(order[3])
                o = getOutput(game,w)
            scores = np.append(scores, game.score)
            
        print("Epoch: ",j)
        print("Worst: ",np.sort(scores)[0])
        print("Best: ",np.sort(scores)[-1])
        print("Average: ",np.average(scores))
        print("====================")
        f.write(str(j)+"\t"+str(np.sort(scores)[0])+"\t"+str(np.sort(scores)[-1])+"\t"+str(np.average(scores))+"\n")
        wList = improve(epochSize, wList, scores, threshold, randomFactor)
    f.close()
    np.save("model"+str(p)+".npy", wList)

def improve(epochSize, wList, scores, threshold,randomFactor):
    wList.shape = epochSize,hDepth+1,hWidth**2,hWidth**2
    bestList = np.array([])
    for i in range(int(epochSize*(threshold/100))):
        scores[[np.argmax(scores)][0]] = -1
        bestList = np.append(bestList, [np.argmax(scores)][0])
    bestList = np.repeat(bestList, 100//threshold)
    for i in range(epochSize):
        if scores[i] != -1:
                wList[i] = wList[int(bestList[i])] + wList[int(bestList[i])]*randomFactor*np.random.random((hDepth+1,hWidth**2,hWidth**2)) - randomFactor/2
    return wList
trainFromModel("model7.npy",500,5,2,1)
