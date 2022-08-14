
#!python3

import datetime
from DAO import *

class CategoryController:
    def newCategory(self, newCat):
        catExists = False
        cats = CategoryDAO.readCategories()
        for cat in cats:
            if cat == newCat:
                catExists = True
        
        if not catExists:
            CategoryDAO.saveCategory(Category(newCat))
            print('New category added successfully!')
        else:
            print('Category already exists! Please double check it.')


    def delCategory(self, delCat):
        cats = CategoryDAO.readCategories()

        #esse filter, na verdade não precisa
        #cat = list(filter(lambda cats: cats == delCat, cats))
        #print(cat)
#        if len(cat) <= 0:
#            print('This category does not exist! Please verify.')
#        else:

        catFound = False
        for i in range(len(cats)):
            if cats[i] == delCat:
                catFound = True
                del cats[i]
                break

        if catFound:
            with open('categories.txt', 'w') as fcat:
                for cat in cats:
                    fcat.writelines(cat+'\n')

            print('Category was deleted!')
            #TODO: Colocar 'sem categoria' no estoque
            #mas acho que o correto era não deixar excluir eqto
            #existir produtos nessa categoria (pensar!)
            stocks = StockDAO.readStock()
            lsto = list(map(lambda x: prodStock(Product(
                x.stoProd.prodID,
                x.stoProd.prodName,
                x.stoProd.prodPrice,
                'No category'), x.stoQty)
                if (x.stoProd.prodCat == delCat) else (x), stocks))

            fsto = open('prodstocks.txt', 'w')
            fsto.close
            for s in lsto:
                pr = Product(s.stoProd.prodID,
                             s.stoProd.prodName,
                             s.stoProd.prodPrice,
                             s.stoProd.prodCat)
                
                StockDAO.saveStock(pr, s.stoQty)
            print('Product category has been updated in stock file')
        else:
            print('Category does not exist! Please verify.')


    def updateCategory(self, fromCat, toCat):
        cats = CategoryDAO.readCategories()
        catFound = list(filter(lambda cats: cats == fromCat, cats))
        if catFound:
            #catExists = list(filter(lambda cats: cats == fromCat, cats))
            #print(catFound[0])
            #print('Good, you may update this category')
            if catFound[0] == toCat:
                print('Sorry, please provide a different category!')
            else:
                #print(cats)
                ucats = list(map(lambda cats: toCat if (cats == fromCat) else (cats) ,cats))
                #print(ucats)
                with open('categories.txt','w') as fcat:
                    for cat in ucats:
                        fcat.writelines(cat + '\n')
                print('Category has been updated!')
                
                #TODO: Alterar também a categoria do estoque
                stocks = StockDAO.readStock()
                lsto = list(map(lambda x: prodStock(Product(
                    x.stoProd.prodID,
                    x.stoProd.prodName,
                    x.stoProd.prodPrice,
                    toCat), x.stoQty)
                    if (x.stoProd.prodCat == fromCat) else (x), stocks))

                fsto = open('prodstocks.txt', 'w')
                fsto.close
                for s in lsto:
                    pr = Product(s.stoProd.prodID,
                                 s.stoProd.prodName,
                                 s.stoProd.prodPrice,
                                 s.stoProd.prodCat)

                    StockDAO.saveStock(pr, s.stoQty)
                print('Product category has been updated in stock file')
        else:
            print('Sorry, category not found!')


    def listCategories(self):
        cats = CategoryDAO.readCategories()
        if len(cats) == 0:
            print('No categories to list!')
        else:
            for cat in cats:
                print(cat)



class StockController:
    def newStockProduct(self, prodID, prodName, prodPrice, prodCat, stoQty):
        stocks = StockDAO.readStock()
        cats   = CategoryDAO.readCategories()
        #print(cats)
        #print('\n')
        cat = list(
            filter(lambda catName: catName == prodCat, cats))
        #print(cat)
        sto = list(
            filter(lambda prod: prod.stoProd.prodName == prodName, stocks))
        #print(sto)
        if len(cat) > 0:
            if len(sto) == 0:
                product = Product(prodID, prodName, prodPrice, prodCat)
                StockDAO.saveStock(product, stoQty)
                print('Product saved successfully!')
            else:
                print('Product already exists!')
        else:
            print('The informed category does not exist!')


    def delStockProduct(self, prodName):
        stocks = StockDAO.readStock()
        #sto = list(filter(lambda prod: prod.stoProd.prodName == prodName, stocks))
        #if len(sto) > 0:
        prodFound = False
        for s in range(len(stocks)):
            if stocks[s].stoProd.prodName == prodName:
                prodFound =  True
                del stocks[s]
                break
        #else:
        #    print('Product to be removed does not exist!')
        if prodFound:
            fsto = open('prodstocks.txt','w')
            fsto.close
            for s in stocks:
                pr = Product(s.stoProd.prodID, s.stoProd.prodName,
                             s.stoProd.prodPrice, s.stoProd.prodCat)
                StockDAO.saveStock(pr, s.stoQty)
            print('Product has been deleted!')
        else:
            print('Product to be removed does not exist!')


    def updateStockProduct(self, prodName, newProdPrice = 0, newProdQty = -1):
        stocks = StockDAO.readStock()
        sto = list(filter(lambda prod: prod.stoProd.prodName == prodName, stocks))
        if len(sto) > 0:
            sto = list(map(lambda x: prodStock(Product(
                x.stoProd.prodID,
                x.stoProd.prodName,
                newProdPrice,
                x.stoProd.prodCat),
                newProdQty)
                if (x.stoProd.prodName == prodName)
                else (x), stocks)
            )

            fsto = open('prodstocks.txt', 'w')
            fsto.close
            for s in sto: 
                pr = Product(s.stoProd.prodID, s.stoProd.prodName,
                            s.stoProd.prodPrice, s.stoProd.prodCat)
                StockDAO.saveStock(pr, s.stoQty)

            print('Product stock has been updated!')
        else:
            print('Product is not in stock!')

    def listStockProducts(self):
        stocks = StockDAO.readStock()
        if len(stocks) == 0:
            print('No products in stock!')
        else:
            qty = 1
            for s in stocks:
                print(f"================= Product {qty} =================")
                print(f"Product ID: {s.stoProd.prodID}"),
                print(f"Product name: {s.stoProd.prodName}"),
                print(f"Product price: {s.stoProd.prodPrice}"),
                print(f"Product cat.: {s.stoProd.prodCat}"),
                print(f"Product qty.: {s.stoQty}\n")
                qty += 1


class SalesController:
    def addNewSales(self, prodName, sellerName, buyerName, qtySold):
        stocks = StockDAO.readStock()
        temp = []
        foundProd = False
        qtyFound  = False
        for s in stocks:
            if s.stoProd.prodName == prodName:
                foundProd = True
                if s.stoQty >= qtySold:
                    qtyFound = True
                    s.stoQty = int(s.stoQty) - int(qtySold)
                    soldProd = sellProduct(Product(
                                                s.stoProd.prodID,
                                                s.stoProd.prodName,
                                                s.stoProd.prodPrice,
                                                s.stoProd.prodCat),
                                                sellerName,
                                                buyerName,
                                                qtySold
                                            )
                    SalesDAO.saveSales(soldProd)
                    valueSold = int(qtySold) * int(s.stoProd.prodPrice)

            temp.append(prodStock(Product(s.stoProd.prodID,
                                s.stoProd.prodName,
                                s.stoProd.prodPrice,
                                s.stoProd.prodCat),
                                s.stoQty
                        ))

        fsto = open('prodstocks.txt','w')
        fsto.close()
        
        for x in temp:
            pr = Product(x.stoProd.prodID,
                         x.stoProd.prodName,
                         x.stoProd.prodPrice,
                         x.stoProd.prodCat)
            StockDAO.saveStock(pr,x.stoQty)
        
        if not foundProd:
            print('Product not found!')
            return 1
        elif not qtyFound:
            print('Qty sold is greater than the qty available stock!')
            return 2

        print (f'Amount sold: {valueSold}')
        return valueSold


    def salesReport(self):
        allSales = SalesDAO.readSoldProd()
        prodSales = []
        for s in allSales:
            pname = s.soldProd.prodName
            qty = s.qtySold
            plist = list(filter(lambda x: x['prodname'] == pname, prodSales))

            if len(plist) > 0:
                prodSales = list(map(lambda x: {'prodname': pname, 'qty':int(x['qty'])+int(qty)}
                    if (x['prodname'] == pname) else (x), prodSales))
            else:
                prodSales.append({'prodname': pname, 'qty': qty})

        pSortedList = sorted(prodSales, key=lambda k: k['qty'], reverse = True)

        print('List of best seller products')
        for p in pSortedList:
            print(f"Product: {p['prodname']}\n")
            print(f"Qty sold: {p['qty']}\n")

    
    def showSales(self, dtstart, dtend):
        allSales = SalesDAO.readSoldProd()
        dts = datetime.strptime(dtstart,'%d/%m/%Y')
        dte = datetime.strptime(dtend, '%d/%m/%Y')
        dtSales = list(filter(lambda x: 
                              datetime.strptime(x.dateSold, '%d/%m/%Y') >= dts and
                              datetime.strptime(x.dateSold, '%d/%m/%Y') <= dte, allSales))
        for s in dtSales:
            mydt = datetime.strptime(s.dateSold, '%d/%m/%Y').date()
            print(
                f"{s.soldProd.prodName}: {s.qtySold} pieces sold on {mydt.strftime('%d/%m/%Y')}")



class SupplierController:
    def newSupplier(self, suppEIN, suppName, suppTel, suppCat):
        supps = SupplierDAO.readSuppliers()
        foundEIN = list(filter(lambda x: 
            x.suppEIN == suppEIN or
            x.suppTel == suppTel, supps))

        if len(foundEIN) > 0:
            print('Supplier EIN or Telephone already exists!')
        elif len(suppEIN) == 10 and len(suppTel) == 12:
            print('New supplier saved!')
            SupplierDAO.saveSupplier(Supplier(
                suppEIN,
                suppName,
                suppTel,
                suppCat
            ))
        else:
            print('Invalid EIN and/or phone number!')


    def updateSupplier(self, updSuppEIN, updSuppName, updSuppTel, updSuppCat):
        supps = SupplierDAO.readSuppliers()
        foundEIN = list(filter(lambda x: x.suppEIN == updSuppEIN, supps))
        if len(foundEIN) > 0:
            lsupps = list(map(lambda x: Supplier(
                updSuppEIN,
                updSuppName,
                updSuppTel,
                updSuppCat
            )if (x.suppEIN == updSuppEIN)
                else (x), supps))

            fsup = open('suppliers.txt','w')
            fsup.close()
            for sup in lsupps:
                SupplierDAO.saveSupplier(Supplier(
                    sup.suppEIN,
                    sup.suppName,
                    sup.suppTel,
                    sup.suppCat
                ))

            print('Supplier information updated!')
        else:
            print('Supplier EIN not found!')


    def delSupplier(self, delSuppEIN):
        supps = SupplierDAO.readSuppliers()
        foundEIN = list(filter(lambda x: x.suppEIN == delSuppEIN, supps))
        if len(foundEIN) > 0:
            for i in range(len(supps)):
                if supps[i].suppEIN == delSuppEIN:
                    del supps[i]
                    break
        else:
            print('Supplier to be deleted does not exist!')
            return None

        fsup = open('suppliers.txt', 'w')
        fsup.close()
        for sup in supps:
            SupplierDAO.saveSupplier(Supplier(
                sup.suppEIN,
                sup.suppName,
                sup.suppTel,
                sup.suppCat
            ))

        print('Supplier has been deleted!')


    def showSupplier(self):
        supps = SupplierDAO.readSuppliers()
        if len(supps) == 0:
            print('Suppliers file is empty!')
        else:
            print('=== Supliers Sorted by Name ===')
            sortsups = sorted(
                supps, key=lambda k: k.suppName)
            for sup in sortsups:
                print(f'EIN: {sup.suppEIN}')
                print(f'Name: {sup.suppName}')
                print(f'Phone: {sup.suppTel}')
                print(f'Cat.: {sup.suppCat}\n')



class CustomerController:
    def newCustomer(self, perSSN, perName, perEmail, perPhone, perAddress):
        persons = PersonDAO.readPersons()
        foundPerson = list(filter(lambda x:
                                  x.perSSN == perSSN or
                                  x.perEmail == perEmail or
                                  x.perPhone == perPhone, persons))

        if len(foundPerson) > 0:
            print('Person SSN, E-mail or Phone already exists!')
        elif len(perSSN) == 11 and len(perPhone) == 12:
            print('New person saved!')
            PersonDAO.savePerson(Person(
                perSSN,
                perName,
                perEmail,
                perPhone,
                perAddress
            ))
        else:
            print('Invalid SSN, E-mail and/or Phone number!')


    def updateCustomer(self, perSSN, perUpdEmail, perUpdPhone, perUpdAddress):
        custs = PersonDAO.readPersons()
        foundSSN = list(filter(lambda x: x.perSSN == perSSN, custs))
        if len(foundSSN) > 0:
            lcusts = list(map(lambda x: Person(
                perSSN,
                x.perName,
                perUpdEmail,
                perUpdPhone,
                perUpdAddress
            )if (x.perSSN == perSSN)
                else (x), custs))

            fcust = open('persons.txt', 'w')
            fcust.close()
            for cust in lcusts:
                PersonDAO.savePerson(Person(
                    cust.perSSN,
                    cust.perName,
                    cust.perEmail,
                    cust.perPhone,
                    cust.perAddress
                ))

            print('Person information updated!')
        else:
            print('Person SSN not found!')


    def delCustomer(self, delPerSSN):
        custs = PersonDAO.readPersons()
        foundCust = list(filter(lambda x: x.perSSN == delPerSSN, custs))
        if len(foundCust) > 0:
            for i in range(len(custs)):
                if custs[i].perSSN == delPerSSN:
                    del custs[i]
                    break
        else:
            print('Customer to be deleted does not exist!')
            return None

        fcust = open('persons.txt', 'w')
        fcust.close()
        for cust in custs:
            PersonDAO.savePerson(Person(
                cust.perSSN,
                cust.perName,
                cust.perPhone,
                cust.perEmail,
                cust.perAddress
            ))

        print('Customer has been deleted!')


    def showCustomers(self):
        custs = PersonDAO.readPersons()
        if len(custs) == 0:
            print('Customer file is empty!')
        else:
            print('=== Customers Sorted by Name ===')
            sortCus = sorted(
                custs, key=lambda k: k.perName)
            for cus in sortCus:
                print(f'SSN: {cus.perSSN}')
                print(f'Name: {cus.perName}')
                print(f'Phone: {cus.perPhone}')
                print(f'E-mail: {cus.perEmail}')
                print(f'Address: {cus.perAddress}\n')



class EmployeeController:
    def newEmployee(self, empID, empName, empSSN, empEmail, empPhone, empAddress):
        emps = EmployeeDAO.readEmployees()
        foundEmpID    = list(filter(lambda x:x.empID == empID, emps))
        foundEmpSSN = list(filter(lambda x: x.perSSN == empSSN, emps))
        foundEmpEmail = list(filter(lambda x: x.perEmail == empEmail, emps))

        if len(foundEmpSSN) > 0:
            print('Employee SSN already exists!')
        elif len(foundEmpID) > 0:
            print('Employee ID already exists!')
        elif len(foundEmpEmail) > 0:
            print('Employee email already exists!')
        elif len(empSSN) == 11 and len(empPhone) == 12:
            print('New employee saved!')
            EmployeeDAO.saveEmployee(Employee(
                empID,
                empSSN,
                empName,
                empEmail,
                empPhone,
                empAddress
            ))
        else:
            print('Invalid SSN and/or Phone number!')


    def updateEmployee(self, empID, perSSN, perUpdEmail, perUpdPhone, perUpdAddress):
        emps = EmployeeDAO.readEmployees()
        foundEmpID = list(filter(lambda x: 
            x.empID  == empID and
            x.perSSN == perSSN, emps))

        if len(foundEmpID) > 0:
            lemps = list(map(lambda x: Employee(
                empID,
                x.perName,
                perSSN,
                perUpdEmail,
                perUpdPhone,
                perUpdAddress
            )if (x.empID == empID and x.perSSN == perSSN)
                else (x), emps))

            femp = open('employees.txt', 'w')
            femp.close()
            for emp in lemps:
                EmployeeDAO.saveEmployee(Employee(
                    emp.empID,
                    emp.perName,
                    emp.perSSN,
                    emp.perEmail,
                    emp.perPhone,
                    emp.perAddress
                ))

            print('Employee information updated!')
        else:
            print('Employee ID or SSN not found!')


    def delEmployee(self, delEmpID):
        emps = EmployeeDAO.readEmployees()
        foundEmp = list(filter(lambda x: x.empID == delEmpID, emps))
        if len(foundEmp) > 0:
            for i in range(len(emps)):
                if emps[i].empID == delEmpID:
                    del emps[i]
                    break
        else:
            print('Employee to be deleted does not exist!')
            return None

        femp = open('employees.txt', 'w')
        femp.close()
        for emp in emps:
            EmployeeDAO.saveEmployee(Employee(
                emp.empID,
                emp.perSSN,
                emp.perName,
                emp.perPhone,
                emp.perEmail,
                emp.perAddress
            ))

        print('Employee has been deleted!')


    def showEmployees(self):
        emps = EmployeeDAO.readEmployees()
        if len(emps) == 0:
            print('Employee file is empty!')
        else:
            print('=== Employees Sorted by Name ===')
            sortEmps = sorted(
                emps, key=lambda k: k.perName)
            for emp in sortEmps:
                print(f'ID: {emp.empID}')
                print(f'SSN: {emp.perSSN}')
                print(f'Name: {emp.perName}')
                print(f'Phone: {emp.perPhone}')
                print(f'E-mail: {emp.perEmail}')
                print(f'Address: {emp.perAddress}\n')


#c = CategoryController()
#c.delCategory('Veggies')
#fromCat = 'Veggies'
#toCat = 'Fish'
#c.updateCategory(fromCat, toCat)
#c.listCategories()
#s = StockController()
#s.newStockProduct('5','Potato','3','Veggies',10)
#s.delStockProduct('Orange')
#s.updateStockProduct('Potato', '4', '210')
#s.listStockProducts()
#sp = SalesController()
#sp.addNewSales('Potato', 'Jonecir', 'Eliane', 10)
#sp.addNewSales('Potato', 'Jonecir', 'Eliane', 20)
#sp.addNewSales('Potato', 'Jonecir', 'Eliane', 30)
#sp.salesReport()
#sp.showSales('23/7/2022','04/08/2022')

#sup = SupplierController()
#sup.newSupplier('51-5503744', 'Cotsco', '953-227-5501', 'Veggies')
#sup.updateSupplier('51-5503744', 'Cotsco', '953-227-5503', 'Veggies')
#sup.delSupplier('40-3403778')
#sup.showSupplier()

#cus = CustomerController()
#cus.newPerson('383-21-2923', 'Jonecir Souza', 'jonecir@gmail.com', '954-148-0680','525 Blue Lake Dr., Pompano Beach, FL')
#cus.newPerson('385-12-9341', 'Eliane Souza', 'elianes@gmail.com', '954-358-1656','525 Blue Lake Dr., Pompano Beach, FL')
#cus.updateCustomer('383-21-2923', 'jonecir@gmail.com', '954-785-0680','101 Walton Blv., Rochester Hills, MI')
#cus.delCustomer('385-12-9341')
#cus.showCustomers()


#emp = EmployeeController()
#emp.newEmployee('1002', 'Eliane Souza', '253-23-2133', 'eliane@gmail.com',
#                '954-148-0680', '525 Blue Lake Dr., Pompano Beach, FL')
#emp.updateEmployee('1001','383-21-2923','jonecir@hotmail.com','587-387-4787','35 A1A Av., Forth Lauderdate, FL')
#emp.delEmployee('1002')

#emp.showEmployees()
