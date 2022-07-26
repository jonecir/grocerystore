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
        else:
            print('Category does not exist! Please verify.')


    def updateCategory(self,fromCat, toCat):
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
        else:
            print('Sorry, category not found!')


#c = CategoryController()
#c.delCategory('Veggies')
#fromCat = 'Veggies'
#toCat = 'Fish'
#c.updateCategory(fromCat, toCat)
