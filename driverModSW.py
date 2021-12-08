from classModSW import ItemsListSW #import class

#the function that creates the list of the items
def makeListSW(): 
    buyList = []
    itemChecker = 0

    #check for input less than or equal to 0, if yes, loop the input.
    while itemChecker <= 0: 
        itemChecker = int(input("How many items will be ordered today? "))
        if itemChecker <= 0:
            print("You can only order at least 1 item, please try again.")
        print() #spacing

    #start the input of items based on the number of orders inputted.
    for i in range(itemChecker): 
        print(f"Item #{i+1} -") #item name counter
        name = str(input("Enter Food: "))

        amount = 0
        amount = float(input("Enter the amount of pounds: "))
        #check for input less than or equal to 0, if yes, loop the input.
        while amount <= 0: 
            print("You cannot enter an amount less than 1, please try again.")
            amount = float(input("Enter the amount of pounds: "))
        print() #spacing

        buyList.append(ItemsListSW(name, amount)) #append both name and amount
    return buyList

#function to create the receipt text.
def receiptSW(list): 
    print("Here is your receipt of the list of item(s) ordered: ")
    print("------------------------------------------------------------")
    for ItemsListSW in list: #loop that prints items based on the list created earlier.
        print(f"           Item:  {ItemsListSW.getNameSW()}")
        print(f" Amount Ordered:  {ItemsListSW.getAmountSW():.1f} lbs")
        print(f"Price per Pound:  ${ItemsListSW.getPriceSW():.2f}")
        print(f" Price of Order:  ${ItemsListSW.getCalcinPSW():.2f}")
        print()


#function to calculate the total price of all items
def finalPriceSW(list): 
    final = 0
    for j in list: #loop for the amount of times needed to be calculated based on the # of items ordered.
        final = j.getCalcinPSW() + final
    print(f"The total cost of your order is ${final:.2f}") #print the final cost of order.
    print() #spacing
    #guide the user of any mistakes they have made.
    print("If one of your orders unintentionally reads $0.00, that means you've probably misinputed the item name. Please go back and redo the process. We apologize for any inconvienience this may cause.")


def main(): #function to call all of the functions in this script.
    list = makeListSW()
    receiptSW(list)
    finalPriceSW(list) 

main() #run the main function to run all other functions