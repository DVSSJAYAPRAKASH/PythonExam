def isLeapyear(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                print("Leap Year")
            else:
                print("Not Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not Leap Year")
def take_input():
    while True:
        n=int(input("Enter the year: "))
        isLeapyear(n)
        print()
        print("1.Continue")
        print("2.Exit")
        print()
        choice=int(input("Enter Your Choice: "))
        print()
        if choice==1:
            continue
        elif choice==2:
            exit()
        else:
            print("Invalid Choice")
            continue
def main():
    take_input()
main()