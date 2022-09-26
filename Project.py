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
        add =[]
        total = []
        for i in range(prds):
            a = random.randint(1,5)
            for row in r:
                row = list(row)
                if a != daykeys[row[0]]:
                    total.append(row)
                elif a == daykeys[row[0]]:
                    l = row
                    b = random.randint(1,9)
                    l[b]=[name,subject]
                    total.append(l)
    with open('timetable.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerows(total)
addperiod()
