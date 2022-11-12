import csv
import ast
from prettytable import PrettyTable
from decimal import *


def getdata():  # Function to get data from the csv file from
    # on to get the data of the restaurants from a csv file
    f = open('data.csv', 'r')
    r = csv.reader(f)
    data = list(r)
    d1 = {}
    global d2
    d2 = {}
    f.close()
    f = open("rateavg.csv", "r")
    rateavg = csv.reader(f)
    rateavg = list(rateavg)
    for i in rateavg:
        if i != []:
            avgrate = Decimal(i[1])
            roundavg = round(avgrate, 1)
            d2[i[0]] = [roundavg, i[-1]]
    for i in data:  # A loop to remove the newline character of a csv file which is produced when we directly write to it(Empty list is recieved when we read)
        if i == []:
            data.remove(i)
    for i in data:  # To create a dictionary----> {'Restaurant Name1':[[Food Name1,Price1],[Food Name2,Price2]],'Restaurant Name2':[[Food Name1,Price1],[Food Name2,Price2]]}
        if len(i) == 1:
            l1 = []
            restau = i[0]
            d1[restau] = l1
        elif len(i) != 1:
            l1.append(i)
    return d1


def cheaprest(restdict):  # function to find cheapest priced restaurant
    lowprice = ('a', 1000000000000000000000000000000000000000)
    averres = []  # List containing the prices of a particular restaurant
    for i in restdict:
        menu = restdict[i]
        price = []
        for items in menu:  # Iteration to append price of a particular restaurant to the list
            itemprice = int(items[-1])
            price.append(itemprice)
        sumprices = sum(price)
        average = sumprices / len(price)
        averres.append((i, average))  # Creates a tuple in averres = [(Restaurant Name, Average)]
    return averres


def dispavg(averrest, restdict, locdata):
    from math import ceil
    myTable = PrettyTable(["Number", "Restaurant Name", "Average Price", "Rating","Number of Ratings","Location"])
    print("Choose a restaurant using the numbers to order from:")
    locations = list(locdata.keys())
    restlist = []  # List containing restaurant names
    for i in range(len(averrest)):  # Print every restaurant name and the restaurant's average price
        myTable.add_row([i + 1, averrest[i][0], averrest[i][1], d2[averrest[i][0]][0],d2[averrest[i][0]][-1],locdata[locations[i]]])
        restlist.append(averrest[i][0])
    print(myTable)
    usersort = input("Would you like to sort this table(Y/N):")
    if usersort.lower() == "y":
        typesort = int(input('''Sort by(Enter Number):
        1. Restaurant Name
        2. Average Price
        3. Rating
        4.Location:'''''))
        if typesort == 1:
            print(myTable.get_string(sortby="Restaurant Name"))
        elif typesort == 2:
            print(myTable.get_string(sortby="Average Price"))
        elif typesort == 3:
            print(myTable.get_string(sortby="Rating"))
        elif typesort == 4:
            print(myTable.get_string(sortby="Location"))
    while True:
        try:
            restnum = int(
                input("Enter which restaurant you would like to choose:"))  # Asks the user to choose a restaurant
        except:
            print("Enter Valid Restaurant Number!")
            continue
        if (restnum > 0 and restnum < len(restlist)) and type(restnum) == int:
            menu = restdict[
                restlist[restnum - 1]]  # Get restaurant name from restlist and then get its menu from restdict
            break
        else:
            print("Enter Valid Restaurant Number!")
    myTable2 = PrettyTable(["Number", "Dishes", "Price"])
    n = 1
    for i in menu:  # Prints the menu of the restaurant chosen by the user
        myTable2.add_row([n, i[0], i[1]])
        n += 1
    print(myTable2)
    return restlist[restnum - 1]


def addtocart(restdict):  # function to add items to cart
    cart = {}
    i = 0
    while True:
        if i == 0:
            global restchoice
            restchoice = dispavg(averrest, restdict, getrestloc())  # restaurant from which they would like item
            menu = restdict[restchoice]
            while True:
                foodchoice = int(
                    input("Enter Item Number of food item you would like to add: "))  # indec of item they choose
                if foodchoice > 0 and foodchoice <= len(menu):
                    break
                else:
                    print("Enter Valid Food Item Number!")
            while True:
                quantity = int(input("Enter quantity you would like to order: "))  # quantity of item
                if quantity > 0:
                    break
                else:
                    print("Enter a Valid Amount!")
            i += 1
        else:
            foodchoice = int(
                input("Enter Item Number of food item you would like to add: "))  # index of item they choose
            quantity = int(input("Enter quantity you would like to order: "))  # quantity of item
            menu = restdict[restchoice]  # next 6 lines are for getting item price
        for items in menu:
            if items[0] == restdict[restchoice][foodchoice - 1][0]:
                itemprice = int(items[-1])
                price = itemprice
        for i in restdict:  # adding item to cart
            for j in range(len(restdict[restchoice])):
                if i == restchoice and restdict[restchoice][foodchoice-1][0] not in list(cart.keys()):
                    cart[restdict[i][foodchoice - 1][0]] = (restchoice, price, quantity)
                    break
                elif i == restchoice and restdict[restchoice][j][0] in list(cart.keys()):
                    quan = cart[restdict[restchoice][foodchoice - 1][0]][-1] + quantity
                    cart[restdict[restchoice][foodchoice - 1][0]] = (restchoice, price, quan)
                    break
        yorn = input("Would you like to add another item(y/n)? ")
        if yorn.lower() == 'n':
            break
    return cart  # returning dictionary containing item name,restaurant ordered from,price and quantity


def viewcart(cart):
    from math import ceil
    bill = PrettyTable(["S.No", "Item", "Quantity", "Price"])
    total = 0
    serialno = 1
    for i in cart:
        bill.add_row([serialno, i, cart[i][-1], (cart[i][1] * cart[i][-1])])
        total += ((cart[i][1]) * (cart[i][-1]))
        serialno += 1
    print(bill)
    print("Total = Rs.", total)
    print("GST = 18%")
    print("Grand Total = Rs.", ceil(total + total * 0.18), )


def ratingscreate():  # Creates a file called ratefile which contains empty ratings in the format [restname,[ratings]]
    ratingslist = []
    for i in restdict:
        ratelisele = [i, []]
        ratingslist.append(ratelisele)
        ratefile = open("rating.csv", "w")
        w = csv.writer(ratefile)
    for i in ratingslist:
        w.writerow(i)
    ratefile.close()


def ratingno():
    with open("rating.csv") as f:
        r = csv.reader(f)
        l = list(r)
        print(l)
        no_ratings = []
        for i in l:
            no_ratings.append(i[-1])
    return no_ratings


def ratingavgcreate():  # To create a file which contains the average of price of every restaurant in the format [restname,ratingavg]
    ratingavglist = []
    for i in restdict:
        ratelisele = [i, []]
        ratingavglist.append(ratelisele)
        rateavgfile = open("rateavg.csv", "w")
        w = csv.writer(rateavgfile)
    for i in ratingavglist:
        w.writerow(i)
    rateavgfile.close()


def rating():  # Accepts rating from the user and adds it to teh file
    l1 = list(cart.values())  # List containing every instance of the restaurant name
    restname = l1[0][0]  # Getting the restaurant name from the list
    print("Thank You for making a purchase from", restname)
    yorn = input("Would you like to add a rating for the following restaurant(Y/N)?")
    while True:
        if yorn.lower() == "y":
            rating = float(input("Enter your rating for the following restaurant(_/5):"))
            if rating >= 0 and rating <= 5:
                print("Your Feedback has been recorded!")
                ratefile = open("rating.csv",
                                "r")  # Opening file containing empty rates/old rates in the form [restname,[ratings]]
                r = csv.reader(ratefile)
                ratings = list(r)
                ratefile.close()
                for i in ratings:  # 1st Loop:To make every string in the format of list to list(cannot use str)
                    if i != []:
                        i[1] = ast.literal_eval(i[1])
                for i in ratings:  # 2nd Loop:To append the rating to the list of ratings present already(nothing or old ratings)
                    if i != []:
                        if i[0] == restname:
                            i[1].append(rating)
                ratefile = open("rating.csv", "w")
                w1 = csv.writer(ratefile)
                for i in ratings:  # 3rd Loop: To write the list with the new rating to the file
                    if i != []:
                        w1.writerow(i)
                ratefile.close()
                break
            else:
                print("Please Enter Valid Rating!")
                continue
        else:
            print("Enjoy your food!")
            break


def ratingsavg():
    ratefile = open("rating.csv", "r")
    allrates = csv.reader(ratefile)
    allrates = list(allrates)
    ratefile.close()  # Opened ratefile to get the individual ratings of the restaurants(NOTE:Not everage)
    rateavgfile = open("rateavg.csv",
                       "r")  # Opening rate avg file to get the blank avg format created by the fn ratingavgcreate()
    r = csv.reader(rateavgfile)
    ratings = list(r)
    ratefile.close()
    rateavgfile = open("rateavg.csv", "w")
    w2 = csv.writer(rateavgfile)
    for i in allrates:  # To convert string in the form of list to list to calculate average
        if i != []:
            i[1] = ast.literal_eval(i[1])
    for i in ratings:  # To convert string in the form of list to list to add value(Maybe not needed?)
        if i != []:
            i[1] = ast.literal_eval(i[1])
    for i in allrates:  # Loop to write the values of the average rates to the file rateavg
        if i != []:
            try:  # Try and except incase the sum is zero(ie:there are no ratings)
                rateavg = (sum(i[1])) / (len(i[1]))
                w2.writerow([i[0], rateavg, len(i[1])])
            except:
                w2.writerow([i[0], 0])


def getrestloc():
    f = open("restloc.csv", newline='')
    r = csv.reader(f)
    data = list(r)
    restlocdata = {}
    for i in data:
        restlocdata[(i[0])] = i[-1]
    return restlocdata


def entersite():
    import pickle
    print('''Welcome to Fast Eats!
    1.Sign up
    2.Login
    3.Exit''')
    choice = int(input("What would you like to do: "))
    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        quit()


def signup():
    import pickle
    f = open('UserData.dat','ab')
    while True:
        phoneno = input("Enter Phone number: ")
        if len(phoneno)==10:
            break
        else:
            print("Enter Valid Phone Number!")
            continue
    while True:
        password = input("Enter password(Include an uppercase,lowercase,number and special character): ")
        conditions = [0, 0, 0, 0]
        for i in password:
            if i.isupper():
                conditions[0] = 1
            elif 33<=ord(i)<=47:
                conditions[3] = 1
            elif 58<=ord(i)<=64:
                conditions[3] = 1
            elif i.islower():
                conditions[1] = 1
            elif i in '0123456789':
                conditions[2] = 1
        for i in range(len(conditions)):
            if conditions[i] != 1 and i == 0:
                print("Please include an uppercase character!")
                i = 1
                break
            elif conditions[i] != 1 and i == 1:
                print("Please include a lowercase character!")
                i = 1
                break
            elif conditions[i] != 1 and i == 2:
                print("Please include a number!")
                i = 1
                break
            elif conditions[i] != 1 and i == 3:
                print("Please include a special character!")
                i = 1
                break
        if i == 1:
            continue
        else:
            break
    while True:
        repass = input("Please Re-Enter your password: ")
        if repass == password:
            all_u_data = []
            while True:
                try:
                    chck_data = pickle.load(f)
                    all_u_data.append(chck_data)
                except:
                    break
            for i in all_u_data:
                if all_u_data[i][0] == phoneno:
                    print("Account with given phone number aldready exists!")
                    entersite()
                else:
                    break
                break
        else:
            print("Passwords do not match")
            continue
        break
    pickle.dump([phoneno, password],f)
    f.close()
    print("Account has been created, Login to continue")
    login()

def login():
    import random
    import pickle
    f = open('UserData.dat','rb')
    phoneno = input("Enter Phone Number: ")
    password = input("Enter Password: ")
    u_data = [phoneno,password]
    all_u_data = []

    while True:
        try:
            chck_data = pickle.load(f)
            all_u_data.append(chck_data)
        except:
            break
    for i in all_u_data:
        if i == u_data:
            print("Signing In", end='')
            y = random.randint(1, 10)
            for i in range(y):
                print('.', end='')
            print("Succesfully logged In!")
            f.close()
            break
    else:
        print("Invalid Credentials!")
        entersite()


#entersite()
restdict = getdata()  # Function to get data from
averrest = cheaprest(restdict)  # Returns the average price of each restaurant
cart = addtocart(restdict)  # Gives the cart of the user
viewcart(cart)  # Basically gives the bill of the user
ratefile = open("rating.csv", "r")
ratelist = csv.reader(ratefile)
ratelist = list(ratelist)
if ratelist == []:  # To prevent it from clearing the rate file everytime the program is run so that the ratings get saved
    ratingscreate()
rating()  # To add rating given by the user
ratingavgcreate()  # To create a blank average rating of every rating provided in a file
ratingsavg()  # Creates a file containing thethe average rating of every restaurant

# todo Create an algorithm for average order time
