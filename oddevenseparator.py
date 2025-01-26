def oddevenseparator(array):
    odd=[]
    even=[]
    for i in array:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Odd Numbers are {odd}")
    print(f"Even Numbers are {even}")
def main():
    array=[]
    while True:
        choice =input("Do you want to Continue Y or N?")
        if choice=='y' or choice=='Y':
            print("Enter the Number")
            value=input()
            if value.isdigit():
                value=int(value)
                array.append(value)
            else:
                print("Enter a Valid input")
                value=input()
                while not(value.isdigit()):
                    print("Enter a Valid input")
                    value=input()
                value=int(value)
                array.append(value)
        elif choice=='n' or choice=='N':
            break
        else:
            print("Invalid Choice")
            continue
    oddevenseparator(array)
main()