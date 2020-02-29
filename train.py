import sys
import numpy as np
import random
import game as g
# np.set_printoptions(threshold=sys.maxsize)

c = 100 # Generation size
r = 100 # Number of generations
hWidth = 16
hDepth = 8

scores = np.array([],int)
wbList = np.array([])

f = open("log.txt", 'w')

for m in range(c):
    game = g.Game()
    # game.verbose = True

    i = np.array(game.board.flatten())
    h = np.zeros((hDepth,hWidth))
    w = np.ones((hDepth+1,np.size(i),hWidth))
    b = np.ones((hDepth+1,np.size(i),hWidth))
    o = np.zeros(4)

    for j in range(np.size(w,0)):
        for k in range(np.size(w,1)):
            for l in range(np.size(w,2)):
                w[j,k,l] = random.randint(-10,10)/100

    for j in range(np.size(b,0)):
        for k in range(np.size(b,1)):
            for l in range(np.size(b,2)):
                b[j,k,l] = random.randint(-10,10)

    def update(i,h,w,b,o):
        for l in range(hDepth):
            for j in range(hWidth):
                for k in range(np.size(i)):
                    h[l,j] += i[k]*w[l,k,j]+b[l,k,j]
                h[l,j] = max(h[l,j],0)

        for j in range(np.size(o)):
            for k in range(hWidth):
                o[j] += h[l,k]*w[l+1,j,k]+b[l+1,j,k]
            o[j] = max(o[j],0)

    while not game.gameEnd:
        if o[0] == o[1] and o[1] == o[2] and o[2] == o[3]:
            o[random.randint(0,3)]+=1
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
        i = np.array(game.board.flatten())
        update(i,h,w,b,o)

    if game.verbose:
        print("\nGame over!")
        print("====================")
        print("Final Score: {0}".format(game.score))
        print("Number of moves: {0}".format(game.moves))
    scores = np.append(scores, game.score/(game.moves+1))
    wbList = np.append(wbList, [w,b])

wbList.shape = m+1,2,np.size(w)

print("Generation: 0")
print("Worst: ",np.sort(scores)[0])
print("Best: ",np.sort(scores)[-1])
print("Average: ",np.average(scores))
print("====================")
f.write("0\t"+str(np.sort(scores)[0])+"\t"+str(np.sort(scores)[-1])+"\t"+str(np.average(scores))+"\n")

for p in range(r):
    wbList2 = np.array([])
    for m in range(c//4):
        biggestScoreIndex = [np.argmax(scores)][0]
        w = wbList[biggestScoreIndex,0]
        b = wbList[biggestScoreIndex,1]
        w.shape = hDepth+1,np.size(i),hWidth
        b.shape = hDepth+1,np.size(i),hWidth
        scores = np.delete(scores,biggestScoreIndex,0)
        wbList = np.delete(wbList,biggestScoreIndex,0)
        for n in range(4):
            for j in range(np.size(w,0)):
                for k in range(np.size(w,1)):
                    for l in range(np.size(w,2)):
                        w[j,k,l] += w[j,k,l]*random.randint(-10,10)/1000

            for j in range(np.size(b,0)):
                for k in range(np.size(b,1)):
                    for l in range(np.size(b,2)):
                        b[j,k,l] += b[j,k,l]*random.randint(-10,10)/1000

            wbList2 = np.append(wbList2, [w,b])

    wbList2.shape = (m+1)*(n+1),2,np.size(w)
    scores = np.array([],int)
    wbList = np.array([])

    for m in range(c):
        game = g.Game()
        # game.verbose = True

        i = np.array(game.board.flatten())
        h = np.zeros((hDepth,hWidth))
        w = wbList2[m,0]
        b = wbList2[m,1]
        w.shape = hDepth+1,np.size(i),hWidth
        b.shape = hDepth+1,np.size(i),hWidth
        o = np.zeros(4)

        update(i,h,w,b,o)

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

        if game.verbose:
            print("\nGame over!")
            print("====================")
            print("Final Score: {0}".format(game.score))
            print("Number of moves: {0}".format(game.moves))
        scores = np.append(scores, game.score/(game.moves+1))
        # print(game.score,game.moves)
        wbList = np.append(wbList, [w,b])

        wbList.shape = m+1,2,np.size(w)

    print("Generation: ",p+1)
    print("Worst: ",np.sort(scores)[0])
    print("Best: ",np.sort(scores)[-1])
    print("Average: ",np.average(scores))
    print("====================")
    f.write(str(p+1)+"\t"+str(np.sort(scores)[0])+"\t"+str(np.sort(scores)[-1])+"\t"+str(np.average(scores))+"\n")
f.close()
# print("\n\nFinal weights and biases: \n",w,"\n",b)
