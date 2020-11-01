class DataManager:

    def __init__(self):
        self.products = []
    pass
    
    def addNewProduct(self, product):
        self.products.append(product)
    pass
    
    def getProducts(self):
        return self.products
    pass

    def getProductsByName(self, name):
        foundProducts = []
        for product in self.products:
            if product.name == name:
                foundProducts.append(product)
                pass
            pass
        return foundProducts

    def increaseProductCount(self, product, increaseValue):
        for currentProduct in self.products:
            if currentProduct == product:
                currentProduct.count += increaseValue
                break
            pass
        pass
    pass

    def decreaseProductCount(self, product, decreaseValue):
        for currentProduct in self.products:
            if currentProduct == product:
                currentProduct.count -= decreaseValue
                break
            pass
        pass
    pass

    def removeProduct(self, product):
        self.products.remove(product)
    pass