import csv
import random
daykeys = {'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5}
days = list(daykeys.keys())
def createblank():
    f = open('timetable.csv','w',newline ='')
    w = csv.writer(f)
    for i in range(5):
        l = [days[i]]
        for j in range(9):
            l.append([])
        w.writerow(l)
    f.close()
createblank()

def addperiod():
    with open('timetable.csv','r',newline='') as f:
        r = csv.reader(f)
        name = input("Enter name of teacher: ")
        subject = input("Enter subject thought: ")
        prds = int(input("Enter number of periods a week: "))
        y = list(r)
    for i in range(prds):
        a = random.randint(0,4)
        b = random.randint(1, 8)
        y[a][b] = [name,subject]
    with open('timetable.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerows(y)
addperiod()
