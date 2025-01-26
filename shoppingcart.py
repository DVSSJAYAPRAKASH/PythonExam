def additems():
    itemname=input("Enter the Item Name: ")
    itemnamelist.append(itemname)
    itemprice=float(input("Enter the Item Price: "))
    itempricelist.append(itemprice)
    print("Items added to cart")

def viewcart():
    print("Items in cart")
    print()
    for i in range(len(itemnamelist)):
        print(f"Item Name: {itemnamelist[i]}")
        print(f"Item Price: {itempricelist[i]}")
        print()

def totalprice():
    totalpricevalue=0
    for i in range(len(itempricelist)):
        totalpricevalue=totalpricevalue+itempricelist[i]
    print(f"Total Price: {totalpricevalue}")

def main():
    global itemnamelist 
    itemnamelist=[]
    global itempricelist
    itempricelist=[]
    while True:
        print()
        print("1. Add Items to Cart")
        print("2. View Items in Cart")
        print("3. Total Price")
        print("4. Exit")
        print()
        choice = (input("Enter the Choice You Want!: "))
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid Choice")
            continue 
        if choice < 1 or choice > 4:
            print("You Entered Invalid Choice")
            continue
        elif choice == 1:
            additems()
        elif choice == 2:
            viewcart()
        elif choice == 3:
            totalprice()
        else:
            exit()
main()