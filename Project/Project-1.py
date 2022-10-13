import csv
def info():
    f = open('data.csv','w+',newline = '')
    w = csv.writer(f)
    w.writerow(['Subject','Teacher','Number of periods','Class'])
    while True:
        sub = input("Enter subject name:")
        teacher = input("Enter teacher name:")
        nump = int(input("Enter the number of periods:"))
        tecclass = input("Enter the class which the teacher handles(Enter in roman numerals:")
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
    d1 = {'XE':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'XF':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'XG':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'XH':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']],'XJ':[['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']]}
    j = 0
    for i in range(1,len(l1)):
        k = 0
        while k < int(l1[i][2]):
            l = l1[i][3]
            d1[l][j].append(l1[i][0])
            j += 1
            if j > 4:
                j = 0
            k += 1
    print(d1)
    f.close()
    g.close()
            
lcreation()
    
            
