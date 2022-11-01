import csv

def userinput():
    food = input("What would you like to order:")
    return food

def getdata():#Function to get the data of the restaurants from a csv file
    f = open('data.csv','r')
    r = csv.reader(f)
    data = list(r)
    d1 = {}
    for i in data:#A loop to remove the newline character of a csv file which is produced when we directly write to it(Empty list is recieved when we read)
        if i == []:
            data.remove(i)
    for i in data:#To create a dictionary----> {'Restaurant Name':[[Food Name1,Price1],[Food Name2,Price2]]}
        if len(i) == 1:
            l1 = []
            restau = i[0]
            d1[restau] = l1
        elif len(i) != 1:
            l1.append(i)
    return d1


def finditem(userfood):#Function to create a list with the item requested by the user in all restaurants
    foodinrest = []
    for i in restdict:
        l1 = restdict[i]
        l1.sort()
        L = 0
        U = len(l1)-1
        while L <= U:
            mid = (L+U)//2
            if userfood.lower() == l1[mid][0].lower():
                foodneeded = l1[mid]
                foodneeded.insert(0,i)
                foodinrest.append(foodneeded)
                break
            elif userfood > l1[mid][0]:
                L = mid+1
            elif userfood < l1[mid][0]:
                U = mid-1
    return foodinrest

def lowestprice(userfoodinrests):#Find the lowest price from the list created by the function finditem(userfood)
    lowestprice = [['','','1000000000000000000000000000000000000000000000000000000000000']]
    for i in userfoodinrests:
        prevres = lowestprice[0][-1]
        newres = i[-1]
        if int(prevres) > int(newres):
            lowestprice[0] = i
        elif int(prevres) == int(newres):
            lowestprice.append(i)
    if len(lowestprice) == 2:
        for i in range(len(lowestprice)):
            if i == 0:
                print(userfood,"is available at the best price at",lowestprice[0][0],",","Cost =",lowestprice[0][2])
            if i == 1:
                print(userfood, "is also available at the best price at",lowestprice[1][0],",","Cost =", lowestprice[1][2])
    else:
        print(userfood, "is available at the best price at", lowestprice[0][0],",","Cost =", lowestprice[0][2])

userfood = userinput()
restdict = getdata()
userfoodinrests = finditem(userfood)
lowestprice(userfoodinrests)

