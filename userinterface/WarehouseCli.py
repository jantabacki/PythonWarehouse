from entites.Product import Product
from terminaltables import AsciiTable
from colorama import init, Fore, Back, Style

class WarehouseCli:
    def __init__(self, dataManager, fileStorage):
        self.dataManager = dataManager
        self.fileStorage = fileStorage
        pass

    def addProductCommand(self):
        name = input("New product's name: ")
        description = input("New product's description: ")
        mass = int(input("New product's mass: "))
        self.dataManager.products.append(Product(name, description, mass, 0))
        print(Fore.GREEN + "done" + Fore.RESET)
        pass

    def removeProductCommand(self):
        index = input("Type product's index: ")
        self.dataManager.removeProduct(self.dataManager.getProducts()[int(index)])
        print(Fore.GREEN + "done" + Fore.RESET)
        pass

    def showAllProductsCommand(self):
        index = 0
        table_data = [["ID", "Name", "Description", "Mass", "Count"]]
        for prod in self.dataManager.getProducts():
            table_data.append(
                [str(index), prod.name, prod.description, str(prod.mass), str(prod.count)])
            index += 1
            pass
        table = AsciiTable(table_data)
        print(table.table)
        pass

    def increaseCountCommand(self):
        index = input("Type product's index: ")
        count = input("Increase count: ")
        self.dataManager.increaseProductCount(
            self.dataManager.getProducts()[int(index)], int(count))
        print(Fore.GREEN + "done" + Fore.RESET)
        pass

    def decreaseCountCommand(self):
        index = input("Type product's index: ")
        count = input("Decrease count: ")
        self.dataManager.decreaseProductCount(
            self.dataManager.getProducts()[int(index)], int(count))
        print(Fore.GREEN + "done" + Fore.RESET)
        pass

    def saveCommand(self):
        self.fileStorage.products = self.dataManager.products
        self.fileStorage.SaveData()
        print(Fore.GREEN + "done" + Fore.RESET)
        pass

    def helpCommand(self):
        table_data = [
            ["Command", "Description"],
            ["AddProduct", "Allows to add new product to database."],
            ["ShowAllProducts", ""],
            ["RemoveProduct", ""],
            ["IncreaseCount", ""],
            ["DecreaseCount", ""],
            ["Save", ""],
            ["Help", ""],
            ["Exit", ""]
        ]
        table = AsciiTable(table_data)
        print(table.table)
        pass

    @staticmethod
    def default(self):
        print(Fore.RED + "Invalid command" + Fore.RESET)
        pass

    switch_case = {
        "addproduct": addProductCommand,
        "showallproducts": showAllProductsCommand,
        "removeproduct": removeProductCommand,
        "increasecount": increaseCountCommand,
        "decreasecount": decreaseCountCommand,
        "save": saveCommand,
        "help": helpCommand
    }

    def start(self):
        command = ""
        while True:
            command = input("Type command: ").lower()
            if command == "exit":
                break
            self.switch_case.get(command, self.default)(self)
            pass
        pass