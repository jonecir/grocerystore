#!python3
#DAO = Data Access Objects

from Model import *

class CategoryDAO:
    @classmethod
    def saveCategory(cls,cat:Category):
        with open('categories.txt','a') as fcat:
            fcat.writelines(cat.catName + '\n')

    
    @classmethod
    def readCategories(cls):
        with open("categories.txt", 'r') as fcat:
            cls.categories = fcat.readlines()

        cls.categories = list(
            map(lambda x: x.replace('\n', ''), cls.categories))
        
        #put categories in a separate list
        cats = []
        for i in cls.categories:
            cats.append(i)
        
        return cats


class ProductDAO:
    @classmethod
    def saveProduct(cls, prod:Product):
        with open('products.txt', 'a') as fpr:
            fpr.writelines(prod.prodID + '|' +
                           prod.prodName + '|' +
                           prod.prodPrice + '|' +
                           prod.prodCat + '\n')

    @classmethod
    def readProducts(cls):
        with open('products.txt', 'r') as fpr:
            cls.products = fpr.readlines()

        #replaces the \n by nothing
        cls.products = list(
            map(lambda x: x.replace('\n', ''), cls.products))

        #split each sales product a list
        cls.products = list(
            map(lambda x: x.split('|'), cls.products))

        prods = []
        for i in cls.products:
            prods.append(Product(i[0], i[1], i[2], i[3]))

        return prods


class StockDAO:
    @classmethod
    def saveStock(cls, prod: Product, stoQty):
        with open('prodstocks.txt', 'a') as fsto:
            fsto.writelines(prod.prodID + '|' +
                            prod.prodName + '|' +
                            prod.prodPrice + '|' +
                            prod.prodCat + '|' +
                            str(stoQty) + '\n')

    @classmethod
    def readStock(cls):
        with open('prodstocks.txt', 'r') as fsto:
            cls.prodstocks = fsto.readlines()

        #replaces the \n by nothing
        cls.prodstocks = list(
            map(lambda x: x.replace('\n', ''), cls.prodstocks))

        #split each sales inside a list
        cls.prodstocks = list(
            map(lambda x: x.split('|'), cls.prodstocks))

        stock = []
        for i in cls.prodstocks:
            stock.append(prodStock(Product(i[0], i[1], i[2], i[3]), i[4]))

        return stock



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



class SupplierDAO:
    @classmethod
    def saveSupplier(cls, supp:Supplier):
        with open('suppliers.txt', 'a') as fsu:
            fsu.writelines(supp.suppName + '|' +
                           supp.suppEIN + '|' +
                           supp.suppPhone + '|' +
                           supp.suppCat + '\n')

    @classmethod
    def readSuppliers(cls):
        with open('suppliers.txt', 'r') as fsu:
            cls.suppliers = fsu.readlines()

        #replaces the \n by nothing
        cls.suppliers = list(
            map(lambda x: x.replace('\n', ''), cls.suppliers))

        #split each sales inside a list
        cls.suppliers = list(
            map(lambda x: x.split('|'), cls.suppliers))

        supps = []
        for i in cls.suppliers:
            supps.append(Supplier(i[0], i[1], i[2], i[3]))

        return supps



class PersonDAO:
    @classmethod
    def savePerson(cls, person: Person):
        with open('persons.txt', 'a') as fper:
            fper.writelines(person.perName + '|' +
                            person.perSSN + '|' +
                            person.perEmail + '|' +
                            person.perPhone + '|' +
                            person.perAddress + '\n')

    @classmethod
    def readPersons(cls):
        with open('persons.txt', 'r') as fper:
            cls.persons = fper.readlines()

        #replaces the \n by nothing
        cls.persons = list(
            map(lambda x: x.replace('\n', ''), cls.persons))

        #split each sales inside a list
        cls.persons = list(
            map(lambda x: x.split('|'), cls.persons))

        pers = []
        for i in cls.persons:
            pers.append(Person(i[0], i[1], i[2], i[3], i[4]))

        return pers



class EmployeeDAO:
    @classmethod
    def saveEmployee(cls, emp: Employee):
        with open('employees.txt', 'a') as femp:
            femp.writelines(emp.empID + '|' + 
                            emp.perName + '|' +
                            emp.perSSN + '|' +
                            emp.perEmail + '|' +
                            emp.perPhone + '|' +
                            emp.perAddress + '\n')

    @classmethod
    def readEmployees(cls):
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

        return emps


#cat = Category('Veggies')
#CategoryDAO.saveCategory(cat)
#cats = CategoryDAO.readCategories()
#for i in cats:
#   print(i)
#pr = Product('1', 'Apple', '5', "Fruits")
#pr = Product('2', 'Orange', '3', "Fruits")
#ProductDAO.saveProduct(pr)
#pr = ProductDAO.readProducts()
#print(pr[0].prodID, pr[0].prodName, pr[0].prodPrice, pr[0].prodCat)

#StockDAO.saveStock(pr,100)
#st = StockDAO.readStock()
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

#sup = Supplier('Wallmart', '12-3456789', '954-782-4554', 'Fruits')
#SupplierDAO.saveSupplier(sup)
#su = SupplierDAO.readSuppliers()
#print(su[0].suppName, su[0].suppEIN, su[0].suppPhone, su[0].suppCat)

#person = Person('Jonecir', '383-21-2923', 'jonecir@gmail.com', '47-99148-0680', 'R. Jaboticabal, 32')
#PersonDAO.savePerson(person)
#per = PersonDAO.readPersons()
#print(per[0].perName, per[0].perSSN, per[0].perEmail,
      #per[0].perPhone, per[0].perAddress)

#empID, empName, empSSN, empEmail, empPhone, empAddress
#emp = Employee('2','Eliane', '383-22-2367', 'eliane@gmail.com', '47-99848-1630', 'R. Jaboticabal, 32')
#EmployeeDAO.saveEmployee(emp)
#emp = EmployeeDAO.readEmployees()
#print(emp[0].empID, emp[0].perName, emp[0].perSSN,
#      emp[0].perEmail, emp[0].perPhone, emp[0].perAddress)

