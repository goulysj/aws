import scipy as sp
import numpy as np
import pandas as pd

array1 = open("minCut.txt")

mat1 = np.zeros(200 * 200).reshape(200,200)
for i in range(200):
    line1 = array1.readline()
    t1 = line1.split("\t")
    t1 = np.array(t1[:-1]).astype('float')
    for j in range(len(t1)):
        mat1[i][int(t1[j] - 1)] = 1




array1 = open("minCut.txt")
ajlist = []
for i in range(200):
    line1 = array1.readline()
    t1 = line1.split("\t")
    t1 = np.array(t1[:-1]).astype('int')
    ajlist += [t1]

count = 0
for i in range(1,201):
    count += len(ajlist[str(i)])



array1 = open("minCut.txt")

ajlist = {}
for i in range(200):
    line1 = array1.readline()
    t1 = line1.split("\t")
    ajlist[t1[0]] = t1[1:-1]

def countlist(adlist):
    count = 0
    for index,item in enumerate(list(adlist.keys())):
        count += len(ajlist[item])
    return count
 
def pickitem (ajlist, randomNO):
    totalNO=randomNO
    for index,item in enumerate(list(ajlist.keys())):
        NO= len(ajlist[item])
        if totalNO >NO:
            totalNO -= NO
        else:
            return (item,ajlist[item][totalNO-1])

def sub (ajlist,liveitem,deaditem):       
    for index,item in enumerate(list(ajlist.keys())):
        NO= len(ajlist[item])
        for i in range(NO):
            if ajlist[item][i]== deaditem:
                ajlist[item][i] = liveitem
    return ajlist

def removedup (ajlist,item):
    NO= len(ajlist[item])
    i=j=0
    while j < NO:
        if ajlist[item][i]==item:
            del ajlist[item][i]
            j += 1
        else :
            i += 1
            j += 1
    return ajlist[item]


array1 = open("minCut.txt")

ajlist = {}
for i in range(200):
    line1 = array1.readline()
    t1 = line1.split("\t")
    ajlist[t1[0]] = t1[1:-1]


for i in range(198):
    edgeNO= countlist(ajlist)
    randomNO= np.random.choice(edgeNO)+1
    liveitem, deaditem=pickitem(ajlist,randomNO)
    ajlist= sub(ajlist,liveitem,deaditem)    
    ajlist[liveitem] += ajlist[deaditem]
    del ajlist[deaditem]
    ajlist[liveitem]= removedup(ajlist,liveitem)
    #print(199-i)

edgeNO= countlist(ajlist)
randomNO= np.random.choice(edgeNO)+1
liveitem, deaditem=pickitem(ajlist,randomNO)    
#combine the two list
ajlist[liveitem] += ajlist[deaditem]
del ajlist[deaditem]
ajlist[liveitem]= removedup(ajlist,liveitem)

def minCut(ajlist):
    for i in range(198):
        edgeNO= countlist(ajlist)
        randomNO= np.random.choice(edgeNO)+1
        liveitem, deaditem=pickitem(ajlist,randomNO)
        ajlist= sub(ajlist,liveitem,deaditem)    
        ajlist[liveitem] += ajlist[deaditem]
        del ajlist[deaditem]
        ajlist[liveitem]= removedup(ajlist,liveitem)
    return len(ajlist[liveitem])



array1 = open("minCut.txt")
ajlist = {}
for i in range(200):
    line1 = array1.readline()
    t1 = line1.split("\t")
    ajlist[t1[0]] = t1[1:-1]

minCut(ajlist)

results= []
for i in range(4000):
    for j in range(200):
        array1 = open("minCut.txt")
        ajlist = {}
        for i in range(200):
            line1 = array1.readline()
            t1 = line1.split("\t")
            ajlist[t1[0]] = t1[1:-1]
        results += [minCut(ajlist)]
    print(i,min(results))
