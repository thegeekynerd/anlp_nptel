import os
import pandas as pd
import re

cor = pd.read_csv('phy_corpus.txt', sep='\n', header=None)[0]

#speed = '\w+[.]*\w+\s[m][/][s]'
speed = '[0-9]+[.]*[0-9]*\s[m][/][s][^2]'
distance = '[0-9]+[.]*[0-9]*\s[m][^/s2]'
accelaration = '[0-9]+[.]*[0-9]*\s[m][/][s][2]'
time = '[0-9]+[.][0-9]*\s[s]+'

speed_value = []
distance_value = []
accelaration_value = []
time_value = []
bim = []

spd = lambda s: re.findall(speed,s)
dist = lambda s: re.findall(distance,s)
acc = lambda s: re.findall(accelaration,s)
t = lambda s: re.findall(time,s)

def find(val):
    if(val):
        return 1
    else:
        return 0


def element(doc):
    temp = [0,0,0,0]
    if(spd(doc)):
        temp[0]=1
    if(dist(doc)):
        temp[1]=1
    if(acc(doc)):
        temp[2]=1
    if(t(doc)):
        temp[3]=1
    return temp


for doc in cor:
    bim.append(element(doc))

def printm():
    print("Terms       \t",end='')
    for i in range (1,10):
        print("D",i,'\t',end='')

    print("\n\nSpeed       \t",end='')
    for spd in range(0,9):
        print(bim[spd][0],'\t',end='')
    print("\nDistance    \t",end='')
    for d in range(0,9):
        print(bim[d][1],'\t',end='')
    print("\nAccelaration\t",end='')
    for ac in range(0,9):
        print(bim[ac][2],'\t',end='')
    print("\nTime        \t",end='')
    for ti in range(0,9):
        print(bim[ti][3],'\t',end='')
        
        

printm()
