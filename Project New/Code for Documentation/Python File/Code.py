import csv
from prettytable import PrettyTable
from decimal import *
import random
import pickle
import time
import datetime as dt
from cryptography.fernet import Fernet

#ASKS THE USER WHETHER THEY WANT TO LOGIN OR SIGNUP
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

#ALLOWS THE USER TO SIGNUP 
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

#ALLOWS THE USER TO LOGIN BASED ON PREVIOUSLY STORED USER DETAILS
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

#VIEW USER INFO
def viewinfo():
    print("Phone Number:",phoneno)
    print("Password:",password)

#VIEW PREVIOUS ORDERS BASED ON RESTAURANT CHOSEN
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

#TO GET DATA FOR EACH RESTAURANT FROM A CSV FILE
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

#TO GET THE LOCATION OF EACH RESTAURANT
def getrestloc():
    f = open("restloc.csv", newline='')
    r = csv.reader(f)
    data = list(r)
    restlocdata = {}
    for i in data:
        restlocdata[(i[0])] = i[-1]
    return restlocdata

#TO FIND THE AVERAGE PRICE OF EACH RESTAURANT BASED ON THEIR MENU
def averrestau(restdict):
    lowprice = ('a', 1000000000000000000000000000000000000000)
    averres = [] 
    for i in restdict:
        menu = restdict[i]
        price = []
        for items in menu:
            itemprice = float(items[-1])
            price.append(itemprice)
        sumprices = sum(price)
        average = round(Decimal(sumprices / len(price)),1)
        averres.append((i, average))
    return averres


#TO DISPLAY THE DETAILS OF EACH RESTAURANT
def dispavg(averrest, restdict, locdata):
    from math import ceil
    myTable = PrettyTable(["Number", "Restaurant Name", "Average Price", "Rating","Number of Ratings","Location"])
    print("Choose a restaurant using the numbers to order from:")
    locations = list(locdata.keys())
    restlist = [] 
    for i in range(len(averrest)):
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
        restnum = int(input("Enter which restaurant you would like to choose:"))  
        if (restnum > 0 and restnum <= len(restlist)) and type(restnum) == int:
            menu = restdict[restlist[restnum - 1]]  
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
    for i in menu: 
        myTable2.add_row([n, i[0],i[1],i[-1]])
        n += 1
    print(myTable2)
    return restlist[restnum - 1]

#TO CREATE THE CART OF THE USER
def addtocart(restdict):
    cart = {}
    i = 0
    while True:
        if i == 0:
            global restchoice
            restchoice = dispavg(averrest, restdict, getrestloc())  
            menu = restdict[restchoice]
            while True:
                foodchoice = int(
                    input("Enter Item Number of food item you would like to add: ")) 
                if foodchoice > 0 and foodchoice <= len(menu):
                    break
                else:
                    print("Enter Valid Food Item Number!")
            while True:
                quantity = int(input("Enter quantity you would like to order: "))
                if quantity > 0 and quantity < 50:
                    break
                elif quantity > 50:
                    print("The required quantity of food is not available")
                else:
                    print("Enter a Valid Amount!")
            i += 1
        else:
            foodchoice = int(
                input("Enter Item Number of food item you would like to add: ")) 
            quantity = int(input("Enter quantity you would like to order: ")) 
            menu = restdict[restchoice]
        for items in menu:
            if items[0] == restdict[restchoice][foodchoice - 1][0]:
                itemprice = int(items[-1])
                price = itemprice
        for i in restdict:
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
    return cart

#TO DISPLAY THE BILL BASED ON THE CART OF THE USER
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

def ratingscreate():
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

#TO CREATE A FILE WITH THE AVERAGE RATING OF EACH RESTAURANT
def ratingavgcreate():
    ratingavglist = []
    for i in restdict:
        ratelisele = [i, '']
        ratingavglist.append(ratelisele)
        rateavgfile = open("rateavg.csv", "w")
        w = csv.writer(rateavgfile)
    for i in ratingavglist:
        w.writerow(i)
    rateavgfile.close()

#TO CREATE A FILE WITH THE RATING OF EACH RESTAURANT
def rating():
    l1 = list(cart.values()) 
    restname = l1[0][0]
    print("Thank You for making a purchase from", restname)
    yorn = input("Would you like to add a rating for the following restaurant(Y/N)?")
    while True:
        if yorn.lower() == "y":
            rating = input("Enter your rating for the following restaurant(_/5):")
            if float(rating) >= 0 and float(rating) <= 5:
                print("Your Feedback has been recorded!")
                ratefile = open("rating.csv",
                                "r") 
                r = csv.reader(ratefile)
                ratings = list(r)
                ratefile.close()
                for i in ratings: 
                    if i != []:
                        if i[0] == restname:
                            oldratings = i[1]
                            i[1] = oldratings + rating + ';'
                ratefile = open("rating.csv", "w")
                w1 = csv.writer(ratefile)
                for i in ratings:
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

#TO UPDATE THE FILE BASED ON THE RATING PROVIDED BY THE USER
def ratingsavg():
    ratefile = open("rating.csv", "r")
    allrates = csv.reader(ratefile)
    allrates = list(allrates)
    ratefile.close() 
    rateavgfile = open("rateavg.csv",
                       "r") 
    r = csv.reader(rateavgfile)
    ratings = list(r)
    ratefile.close()
    rateavgfile = open("rateavg.csv", "w")
    w2 = csv.writer(rateavgfile)
    for i in allrates: 
        if i != []:
            try:
                values = i[1].split(';')
                for j in range(len(values)):
                    if values[j] != '':
                        values[j] = float(values[j]) 
                    elif values[j] == '':
                        values.remove('')
                rateavg = sum(values)/len(values)
                l1 = [i[0], rateavg, len(values)]
                w2.writerow(l1)
            except:
                w2.writerow([i[0], 0,0])

#TO DISPLAY A MENU TO ASK THE USER WHAT THEY WANT TO DO
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
        restdict = getdata()  
        global averrest
        averrest = averrestau(restdict)
        global cart
        cart = addtocart(restdict)  
        viewcart(cart)  
        ratefile = open("rating.csv", "r")
        ratelist = csv.reader(ratefile)
        ratelist = list(ratelist)
        if ratelist == []:  
            ratingscreate()
        rating()  
        ratingavgcreate()
        ratingsavg()
    elif choice == 3:
        print("Thank You, Have a nice day!")
        
entersite()
menu()




