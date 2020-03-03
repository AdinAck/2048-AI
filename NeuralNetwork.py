import os.path
import numpy as np
import game as g
from pynput import keyboard
import signal

# Variable definitions
hWidth = 4
hDepth = 4

# Functions
def sigmoid(x):
    return 1/(1+np.exp(-x,dtype=np.complex128))


# Get output from input
def getOutput(game,w):
    a = game.board
    for i in range(hDepth+1):
        a = sigmoid(np.dot(a.flatten(),w[i]))
        # a = np.maximum(0,np.dot(a.flatten(),w[i]))
    a.shape = 4,4
    return sigmoid(np.sum(a,0))

def train(genSize, iterations, threshold, mutationFactor, modelName=None):
    p = 0
    while os.path.exists("log"+str(p)+".txt"):
        p += 1
    f = open("log"+str(p)+".txt", 'w')
    w = np.ones((hDepth+1,hWidth**2,hWidth**2))
    if modelName != None:
        wList = np.load(modelName)
    else:
        wList = np.array([],dtype=np.complex128)
    print("Beginning train session from {0}.\nHidden layers: {1}\nGeneration size: {2}\nIterations: {3}\
    \nFitness threshold: {4}\nMutationFactor".format(modelName,np.size(w,0)-1,genSize,iterations,threshold,mutationFactor))
    print("\n====================")
    try:
        for j in range(iterations):
            scores = np.array([],int)
            game = g.Game()
            o = getOutput(game,w)
            for i in range(genSize):
                game = g.Game()
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
                if j < 1 and modelName == None:
                    wList = np.append(wList, w)
            print("Epoch: ",j)
            print("Worst: ",np.sort(scores)[0])
            print("Best: ",np.sort(scores)[-1])
            print("Average: ",np.average(scores))
            print("====================")
            f.write(str(j)+"\t"+str(np.sort(scores)[0])+"\t"+str(np.sort(scores)[-1])+"\t"+str(np.average(scores))+"\n")
            wList = improve(genSize, wList, scores, threshold, mutationFactor)
    except KeyboardInterrupt:
        print("\nInterrupted, closing log and saving model...\n")
    print("Session complete from model \"{0}\".\nHidden layers: {1}\nGeneration size: {2}\nIterations: {3}\
    \nFitness threshold: {4}\nMutationFactor\n".format(modelName,np.size(w,0)-1,genSize,j,threshold,mutationFactor))
    f.close()
    np.save("model"+str(p)+".npy", wList)
    print("Log saved as: {0}\nModel saved as: {1}".format("log"+str(p)+".txt","model"+str(p)+".npy"))

def improve(genSize, wList, scores, threshold,mutationFactor):
    wList.shape = genSize,hDepth+1,hWidth**2,hWidth**2
    bestList = np.array([])
    for i in range(int(genSize*(threshold/100))):
        scores[[np.argmax(scores)][0]] = -1
        bestList = np.append(bestList, [np.argmax(scores)][0])
    bestList = np.repeat(bestList, 100//threshold)
    for i in range(genSize):
        if scores[i] != -1:
            try:
                wList[i] = wList[int(bestList[i])] + wList[int(bestList[i])]*mutationFactor*np.random.random((hDepth+1,hWidth**2,hWidth**2)) - mutationFactor/2
            except IndexError:
                raise Exception("Generation size is not divisible by fitness threshold.")
    return wList

train(100,10000,10,.1)
