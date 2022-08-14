#!python3
import Controller
import os.path

from Model import prodStock

if __name__ == "__main__":
    while True:
        local = int(input("Enter 1 for (Category)\n"
                          "Enter 2 for (Stock)\n"
                          "Enter 3 for (Supplier)\n"
                          "Enter 4 (Customer)\n"
                          "Enter 5 (Employee)\n"
                          "Enter 6 for (Sales)\n"
                          #"Enter 7 for best seller products\n"
                          "Enter 7 to Exit\n"))

        if local == 1:
            cat = Controller.CategoryController()
            while True:
                catOption = int(input("Enter 1 to create a new category\n"
                                    "Enter 2 to remove a category\n"
                                    "Enter 3 to edit a category\n"
                                    "Enter 4 to view all categories\n"
                                    "Enter 5 to Exit\n"))

                if catOption == 1:
                    catname = input(
                        "Enter category name: \n")
                    cat.newCategory(catname)
                elif catOption == 2:
                    catname = input(
                        "Enter category name to be removed: \n")
                    cat.delCategory(catname)
                elif catOption == 3:
                    catname = input(
                        "Enter category name: \n")
                    newcat = input(
                        "Enter new category name: \n")
                    cat.updateCategory(catname, newcat)
                elif catOption == 4:
                    cat.listCategories()
                else:
                    break
        elif local == 2:
            sto = Controller.StockController()
            while True:
                stoOption = int(input("Enter 1 to create a new product\n"
                                      "Enter 2 to remove a product\n"
                                      "Enter 3 to edit a product\n"
                                      "Enter 4 to view all products\n"
                                      "Enter 5 to Exit\n"))
                if stoOption == 1:
                    prID = input(
                        "Enter product ID: \n")
                    prName = input(
                        "Enter product name: \n")
                    prPrice = input(
                        "Enter product price: \n")
                    prCat = input(
                        "Enter product cat: \n")
                    prQty = input(
                        "Enter product qty: \n")
                    sto.newStockProduct(prID, prName, prPrice,  prCat, prQty)
                elif stoOption == 2:
                    prodName = input(
                        "Enter product name to be removed: \n")
                    sto.delStockProduct(prodName)
                elif stoOption == 3:
                    prodName = input(
                        "Enter product name to updat: \n")
                    newPrice = input(
                        "Enter new product price: \n")
                    newQty = input(
                        "Enter product qty: \n")
                    sto.updateStockProduct(prodName, newPrice, newQty)
                elif stoOption == 4:
                    sto.listStockProducts()
                else:
                    break
        elif local == 3:
            sup = Controller.SupplierController()
            while True:
                supOption = int(input("Enter 1 to create a new supplier\n"
                                      "Enter 2 to remove a supplier\n"
                                      "Enter 3 to edit a supplier\n"
                                      "Enter 4 to view all supplier\n"
                                      "Enter 5 to Exit\n"))
                if supOption == 1:
                    supEIN = input(
                        "Enter supplier EIN: \n")
                    supName = input(
                        "Enter suplier name: \n")
                    supPhone = input(
                        "Enter supplier phone #: \n")
                    supCat = input(
                        "Enter supplier cat: \n")
                    sup.newSupplier(supEIN, supName, supPhone, supCat)
                elif supOption == 2:
                    supEIN = input(
                        "Enter supplier EIN: \n")
                    sup.delSupplier(supEIN)
                elif supOption == 3:
                    supEIN = input(
                        "Enter supplier EIN: \n")
                    supName = input(
                        "Enter suplier name: \n")
                    supPhone = input(
                        "Enter supplier phone #: \n")
                    supCat = input(
                        "Enter supplier cat: \n")
                    sup.updateSupplier(supEIN, supName, supPhone, supCat)
                elif supOption == 4:
                    sup.showSupplier()
                else:
                    break
        elif local == 4:
            cus = Controller.CustomerController()
            while True:
                cusOption = int(input("Enter 1 to create a new customer\n"
                                      "Enter 2 to remove a customer\n"
                                      "Enter 3 to edit a customer\n"
                                      "Enter 4 to view all customers\n"
                                      "Enter 5 to Exit\n"))
                if cusOption == 1:
                    perSSN = input(
                        "Enter customer SSN: \n")
                    perName = input(
                        "Enter customer name: \n")
                    perEmail = input(
                        "Enter customer email: \n")
                    perPhone = input(
                        "Enter customer phone #: \n")
                    perAddr = input(
                        "Enter customer address: \n")
                    cus.newCustomer(perSSN, perName, perEmail, perPhone, perAddr)
                elif cusOption == 2:
                    perSSN = input(
                        "Enter customer SSN: \n")
                    cus.delCustomer(perSSN)
                elif cusOption == 3:
                    perSSN = input(
                        "Enter customer SSN: \n")
                    perEmail = input(
                        "Enter customer email: \n")
                    perPhone = input(
                        "Enter customer phone #: \n")
                    perAddr = input(
                        "Enter customer address: \n")
                    cus.updateCustomer(perSSN, perEmail, perPhone, perAddr)
                elif cusOption == 4:
                    cus.showCustomers()
                else:
                    break
        elif local == 5:
            emp = Controller.EmployeeController()
            while True:
                empOption = int(input("Enter 1 to create a new employee\n"
                                      "Enter 2 to remove a employee\n"
                                      "Enter 3 to edit a employee\n"
                                      "Enter 4 to view all employees\n"
                                      "Enter 5 to Exit\n"))
                if empOption == 1:
                    empID = input(
                        "Enter employee EIN: \n")
                    empName = input(
                        "Enter employee name: \n")
                    empSSN = input(
                        "Enter employee SSN: \n")
                    empEmail = input(
                        "Enter employee email: \n")
                    empPhone = input(
                        "Enter employee phone #: \n")
                    empAddr = input(
                        "Enter employee address: \n")
                    emp.newEmployee(empID, empName, empSSN, empEmail, empPhone, empAddr)
                elif empOption == 2:
                    empID = input(
                        "Enter employee EIN: \n")
                    emp.delEmployee(empID)
                elif empOption == 3:
                    empID = input(
                        "Enter employee EIN: \n")
                    empSSN = input(
                        "Enter employee SSN: \n")
                    empEmail = input(
                        "Enter employee email: \n")
                    empPhone = input(
                        "Enter employee phone #: \n")
                    empAddr = input(
                        "Enter employee address: \n")
                    emp.updateEmployee(empID, empSSN, empEmail, empPhone, empAddr)
                elif empOption == 4:
                    emp.showEmployees()
                else:
                    break
        elif local == 6:
            sal = Controller.SalesController()
            while True:
                salOption = int(input("Enter 1 to create a new sale\n"
                                      "Enter 2 to view all sales\n"
                                      "Enter 3 to view sales report\n"
                                      "Enter 4 to Exit\n"))
                if salOption == 1:
                    prName = input('Enter product name:')
                    seller = input('Enter seller')
                    buyer = input('Enter buyer name:')
                    qty = input('Enter qty:')
                    sal.addNewSales(prName,seller, buyer, qty)
                elif salOption == 2:
                    std = input('Enter start date:')
                    edt = input('Enter end date:')
                    sal.showSales(std, edt)
                elif salOption == 3:
                    sal.salesReport()
                else:
                    break
        else:
            break
