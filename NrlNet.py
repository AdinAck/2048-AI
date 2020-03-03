import os.path
import numpy as np
import game as g

# Variable definitions
hWidth = 4

# Functions
def sigmoid(x):
    return 1/(1+np.exp(-x,dtype=np.complex128))


# Get output from input
def getOutput(game,w):
    a = game.board
    for i in range(np.size(w,0)):
        a = sigmoid(np.dot(a.flatten(),w[i]))
        # a = np.maximum(0,np.dot(a.flatten(),w[i]))
    a.shape = 4,4
    return sigmoid(np.sum(a,0))

def train(genSize, iterations, threshold, mutationFactor, hDepth=None, model=None, outputModel=False, outputLog=False):
    if outputLog:
        f = open("log.txt", 'w')
    elif outputLog != False:
        f = open(outputLog, 'w')
    if model != None:
        wList = np.load(model)
        hDepth = np.size(wList, 1)-1
        w = wList[0]
    else:
        wList = np.array([],dtype=np.complex128)
        w = np.ones((hDepth+1,hWidth**2,hWidth**2))
    print("Beginning train session from {0}.\nHidden layers: {1}\nGeneration size: {2}\nIterations: {3}\
    \nFitness threshold: {4}\nMutationFactor".format(model,np.size(w,0)-1,genSize,iterations,threshold,mutationFactor))
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
                if j < 1 and model == None:
                    wList = np.append(wList, w)
            print("Epoch: ",j)
            print("Worst: ",np.sort(scores)[0])
            print("Best: ",np.sort(scores)[-1])
            print("Average: ",np.average(scores))
            print("====================")
            if outputLog != False:
                f.write(str(j)+"\t"+str(np.sort(scores)[0])+"\t"+str(np.sort(scores)[-1])+"\t"+str(np.average(scores))+"\n")
            wList = improve(genSize, wList, hDepth, scores, threshold, mutationFactor)
    except KeyboardInterrupt:
        print("\nInterrupted, closing log and saving model...\n")
    print("Session complete from model \"{0}\".\nHidden layers: {1}\nGeneration size: {2}\nIterations: {3}\
    \nFitness threshold: {4}\nMutationFactor: {5}\n".format(model,np.size(w,0)-1,genSize,j,threshold,mutationFactor))
    if outputModel:
        outputModel = model
    elif not outputModel:
        outputModel = None
    if outputLog != False:
        f.close()
    if outputModel != False:
        np.save(outputModel, wList)
    print("Log saved as: {0}\nModel saved as: {1}".format(outputLog,outputModel))

def improve(genSize, wList, hDepth, scores, threshold, mutationFactor):
    try:
        wList.shape = genSize,hDepth+1,hWidth**2,hWidth**2
    except ValueError:
        raise Exception("Model generation size does not match current generation size.")
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
