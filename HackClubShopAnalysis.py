from colorama import Fore
import csv

items = []
mostEfficient = []

class Item:
    def __init__(self, name, shopPrice, actualPrice, available):
        self.name = name
        self.shopPrice = shopPrice
        self.actualPrice = actualPrice
        self.available = available

    def getName(self):
        return self.name
    
    def getShopPrice(self):
        return self.shopPrice

    def getActualPrice(self):
        return self.actualPrice
    
    def getAvailable(self):
        if self.available == "y":
            return True
        else:
            return False
    
    def getActualPriceOverShopPrice(self):
        if int(self.actualPrice) == 0:
            return 0
        else: 
            return round((int(self.actualPrice) / int(self.shopPrice)), 3)


with open('shop.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    next(csv_reader, None)
    
    for row in csv_reader:
        items.append(Item(row[0], row[1], row[2], row[3]))


for i in range(len(items)):
    mostEfficient.append([items[i].getName(), items[i].getActualPriceOverShopPrice()])
    #print((Fore.RED + items[i].getName()), Fore.WHITE + str(items[i].getActualPriceOverShopPrice()))


sortedMostEfficient = sorted(mostEfficient,key=lambda x: x[1])


for i in range(len(sortedMostEfficient)):
    print((Fore.RED + sortedMostEfficient[i][0]), Fore.WHITE + str(sortedMostEfficient[i][1]))