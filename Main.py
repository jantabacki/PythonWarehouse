from entites.Product import Product
from datasource.FileStorage import FileStorage
from datamanagement.DataManager import DataManager
from userinterface.WarehouseCli import WarehouseCli
from terminaltables import AsciiTable
from colorama import init, Fore, Back, Style

init()

print("Starting data manager")
dataManager = DataManager()
print("Loading data from file")
fileStorage = FileStorage("save.txt")
fileStorage.LoadData()
dataManager.products = fileStorage.products
print(Fore.GREEN + "Client is ready" + Fore.RESET)

warehouseCli = WarehouseCli(dataManager, fileStorage)
warehouseCli.start()