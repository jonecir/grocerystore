#!python3
#DAO = Data Access Objects

from Model import *

class CategoryDAO:
    @classmethod
    def saveCategory(cls,cat:Category):
        try:
            with open('categories.txt','a') as fcat:
                fcat.writelines(cat.catName + '\n')
                fcat.close()

        except FileNotFoundError:
            with open('categories.txt', 'w') as fcat:
                fcat.writelines(cat.catName + '\n')
                fcat.close()
    
    @classmethod
    def readCategories(cls):
        try:
            cats = []
            with open("categories.txt", 'r') as fcat:
                cls.categories = fcat.readlines()

            cls.categories = list(
                map(lambda x: x.replace('\n', ''), cls.categories))
            
            #put categories in a separate list
            #cats = []
            for i in cls.categories:
                cats.append(i)
            
            fcat.close()
            return cats

        except FileNotFoundError:
            return cats


class ProductDAO:
    @classmethod
    def saveProduct(cls, prod:Product):
        try:
            fpr = open('products.txt', 'a')

        except FileNotFoundError:
            fpr = open('products.txt', 'w')

        fpr.writelines(prod.prodID + '|' +
                        prod.prodName + '|' +
                        prod.prodPrice + '|' +
                        prod.prodCat + '\n')
        fpr.close()


    @classmethod
    def readProducts(cls):
        try:
            prods = []
            with open('products.txt', 'r') as fpr:
                cls.products = fpr.readlines()

            #replaces the \n by nothing
            cls.products = list(
                map(lambda x: x.replace('\n', ''), cls.products))

            #split each sales product a list
            cls.products = list(
                map(lambda x: x.split('|'), cls.products))

            for i in cls.products:
                prods.append(Product(i[0], i[1], i[2], i[3]))

            fpr.close()
        except FileNotFoundError:
            return prods

        return prods


class StockDAO:
    @classmethod
    def saveStock(cls, prod: Product, stoQty):
        try:
            fsto = open('prodstocks.txt', 'a')

        except FileNotFoundError:
            fsto = open('prodstocks.txt', 'w')

        fsto.writelines(prod.prodID + '|' +
                        prod.prodName + '|' +
                        prod.prodPrice + '|' +
                        prod.prodCat + '|' +
                        str(stoQty) + '\n')
        fsto.close()


    @classmethod
    def readStock(cls):
        try:
            stocks = []
            with open('prodstocks.txt', 'r') as fsto:
                cls.prodstocks = fsto.readlines()

            #replaces the \n by nothing
            cls.prodstocks = list(
                map(lambda x: x.replace('\n', ''), cls.prodstocks))

            #split each sales inside a list
            cls.prodstocks = list(
                map(lambda x: x.split('|'), cls.prodstocks))

            for i in cls.prodstocks:
                stocks.append(prodStock(Product(i[0], i[1], i[2], i[3]), int(i[4])))

            fsto.close()
        except FileNotFoundError:
            return stocks
        
        return stocks



class SalesDAO:
    @classmethod
    def saveSales(cls, sellProd: sellProduct):
        try:
            fsp = open('soldprods.txt', 'a')

        except FileNotFoundError:
            fsp = open('soldprods.txt', 'w')

        fsp.writelines(sellProd.soldProd.prodID + '|' +
                       sellProd.soldProd.prodName + '|' +
                       sellProd.soldProd.prodPrice + '|' +
                       sellProd.soldProd.prodCat + '|' +
                       sellProd.salesPerson + '|' +
                       sellProd.buyerPerson + '|' +
                       str(sellProd.qtySold) + '\n')
        fsp.close()


    @classmethod
    def readSoldProd(cls):
        try:
            sales = []
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
            for i in cls.soldprods:
                sales.append(sellProduct(
                    Product(i[0], i[1], i[2], i[3]), i[4], i[5], i[6], i[7]))

            fsp.close()
        except FileNotFoundError:
            return sales

        return sales



class SupplierDAO:
    @classmethod
    def saveSupplier(cls, supp:Supplier):
        try:
            fsu = open('suppliers.txt', 'a')

        except FileNotFoundError:
            fsu = open('suppliers.txt', 'w')

        fsu.writelines(supp.suppEIN + '|' +
                        supp.suppName + '|' +
                        supp.suppTel + '|' +
                        supp.suppCat + '\n')
        fsu.close()


    @classmethod
    def readSuppliers(cls):
        try:
            supps = []
            with open('suppliers.txt', 'r') as fsu:
                cls.suppliers = fsu.readlines()

            #replaces the \n by nothing
            cls.suppliers = list(
                map(lambda x: x.replace('\n', ''), cls.suppliers))

            #split each sales inside a list
            cls.suppliers = list(
                map(lambda x: x.split('|'), cls.suppliers))

            for i in cls.suppliers:
                supps.append(Supplier(i[0], i[1], i[2], i[3]))

            fsu.close()
        except FileNotFoundError:
            return supps

        return supps



class PersonDAO:
    @classmethod
    def savePerson(cls, person: Person):
        try:
            fper = open('persons.txt', 'a')

        except FileNotFoundError:
            fper = open('persons.txt', 'w')

        fper.writelines(person.perSSN + '|' +
                        person.perName + '|' +
                        person.perEmail + '|' +
                        person.perPhone + '|' +
                        person.perAddress + '\n')
        fper.close()


    @classmethod
    def readPersons(cls):
        try:
            pers = []
            with open('persons.txt', 'r') as fper:
                cls.persons = fper.readlines()

            #replaces the \n by nothing
            cls.persons = list(
                map(lambda x: x.replace('\n', ''), cls.persons))

            #split each sales inside a list
            cls.persons = list(
                map(lambda x: x.split('|'), cls.persons))

            for i in cls.persons:
                pers.append(Person(i[0], i[1], i[2], i[3], i[4]))

            fper.close()
        except FileNotFoundError:
            return pers

        return pers



class EmployeeDAO:
    @classmethod
    def saveEmployee(cls, emp: Employee):
        try:
            femp = open('employees.txt', 'a')

        except FileNotFoundError:
            femp = open('employees.txt', 'w')

        femp.writelines(emp.empID + '|' + 
                        emp.perName + '|' +
                        emp.perSSN + '|' +
                        emp.perEmail + '|' +
                        emp.perPhone + '|' +
                        emp.perAddress + '\n')

        femp.close()


    @classmethod
    def readEmployees(cls):
        try:
            emps = []
            with open('employees.txt', 'r') as femp:
                cls.employees = femp.readlines()

            #replaces the \n by nothing
            cls.employees = list(
                map(lambda x: x.replace('\n', ''), cls.employees))

            #split each employee inside a list
            cls.employees = list(
                map(lambda x: x.split('|'), cls.employees))

            emps = []
            for i in cls.employees:
                emps.append(Employee(i[0], i[1], i[2], i[3], i[4], i[5]))
            femp.close()
        except FileNotFoundError:
            return emps

        return emps


#cat = Category('Veggies')
#CategoryDAO.saveCategory(cat)
#cats = CategoryDAO.readCategories()
#for i in cats:
#   print(i)
#pr1 = Product('1', 'Apple', '3', "Fruits")
#pr2 = Product('2', 'Orange', '2', "Fruits")
#pr3 = Product('3', 'Carrot', '5', "Veggies")
#pr4 = Product('4', 'Potato', '1', "Vegetables")
#ProductDAO.saveProduct(pr1)
#ProductDAO.saveProduct(pr2)
#ProductDAO.saveProduct(pr3)
#ProductDAO.saveProduct(pr4)
#pr = ProductDAO.readProducts()
#print(pr[0].prodID, pr[0].prodName, pr[0].prodPrice, pr[0].prodCat)

#StockDAO.saveStock(pr,100)
#st = StockDAO.readStock()
#print(st)
#for s in st:
#    print(s.stoProd.prodCat)
#print(st[0].stoProd.prodID + ',' +
#      st[0].stoProd.prodName + ',' +
#      st[0].stoProd.prodPrice + ',' +
#      st[0].stoProd.prodCat + ',' +
#      st[0].stoQty)

#pr = Product('1','Apple','5',"Fruits")
#sp = sellProduct(pr,'Jone','Eliane',3)

#sales = SalesDAO.readSoldProd()
#print(sales[0].soldProd.prodName)
#print(sales[1].soldProd.prodName)
#print(sales[0].buyerPerson)
#print(sales[1].buyerPerson)

#sup = Supplier('35-3337789', 'Krogger', '857-732-5355', 'Vegetables')
#SupplierDAO.saveSupplier(sup)
#su = SupplierDAO.readSuppliers()
#print(su[0].suppEIN, su[0].suppName, su[0].suppTel, su[0].suppCat)

#person = Person('383-21-2923', 'Jonecir', 'jonecir@gmail.com', '47-99148-0680', 'R. Jaboticabal, 32')
#PersonDAO.savePerson(person)
#per = PersonDAO.readPersons()
#print(per[0].perSSN, per[0].perName, per[0].perEmail,
      #per[0].perPhone, per[0].perAddress)

#empID, empName, empSSN, empEmail, empPhone, empAddress
#emp = Employee('2','Eliane', '383-22-2367', 'eliane@gmail.com', '47-99848-1630', 'R. Jaboticabal, 32')
#EmployeeDAO.saveEmployee(emp)
#emp = EmployeeDAO.readEmployees()
#print(emp[0].empID, emp[0].perName, emp[0].perSSN,
#      emp[0].perEmail, emp[0].perPhone, emp[0].perAddress)

