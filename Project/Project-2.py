import csv
def info():
    f = open('data.csv','w+',newline = '')
    w = csv.writer(f)
    w.writerow(['Subject','Teacher','Number of periods','Class'])
    while True:
        sub = input("Enter subject name:")
        teacher = input("Enter teacher name:")
        nump = int(input("Enter the number of periods:"))
        tecclass = input("Enter the class which the teacher handles:")
        yorn = input("Do you want to add more records?(y/n):")
        w.writerow([sub,teacher,nump,tecclass])
        if yorn == 'n':
            break
    f.close()
#info()
def ctttt():
    p = open('teachertt.csv','w',newline = '')
    w = csv.writer(p)
    l = [[],[],[],[],[],[],[],[],[]]
    for i in range(5):
        w.writerow(l)
    p.close()
ctttt()

import random as ran
l2 = []
def addteach(ints):
    while len(l2) != ints: 
        with open('teachertt.csv','r') as g:
            r = csv.reader(g)
            table = list(r)
        F = open("data.csv",'r')
        r = csv.reader(F)
        w = csv.writer(g)
        l = list(r)
        print(table)
        rand = ran.randint(1,ints)
        if rand not in l2:
            l2.append(rand)
            print(l2)
            teach = str(l[rand][-1])
            i=0
            while i<9:
                j=ran.randint(0,8)
                k=ran.randint(0,4)
                print(j,k)
                if table[k][j] == '[]':
                    table[k][j]=[teach]
                    i+=1
            print(l[rand][1])
            print(table)
            h = open('teachertt.csv','w')
            w2 = csv.writer(h)
            w2.writerow([l[rand][1]])
            w2.writerows(table)
            F.close()
ints = 6
addteach(ints)
