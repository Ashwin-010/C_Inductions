import csv
import random
def createdict():#To create a dictionary like this{'Jacob': [['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]']]}
    d1 = {}
    with open('teachertt.csv','r') as g:
            r = csv.reader(g)
            table = list(r)
    F = open("data.csv",'r')
    r = csv.reader(F)
    l = list(r)
    for i in range(1,len(l)):#Creates a new key with a blank timetable for 45 periods
        d1[l[i][1]] = table
    return d1

import random as rn
def addteach(ints,d1):
    F = open("data.csv",'r')
    r = csv.reader(F)
    l = list(r)#L contains the data for each and every teacher
    print(l)
    l2 = []
    while len(l2) != ints:   #Condition: To prevent the while loop from overshooting the number of teachers for which the timetable is created
        rand = rn.randint(1,ints)#A random integer to take the details of a specific teacher(A for loop can be used?)
        if rand not in l2:
            l2.append(rand)
            teach = str(l[rand][1])#Teach = teacher's name
            teaclass = l[rand][-1]#Teaclass = The class to be assigned to the teacher
            i = 0
        while i<9:
            day = rn.randint(0,4)#Random integer to find the day
            period = rn.randint(0,8)#Random integer to find the period to which the teacher's class must be assigned
            l = d1[teach][day][period]#List(of the particular day of the particular week to which the class of the teacher must be assigned
            if l == []:
                l = [teaclass]
                i += 1          
    print(d1)#Final list after iterating over all teacher's data
            
                

d1 = createdict()
print(d1)
ints = 6
addteach(ints,d1)

