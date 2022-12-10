def cheaprest(restdict):#function to find cheapest priced restaurant
    import statistics
    lowprice = ('a',1000000000000000000000000000000000000000)
    restnames = restdict.keys()
    for i in range(len(restdict)):#iterating over all restaurants
        itemprices = []#list containing prices of all items form a single rest
        for j in restdict:#loop to append prices of all items from menu
            price = j[1]
            itemprices.append(price)
        avg = statistics.mean(itemprices)
        restavg = (restnames[i],avg)
        if restavg[1]<=lowprice[1]:#checking if avg price lower or not
            lowprice=restavg
    print("The least expensive restaurant is: ",lowprice[0])
    return lowprice[0]
cheaprest(restdict)
#todo error comparing prices due to string datatype of prices of items
