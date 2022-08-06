#!python3

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
sp = SalesController()
#sp.addNewSales('Carrots', 'Jonecir', 'Eliane', 10)
sp.salesReport()