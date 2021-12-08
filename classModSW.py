class ItemsListSW:
    def __init__(self, name, amount): #the initializing method
        self.__name = name #name of item
        self.__amount = amount #amount of item in pounds
        self.__price = self.foodPriceListSW() #the method for the list of prices for each item
        self.__calcPrice = self.calcingPriceSW() #the method for calculating the price by multiplying the amount and unit price

    def foodPriceListSW(self): #establish the food prices
        if self.__name == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__price = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.__name == "Moose Cheese":
            self.__price = 487.20
        elif self.__name == "White Truffles":
            self.__price = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__price = 270.81
        else: 
            self.__price = 0.00 #if user inputs name of item that does not correspond with list, do not add price
        
        return self.__price

    def calcingPriceSW(self): #calculating price method: added the function
        self.__calcPrice = self.__price * self.__amount
        return self.__calcPrice

    #functions that return values for all/accessors functions 
    def getNameSW(self):
        return self.__name
    def getAmountSW(self):
        return self.__amount
    def getPriceSW(self):
        return self.__price
    def getCalcinPSW(self):
        return self.__calcPrice
    
    