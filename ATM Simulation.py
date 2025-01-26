balance = 0
def checkbalance():
    print()
    print(f"Your current balance is Rs{balance}")
    print()
def deposit():
    deposit = float(input("Enter amount to be deposited: "))
    global balance
    if deposit < 0:
        print("Invalid amount")
        return
    balance += deposit
    print()
    print(f"Amount deposited: Rs {balance}")
def withdrawmoney():
    withdrawnamount = float(input("Enter amount to be withdrawn:"))
    global balance
    if withdrawnamount<0:
        print()
        print("Invalid amount")
        return
    if withdrawnamount > balance:
        print()
        print("Insufficient balance for Withdrawal")
        return
    balance -= withdrawnamount

def main():
    while True:
        print()
        print("1. CheckBalance")
        print("2. Want to Deposit Money")
        print("3. Want to WithDraw Money")
        print("4. Exit")
        print()
        choice=int(input("Enter the Choice You Want!: "))
        if choice<1 or choice>4:
            print("You Entered Invalid Choice")
            continue
        elif choice==1:
            checkbalance()
        elif choice==2:
            deposit()
        elif choice==3:
            withdrawmoney()
        else:
            exit()
main()
