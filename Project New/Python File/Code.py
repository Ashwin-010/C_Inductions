import csv
import ast
from prettytable import PrettyTable
from decimal import *
import random
import pickle
import time
import datetime as dt
from cryptography.fernet import Fernet

def entersite():
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
key = Fernet(b'7FXASAwFtL74HPsAtwXMjTrmyAQM3-pUF_C6dpsGeF4=')

def signup():
    f = open('UserData.csv','a',newline = '')
    w = csv.writer(f)
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
                    print("Account with given phone number already exists!")
                    entersite()
                else:
                    break
                break
        else:
            print("Passwords do not match")
            continue
        break
    bytephonenum = bytes(phoneno,'utf-8')
    encrypphonenum = key.encrypt(bytephonenum)
    encrypphonenum = str(encrypphonenum,'utf-8')
    bytepassw = bytes(password,'utf-8')
    encryppassw = key.encrypt(bytepassw)
    encryppassw = str(encryppassw,'utf-8')
    w.writerow([encrypphonenum, encryppassw])
    f.close()
    print("Account has been created, Login to continue")
    login()

def login():
    f = open('UserData.csv', 'r')
    global phoneno
    global password
    phoneno = input("Enter Phone Number: ")
    password = input("Enter Password: ")
    r = csv.reader(f)
    all_u_data = list(r)
    loginorno = 0
    for i, j in all_u_data:
        i = i.lstrip("b'")
        i = i.rstrip("'")
        j = j.lstrip("b'")
        j = j.rstrip("'")
        if str(key.decrypt(bytes(i, 'utf-8')), 'utf-8') == phoneno and str(key.decrypt(bytes(j, 'utf-8')),
                                                                               'utf-8') == password:
             print("Signing In", end='')
             y = random.randint(2, 5)
             for i in range(y):
                 time.sleep(0.5)
                 print('.', end='')
                 print("Successfully logged In!")
                 f.close()
                 break
             loginorno = 1
    if loginorno == 0:
        time.sleep(1.5)
        print("Invalid Credentials!")
        entersite()

def viewinfo():
    print("Phone Number:",phoneno)
    print("Password:",password)

def viewords(phoneno,restchoice):
    yorn = input("Would you like to view your past orders from this restaurant?(Y/N)")
    if yorn.lower()=='y':
        phstr = str(phoneno)+'.dat'
        try:
            f=open(phstr,'rb')
            pastords = []
            while True:
                try:
                    data = pickle.load(f)
                    pastords.append(data)
                except:
                    break
            f.close()
            sno = 1
            checknum = 0
            for i in range(len(pastords)):
                if pastords[i][2] == restchoice:
                    print("Order Placed on", pastords[i][1], "from", pastords[i][2])
                    checknum = 1
                    order = PrettyTable(pastords[i][3][0])
                    for j in pastords[i][3]:
                        if type(j[0]) == int:
                            order.add_row(j)
                    print(order)
            if checknum == 0:
                print("You have not placed any orders from this restaurant!")
                time.sleep(2)
                return 0
            return 1
        except:
            print("You have not placed any orders from this restaurant!")
            time.sleep(2)
            return 0

def getdata():  # Function to get data from the csv file from
    f = open('data.csv', 'r')
    r = csv.reader(f)
    data = list(r)
    d1 = {}
    global ratingdict
    ratingdict = {}
    f.close()
    f = open("rateavg.csv", "r")
    rateavg = csv.reader(f)
    rateavg = list(rateavg)
    for i in rateavg:
        if i != []:
            if i[1] != '':
                roundavg = round(Decimal(i[1]), 1)
                ratingdict[i[0]] = [roundavg, i[-1]]
            elif i[1] == '':
                roundavg = 0
                ratingdict[i[0]] = [roundavg, i[-1]]
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
    for i in d1:
        if i not in ratingdict:
            ratingdict[i] = [0, '0']
    return d1

def getrestloc():
    f = open("restloc.csv", newline='')
    r = csv.reader(f)
    data = list(r)
    restlocdata = {}
    for i in data:
        restlocdata[(i[0])] = i[-1]
    return restlocdata


def averrestau(restdict):  # function to find cheapest priced restaurant
    lowprice = ('a', 1000000000000000000000000000000000000000)
    averres = []  # List containing the prices of a particular restaurant
    for i in restdict:
        menu = restdict[i]
        price = []
        for items in menu:# Iteration to append price of a particular restaurant to the list
            itemprice = float(items[-1])
            price.append(itemprice)
        sumprices = sum(price)
        average = round(Decimal(sumprices / len(price)),1)
        averres.append((i, average))  # Creates a tuple in averres = [(Restaurant Name, Average)]
    return averres

def menu():
    userchoice = int(input('''What would you like to do today?
        1. Check user info
        2. Order food
        3.Exit:'''))
    if userchoice == 1:
        viewinfo()
        menu()
    elif userchoice == 2:
        global restdict
        restdict = getdata()  # Function to get data from CSV File
        global averrest
        averrest = averrestau(restdict)  # Returns the average price of each restaurant
        global cart
        cart = addtocart(restdict)  # Gives the cart of the user
        viewcart(cart)  # Basically gives the bill of the user
        ratefile = open("rating.csv", "r")
        ratelist = csv.reader(ratefile)
        ratelist = list(ratelist)
        if ratelist == []:  # To prevent it from clearing the rate file everytime the program is run so that the ratings get saved
            ratingscreate()
        rating()  # To add rating given by the user
        ratingavgcreate()  # To create a blank average rating of every rating provided in a file
        ratingsavg()
    elif choice == 3:
        print("Thank You, Have a nice day!")

def dispavg(averrest, restdict, locdata):
    from math import ceil
    myTable = PrettyTable(["Number", "Restaurant Name", "Average Price", "Rating","Number of Ratings","Location"])
    print("Choose a restaurant using the numbers to order from:")
    locations = list(locdata.keys())
    restlist = []  # List containing restaurant names
    for i in range(len(averrest)):# Print every restaurant name and the restaurant's average price
        if ratingdict[averrest[i][0]][-1] == '':
            myTable.add_row(
                [i + 1, averrest[i][0], averrest[i][1], ratingdict[averrest[i][0]][0], 0, locdata[locations[i]]])
            restlist.append(averrest[i][0])
        else:
            myTable.add_row([i + 1, averrest[i][0], averrest[i][1], ratingdict[averrest[i][0]][0], ratingdict[averrest[i][0]][-1], locdata[locations[i]]])
            restlist.append(averrest[i][0])
    print(myTable)
    usersort = input("Would you like to sort this table(Y/N):")
    if usersort.lower() == "y":
        typesort = int(input('''Sort by(Enter Number):
        1. Restaurant Name
        2. Average Price
        3.Rating
        4.Location:'''))
        if typesort == 1:
            print(myTable.get_string(sortby="Restaurant Name"))
        elif typesort == 2:
            print(myTable.get_string(sortby="Average Price"))
        elif typesort == 3:
            print(myTable.get_string(sortby="Rating",reversesort = True))
        elif typesort == 4:
            print(myTable.get_string(sortby="Location"))
    while True:
        restnum = int(input("Enter which restaurant you would like to choose:"))  # Asks the user to choose a restaurant
        if (restnum > 0 and restnum <= len(restlist)) and type(restnum) == int:
            menu = restdict[restlist[restnum - 1]]  # Get restaurant name from restlist and then get its menu from restdict
            break
        else:
            print("Enter Valid Restaurant Number!")
            continue
    restchoice = restlist[restnum - 1]
    if viewords(phoneno,restchoice):
        print("Continuing in 10 seconds!")
        time.sleep(10)
    myTable2 = PrettyTable(["Number", "Dishes","Veg/Non Veg", "Price"])
    n = 1
    for i in menu:  # Prints the menu of the restaurant chosen by the user
        myTable2.add_row([n, i[0],i[1],i[-1]])
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
                if quantity > 0 and quantity < 50:
                    break
                elif quantity > 50:
                    print("The required quantity of food is not available")
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
    order = [["S.No", "Item", "Quantity", "Price"]]
    bill = PrettyTable(["S.No", "Item", "Quantity", "Price"])
    total = 0
    serialno = 1
    for i in cart:
        bill.add_row([serialno, i, cart[i][-1], (cart[i][1] * cart[i][-1])])
        order.append([serialno, i, cart[i][-1], (cart[i][1] * cart[i][-1])])
        total += ((cart[i][1]) * (cart[i][-1]))
        serialno += 1
    print(bill)
    print("Total = Rs.", total)
    print("GST = 18%")
    print("Grand Total = Rs.", ceil(total + total * 0.18), )
    phstr = str(phoneno) +'.dat'
    time = dt.datetime.now()
    f = open(phstr,'ab')
    pickle.dump([phoneno,time,restchoice,order],f)
    f.close()

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
    with open("rating.csv") as f:
        r = csv.reader(f)
        l = list(r)
        no_ratings = []
        for i in l:
            no_ratings.append(i[-1])
    return no_ratings


def ratingavgcreate():  # To create a file which contains the average of price of every restaurant in the format [restname,ratingavg]
    ratingavglist = []
    for i in restdict:
        ratelisele = [i, '']
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
            rating = input("Enter your rating for the following restaurant(_/5):")
            if float(rating) >= 0 and float(rating) <= 5:
                print("Your Feedback has been recorded!")
                ratefile = open("rating.csv",
                                "r")  # Opening file containing empty rates/old rates in the form [restname,[ratings]]
                r = csv.reader(ratefile)
                ratings = list(r)
                ratefile.close()
                for i in ratings:  # 2nd Loop:To append the rating to the list of ratings present already(nothing or old ratings)
                    if i != []:
                        if i[0] == restname:
                            oldratings = i[1]
                            i[1] = oldratings + rating + ';'
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
    for i in allrates:  # Loop to write the values of the average rates to the file rateavg
        if i != []:# Try and except incase the sum is zero(ie:there are no ratings)
            try:
                values = i[1].split(';')
                for j in range(len(values)):
                    if values[j] != '':
                        values[j] = float(values[j])  # To convert the values from string to integer
                    elif values[j] == '':
                        values.remove('')
                rateavg = sum(values)/len(values)
                l1 = [i[0], rateavg, len(values)]
                w2.writerow(l1)
            except:
                w2.writerow([i[0], 0,0])

entersite()
menu()
  # Creates a file containing thethe average rating of every restaurant'''



