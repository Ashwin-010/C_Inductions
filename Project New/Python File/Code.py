import csv
def userinput():
    food = input("What would you like to eat today:")

def getdata():#Function to get the data of the restaurants from a csv file
    f = open('data.csv','r')
    r = csv.reader(f)
    l = list(r)
    d1 = {}
    for i in l:#A loop to remove the newline character of a csv file which is produced when we directly write to it(Empty list is recieved when we read)
        if i == []:
            l.remove(i)
    for i in l:#To create a dictionary----> {'Restaurant Name':[[Food Name1,Price1],[Food Name2,Price2]]}
        if len(i) == 1:
            l1 = []
            restau = i[0]
            d1[restau] = l1
        elif len(i) != 1:
            l1.append(i)
    print(d1)

userinput()
getdata()
