import csv

def userinput():#Todo Add an order view option(More efficient to do this maybe after implementation of GUI)
    cart = []#List containing items ordered
    while True:
        food = input("What would you like to order:")
        cart.append(food)
        yorn = input("Would you like to add another item to your cart?(Y/N):")#CLI version of adding items to cart
        if yorn.lower() == "n":
            break
    print(cart)
    f = open('Order.csv','w')#Text file containing all the products ordered(Created for future use when they want to view order)
    w = csv.writer(f)
    w.writerow(cart)
    return cart

def getdata():#Function to get the data of the restaurants from a csv file
    f = open('data.csv','r')
    r = csv.reader(f)
    data = list(r)
    d1 = {}
    for i in data:#A loop to remove the newline character of a csv file which is produced when we directly write to it(Empty list is recieved when we read)
        if i == []:
            data.remove(i)
    for i in data:#To create a dictionary----> {'Restaurant Name1':[[Food Name1,Price1],[Food Name2,Price2]],'Restaurant Name2':[[Food Name1,Price1],[Food Name2,Price2]]}
        if len(i) == 1:
            l1 = []
            restau = i[0]
            d1[restau] = l1
        elif len(i) != 1:
            l1.append(i)
    return d1


def finditem(userfood):#Function to create a list with the item requested by the user in all restaurants
    foodinrest = []#List to be created -> [[Restaurant Name1, Food required, Price],[Res Name2, Food required,Price]]
    for i in restdict:#Finding the item name in a particular restaurant from the dict(Values=Nested List) created in above fn using binary search
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
        prevres = lowestprice[0][-1]#Value stored in lowestprice before
        newres = i[-1]#New value in the list
        if int(prevres) > int(newres):#If the given number is lesser than the one before we equate this in that list
            lowestprice[0] = i
        elif int(prevres) == int(newres):
            lowestprice.append(i)
    if len(lowestprice) == 2:#A case where if two restaurants have the same food at the same price
        for i in range(len(lowestprice)):
            if i == 0:
                print(userfood,"is available at the best price at",lowestprice[0][0],",","Cost =",lowestprice[0][2])
            if i == 1:
                print(userfood, "is also available at the best price at",lowestprice[1][0],",","Cost =", lowestprice[1][2])
    else:
        print(userfood, "is available at the best price at", lowestprice[0][0],",","Cost =", lowestprice[0][2])

userfoods = userinput()
restdict = getdata()
#todo Have to compare total menu price for every restaurant not every food(Change that)
for userfood in userfoods:#A loop to get the lowest price for each and every product added to the cart
    userfoodinrests = finditem(userfood)
    lowestprice(userfoodinrests)

