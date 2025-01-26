def take_input():
    global total
    global people
    global tip
    total=input("Total Bill Amount: ")
    if total.isdigit():
        total=int(total)
    else:
        print("Invalid Amount")
        total=input("Total Bill Amount: ")
        while not(total.isdigit()):
            print("Invalid Amount")
            total=input("Total Bill Amount: ")
        total=int(total)
    people=input("Number of People: ")
    if people.isdigit():
        people=int(people)
    else:
        print("Invalid Number")
        people=input("Number of People:")
        while not(people.isdigit()):
            print("Invalid Number")
            people=input("Number of People: ")
        people=int(people)
    tip=input("Tip Amount: ")
    if tip.isdigit():
        tip=int(tip)
    else:
        print("Invalid Amount")
        tip=input("Tip Amount")
        while not(tip.isdigit()):
            print("Invalid Amount")
            tip=input("Tip Amount")
        tip=int(tip)
def billsplitter():
    global total
    global people
    global tip
    print()
    print("Welcome to the Bill Splitter")
    print()
    take_input()
    print()
    print(f"Total Bill Amount: Rs {total}")
    print(f"Number of People: {people}")
    print(f"Tip Amount: Rs {tip}")
    print()
    total+=tip
    eachperson=total/people
    print(f"Each Person has to pay: Rs {eachperson}")
def main():
    while True:
        print()
        print("1. Bill Splitter")
        print("2. Exit")
        print()
        choice=input("Enter the Choice You Want!: ")
        if choice.isdigit():
            choice=int(choice)
        else:
            print("Invalid Choice")
            continue
        if choice<1 or choice>2:
            print("You Entered Invalid Choice")
            continue
        elif choice==1:
            billsplitter()
        else:
            exit()
main()
