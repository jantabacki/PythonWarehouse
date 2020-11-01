import os.path
from os import path
from entites.Product import Product

class FileStorage:

    def __init__(self, fileName):
        self.fileName = fileName
        self.products = []
        if not path.exists(fileName):
            open(fileName, "w").close
        pass
    
    def LoadData(self):
        self.products = []
        file = open(self.fileName, "r")
        lines = file.readlines()
        for line in lines:
            splittedLine = line.split(";")
            self.products.append(Product(splittedLine[0], splittedLine[1], int(splittedLine[2]), int(splittedLine[3])))
            pass
        file.close()
        pass        

    def SaveData(self):
        file = open(self.fileName, "w")
        for product in self.products:
            file.write(product.name + ";" + product.description + ";" + str(product.mass) + ";" + str(product.count) + ";" + "\n")
            pass
        file.close()
        pass