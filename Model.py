#!python3

from datetime import datetime

class Category:
    def __init__(self, catID, catName):
        self.catID = catID
        self.catName = catName


class Product:
    def __init__(self, prodID, prodName, prodPrice, prodCat):
        self.prodID = prodID
        self.prodName = prodName
        self.prodQty = prodPrice
        self.prodCat = prodCat


class prodStock:
    def __init__(self, stoProd:Product, stoQty):
        self.stoProd = stoProd
        self.stoQty = stoQty


class sellProduct:
    def __init__(self,soldProd:Product, salesPerson, buyerPerson, qtySold, dateSold = datetime.now()):
        self.soldProd = soldProd
        self.salesPerson = salesPerson
        self.buyerPerson = buyerPerson
        self.qtySold = qtySold
        self.dateSold = dateSold


class Supplier:
    def __init__(self, suppName, suppEIN, suppPhone, suppCat):
        self.suppName = suppName
        self.suppEIN = suppEIN
        self.suppPhone = suppPhone
        self.suppCat = suppCat


class Person:
    def __init__(self,perName, perSSN, perEmail, perPhone, perAddress):
        self.perSSN = perName
        self.perSSN = perSSN
        self.perEmail = perEmail
        self.perPhone = perPhone
        self.perAddress = perAddress


class Employee(Person):
    def __init__(self, empID, empName, empSSN, empEmail, empPhone, empAddress):
        self.empID = empID
        super(Employee, self).__init__(empName, empSSN, empEmail, empPhone, empAddress)
