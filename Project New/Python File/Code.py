import csv
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

def dispavg(averrest,restdict):#Todo Formatting of display(Look up lab fibonacci program(sir's solution))
    print("Restaurant Name\t\t\t\t\t","Average Price")#Print every restaurant name and the restaurant's average price
    for i in range(len(averrest)):
        print(averrest[i][0],"\t\t\t\t\t",averrest[i][1])
    restname = input("Enter which restaurant you would like to choose:")#Asks the user to choose a restaurant
    menu = restdict[restname]
    print("Dishes\t\t","Price")
    for i in menu:#Prints the menu of the restaurant chosen by the user
        print(i[0],"\t\t",i[1])

restdict = getdata()
averrest = cheaprest(restdict)
dispavg(averrest,restdict)
#Todo Accept User input add to cart and then provide total price and an option to view the order

def addtocart(restdict):#function to add items to cart
    cart = {}
    while True:
        restchoice = dispavg(averrest, restdict)#restaurant from which they would like item
        foodchoice = int(input("Enter Item Number of food item you would like to add: "))#indec of item they choose
        quantity = int(input("Enter quantity you would like to order: "))#quantity of item
        menu = restdict[restchoice]         #next 6 lines are for getting item price
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
    import math
    print("S.No\tItem\tRestaurant\tQuantity\tprice")
    total = 0
    serialno = 1
    for i in cart:
        print(serialno,".\t",i,"\t",cart[i][0],"\t",cart[i][-1],"\t",(cart[i][1])*2)
        total+=((cart[i][1])*2)
        serialno+=1
    print("Total = Rs.",total)
    print("GST = 18%")
    print("Grand Total = Rs.",math.ceil(total+total*0.18),)
viewcart(addtocart(restdict))

#todo allign tables
#todo add serial numbers for restaurant so that we dont have to type in full name everytime
