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
def lcreation():
    f = open('data.csv','r')
    g = open('timetable.csv','w+',newline = '')
    w = csv.writer(g)
    w.writerow(['Day','1','2','3','4','5','6','7','8','9'])
    r = csv.reader(f)
    l1 = list(r)
    d9 = {'9E':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'9F':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'9G':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'9H':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'9J':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']]}
    d10 = {'10E':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'10F':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'10G':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'10H':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'10J':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']]}
    j = 0
    for i in range(1,len(l1)):
        k = 0
        while k < int(l1[i][2]):
            l = l1[i][3]
            if '9' in l:
                d9[l][j].append(l1[i][0])
            if '10' in l:
                d10[l][j].append(l1[i][0])
            j += 1
            if j > 4:
                j = 0
            k += 1
    for i in d9:
        d9[i].insert(0,[i])
    for i in d10:
        d10[i].insert(0,[i])
    for i in d9:
        w.writerows(d9[i])
        w.writerow([])
    for i in d10:
        w.writerows(d10[i])
        w.writerow([])
    print(d9)
    print(d10)
    f.close()
    g.close()
            
lcreation()
    
            
