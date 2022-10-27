import csv
import random
def createdict():
    d1 = {}
    with open('teachertt.csv','r') as g:
            r = csv.reader(g)
            table = list(r)
    F = open("data.csv",'r')
    r = csv.reader(F)
    l = list(r)
    for i in range(1,len(l)):
        d1[l[i][1]] = table
    return d1

import random as rn
def addteach(ints,d1):
    F = open("data.csv",'r')
    r = csv.reader(F)
    l = list(r)
    print(l)
    l2 = []
    while len(l2) != ints:   
        rand = rn.randint(1,ints)
        if rand not in l2:
            l2.append(rand)
            teach = str(l[rand][1])
            teaclass = l[rand][-1]
            i = 0
        while i<9:
            day = rn.randint(0,4)
            period = rn.randint(0,8)
            l = d1[teach][day][period]
            if l == []:
                l = [teaclass]
                i += 1          
    print(d1)
            
                

d1 = createdict()
print(d1)
ints = 6
addteach(ints,d1)

