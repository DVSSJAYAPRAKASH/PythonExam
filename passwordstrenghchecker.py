def passwordstrengthchecker():
    digit=0
    upper=0
    lower=0
    special=0
    password = input("Enter your password: ")
    if len(password) < 8:
        print("invalid password")
        return
    for i in password:
        if i.isdigit():
            digit+=1
        # elif i.isalpha():
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif not(i.isalnum()):
            special+=1
    if digit>0 and upper>0 and lower>0 and special>0:
        print()
        print("valid password")
    else:
        print()
        print("invalid password")
def main():
    while True:
        print()
        print("1.Password Strength Checker")
        print("2.Exit")
        print()
        choice=int(input("Enter Your Choice: "))
        print()
        if choice==1:
            passwordstrengthchecker()
        elif choice==2:
            exit()
        else:
            print("Invalid Choice")
            continue
main()

    
    