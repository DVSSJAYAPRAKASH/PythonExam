def LoanEligibility():
    age = int(input("Enter your age: "))
    salary = int(input("Enter your salary: "))
    creditscore = int(input("Enter your credit score: "))
    print()
    if age >= 18 and salary >= 25000 and creditscore >= 650:
        print("You are eligible for loan.")
    else:
        print("You are not eligible for loan.")
def main():
    while True:
        print()
        print("1. Check Loan Eligibility")
        print("2. Exit")
        print()
        choice = input("Enter the Choice You Want!: ")
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid Choice")
            continue
        if choice < 1 or choice > 2:
            print("You Entered Invalid Choice")
            continue
        elif choice == 1:
            LoanEligibility()
        else:
            exit()
main()