def palindrome(n):
    n=str(n)
    if n==n[::-1]:
        print()
        print("Palindrome")
    else:
        print()
        print("Not Palindrome")
def take_input():
    n=(input("Enter the value: "))
    palindrome(n)
def main():
    while True:
        print()
        print("1.Palindrome Checker")
        print("2.Exit")
        print()
        choice=int(input("Enter Your Choice: "))
        print()
        if choice==1:
            take_input()
        elif choice==2:
            exit()
        else:
            print("Invalid Choice")
            continue
main()