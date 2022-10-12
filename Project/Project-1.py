import csv
def info():
    f = open('data.csv','w+',newline = '')
    w = csv.writer(f)
    w.writerow(['Subject','Teacher','Number of periods'])
    while True:
        sub = input("Enter subject name:")
        teacher = input("Enter teacher name:")
        nump = int(input("Enter the number of periods:"))
        yorn = input("Do you want to add more records?(y/n):")
        w.writerow([sub,teacher,nump])
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
    l = [['Monday'],['Tuesday'],['Wednesday'],['Thursday'],['Friday']]
    j = 0
    for i in range(1,len(l1)):
        k = 0
        while k < int(l1[i][2]):
            l[j].append(l1[i][0])
            j += 1
            if j > 4:
                j = 0
            k += 1
    w.writerows(l)
    f.close()
    g.close()
            
lcreation()
    
    
            
