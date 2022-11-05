import csv
import ast
from prettytable import PrettyTable
from decimal import *
def getdata():#Function to get data from the csv file from
    # on to get the data of the restaurants from a csv file
    f = open('data.csv','r')
    r = csv.reader(f)
    data = list(r)
    d1 = {}
    global d2
    d2 = {}
    f.close()
    f = open("rateavg.csv","r")
    rateavg = csv.reader(f)
    rateavg = list(rateavg)
    for i in rateavg:
        if i != []:
            avgrate = Decimal(i[1])
            d2[i[0]] = round(avgrate,1)
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

def cheaprest(restdict):#function to find cheapest priced restaurant
    lowprice = ('a',1000000000000000000000000000000000000000)
    averres = []#List containing the prices of a particular restaurant
    for i in restdict:
        menu = restdict[i]
        price = []
        for items in menu:#Iteration to append price of a particular restaurant to the list
            itemprice = int(items[-1])
            price.append(itemprice)
        sumprices = sum(price)
        average = sumprices/len(price)
        averres.append((i,average))#Creates a tuple in averres = [(Restaurant Name, Average)]
    return averres

def dispavg(averrest,restdict,locdata):
    myTable = PrettyTable(["Number","Restaurant Name","Average Price","Rating","Location"])
    print("Choose a restaurant using the numbers to order from:")
    locations = list(locdata.keys())
    restlist = []#List containing restaurant names
    for i in range(len(averrest)):#Print every restaurant name and the restaurant's average price
            myTable.add_row([i+1,averrest[i][0],averrest[i][1],d2[averrest[i][0]],locdata[locations[i]]])
            restlist.append(averrest[i][0])
    print(myTable)
    usersort = input("Would you like to sort this table(Y/N):")
    if usersort.lower() == "y":
        typesort = int(input('''Sort by(Enter Number):
        1. Restaurant Name
        2. Average Price
        3. Rating
        4.Location'''''))
        if typesort == 1:
            print(myTable.get_string(sortby="Restaurant Name"))
        elif typesort == 2:
            print(myTable.get_string(sortby="Average Price"))
        elif typesort == 3:
            print(myTable.get_string(sortby="Rating"))
        elif typesort == 4:
            print(myTable.get_string(sortby="Location"))
    restnum = int(input("Enter which restaurant you would like to choose:"))#Asks the user to choose a restaurant
    menu = restdict[restlist[restnum-1]]#Get restaurant name from restlist and then get its menu from restdict
    myTable2 =  PrettyTable(["Number","Dishes","Price"])
    n=1
    for i in menu:#Prints the menu of the restaurant chosen by the user
        myTable2.add_row([n,i[0],i[1]])
        n+=1
    print(myTable2)
    return restlist[restnum-1]


def addtocart(restdict):#function to add items to cart
    cart = {}
    i = 0
    while True:
        if i ==0 :
            global restchoice
            restchoice = dispavg(averrest,restdict,getrestloc())#restaurant from which they would like item
            foodchoice = int(input("Enter Item Number of food item you would like to add: "))#indec of item they choose
            quantity = int(input("Enter quantity you would like to order: "))#quantity of item
            menu = restdict[restchoice]         #next 6 lines are for getting item price
            i += 1
        else:
            foodchoice = int( input("Enter Item Number of food item you would like to add: "))  # indec of item they choose
            quantity = int(input("Enter quantity you would like to order: "))  # quantity of item
            menu = restdict[restchoice]  # next 6 lines are for getting item price
        for items in menu:
            if items[0] == restdict[restchoice][foodchoice-1][0]:
                itemprice = int(items[-1])
                price = itemprice
        for i in restdict:#adding item to cart
            if i==restchoice:
                cart[restdict[i][foodchoice-1][0]]= (restchoice,price,quantity)
        yorn = input("Would you like to add another item(y/n)? ")
        if yorn.lower()=='n':
            break
    return cart#returning dictionary containing item name,restaurant ordered from,price and quantity


def viewcart(cart):
    from math import ceil
    bill = PrettyTable(["S.No", "Item","Quantity","Price"])
    total = 0
    serialno = 1
    for i in cart:
        bill.add_row([serialno, i, cart[i][-1], (cart[i][1]*cart[i][-1])])
        total+=((cart[i][1])*(cart[i][-1]))
        serialno+=1
    print(bill)
    print("Total = Rs.",total)
    print("GST = 18%")
    print("Grand Total = Rs.",ceil(total+total*0.18),)

def ratingscreate():#Creates a file called ratefile which contains empty ratings in the format [restname,[ratings]]
    ratingslist = []
    for i in restdict:
        ratelisele = [i, []]
        ratingslist.append(ratelisele)
        ratefile = open("rating.csv", "w")
        w = csv.writer(ratefile)
    for i in ratingslist:
        w.writerow(i)
    ratefile.close()

def ratingavgcreate():#To create a file which contains the average of price of every restaurant in the format [restname,ratingavg]
    ratingavglist = []
    for i in restdict:
        ratelisele = [i, []]
        ratingavglist.append(ratelisele)
        rateavgfile = open("rateavg.csv", "w")
        w = csv.writer(rateavgfile)
    for i in ratingavglist:
        w.writerow(i)
    rateavgfile.close()

def rating():#Accepts rating from the user and adds it to teh file
    l1 = list(cart.values())#List containing every instance of the restaurant name
    restname = l1[0][0]#Getting the restaurant name from the list
    print("Thank You for making a purchase from",restname)
    yorn = input("Would you like to add a rating for the following restaurant(Y/N)?")
    if yorn.lower() == "y":
        rating = float(input("Enter your rating for the following restaurant:"))
        print("Your Feedback has been recorded!")
        ratefile = open("rating.csv","r")#Opening file containing empty rates/old rates in the form [restname,[ratings]]
        r = csv.reader(ratefile)
        ratings = list(r)
        ratefile.close()
        for i in ratings:#1st Loop:To make every string in the format of list to list(cannot use str)
            if i != []:
                i[1] = ast.literal_eval(i[1])
        for i in ratings:#2nd Loop:To append the rating to the list of ratings present already(nothing or old ratings)
            if i != []:
                if i[0] == restname:
                    i[1].append(rating)
        ratefile = open("rating.csv", "w")
        w1 = csv.writer(ratefile)
        for i in ratings:#3rd Loop: To write the list with the new rating to the file
            if i != []:
                w1.writerow(i)
        ratefile.close()
    else:
        print("Have a good day!")

def ratingsavg():
    ratefile = open("rating.csv", "r")
    allrates = csv.reader(ratefile)
    allrates = list(allrates)
    ratefile.close()#Opened ratefile to get the individual ratings of the restaurants(NOTE:Not everage)
    rateavgfile = open("rateavg.csv", "r")#Opening rate avg file to get the blank avg format created by the fn ratingavgcreate()
    r = csv.reader(rateavgfile)
    ratings = list(r)
    ratefile.close()
    rateavgfile = open("rateavg.csv", "w")
    w2 = csv.writer(rateavgfile)
    for i in allrates:#To convert string in the form of list to list to calculate average
        if i != []:
                i[1] = ast.literal_eval(i[1])
    for i in ratings:#To convert string in the form of list to list to add value(Maybe not needed?)
        if i != []:
            i[1] = ast.literal_eval(i[1])
    for i in allrates:#Loop to write the values of the average rates to the file rateavg
        if i != []:
            try:#Try and except incase the sum is zero(ie:there are no ratings)
                rateavg = (sum(i[1])) / (len(i[1]))
                w2.writerow([i[0], rateavg])
            except:
                w2.writerow([i[0],0])

def getrestloc():
    f = open("restloc.csv",newline ='')
    r = csv.reader(f)
    data = list(r)
    restlocdata = {}
    for i in data:
        restlocdata[(i[0])]=i[-1]
    return restlocdata


restdict = getdata()#Function to get data from
averrest = cheaprest(restdict)#Returns the average price of each restaurant
cart = addtocart(restdict)#Gives the cart of the user
viewcart(cart)#Basically gives the bill of the user
ratefile = open("rating.csv", "r")
ratelist = csv.reader(ratefile)
ratelist = list(ratelist)
if ratelist == []:#To prevent it from clearing the rate file everytime the program is run so that the ratings get saved
    ratingscreate()
rating()#To add rating given by the user
ratingavgcreate()#To create a blank average rating of every rating provided in a file
ratingsavg()#Creates a file containing thethe average rating of every restaurant

#todo Create an algorithm for average order time






