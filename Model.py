#!python3

from datetime import datetime

class Category:
    def __init__(self, catName):
        self.catName = catName


class Product:
    def __init__(self, prodID, prodName, prodPrice, prodCat):
        self.prodID = prodID
        self.prodName = prodName
        self.prodPrice = prodPrice
        self.prodCat = prodCat


class prodStock:
    def __init__(self, stoProd:Product, stoQty):
        self.stoProd = stoProd
        self.stoQty = stoQty


class sellProduct:
    def __init__(self,soldProd:Product, salesPerson, buyerPerson, qtySold, dateSold = datetime.now().strftime('%d/%m/%Y')):
        self.soldProd = soldProd
        self.salesPerson = salesPerson
        self.buyerPerson = buyerPerson
        self.qtySold = qtySold
        self.dateSold = dateSold


class Supplier:
    def __init__(self, suppEIN, suppName, suppTel, suppCat):
        self.suppEIN = suppEIN
        self.suppName = suppName
        self.suppTel = suppTel
        self.suppCat = suppCat


class Person:
    def __init__(self, perSSN, perName, perEmail, perPhone, perAddress):
        self.perSSN = perSSN
        self.perName = perName
        self.perEmail = perEmail
        self.perPhone = perPhone
        self.perAddress = perAddress


class Employee(Person):
    def __init__(self, empID, perName, perSSN, perEmail, perPhone, perAddress):
        self.empID = empID
        super(Employee, self).__init__(
            perName, perSSN, perEmail, perPhone, perAddress)

