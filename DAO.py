#!python3
#DAO = Data Access Objects

from Model import *

class CategoryDAO:
    @classmethod
    def saveCategory(cls,catID, catName):
        with open('categories.txt','a') as fcat:
            fcat.writelines(catName + '\n')

    
    @classmethod
    def readCategory(cls):
        with open("categories.txt", 'r') as fcat:
            cls.categories = fcat.readlines()

        cls.categories = list(
            map(lambda x: x.replace('\n', ''), cls.categories))
        
        #put categories in a separate list
        cat = []
        for i in cls.categories:
            cat.append(i)
        
        return cat


class SalesDAO:
    @classmethod
    def saveSales(cls, sellProd: sellProduct):
        with open('soldprods.txt','a') as fsp:
            fsp.writelines(sellProd.soldProd.prodID + '|' +
                           sellProd.soldProd.prodName + '|' +
                           sellProd.soldProd.prodPrice + '|' +
                           sellProd.soldProd.prodCat + '|' +
                           sellProd.salesPerson + '|' +
                           sellProd.buyerPerson + '|' +
                           str(sellProd.qtySold) + '|' +
                           sellProd.dateSold + '\n')

    @classmethod
    def readSoldProd(cls):
        with open('soldprods.txt','r') as fsp:
            cls.soldprods = fsp.readlines()

        #replaces the \n by nothing
        cls.soldprods = list(
            map(lambda x: x.replace('\n', ''), cls.soldprods))

        #print(cls.soldprods)
        #split each sales inside a list
        cls.soldprods = list(
            map(lambda x: x.split('|'), cls.soldprods))
        #print(cls.soldprods)

        #put sales in a separate list
        sales = []
        for i in cls.soldprods:
            sales.append(sellProduct(
                Product(i[0], i[1], i[2], i[3]), i[4], i[5], i[6], i[7]))

        return sales

#pr = Product('1','Apple','5',"Fruits")
#sp = sellProduct(pr,'Jone','Eliane',3)

#sales = SalesDAO.readSoldProd()
#print(sales[0].soldProd.prodName)
#print(sales[1].soldProd.prodName)
#print(sales[0].buyerPerson)
#print(sales[1].buyerPerson)
