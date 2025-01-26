def multiplicationtable(n,a,b):
    for i in range(a,b+1):
        print(n,'x',i,'=',n*i)
def main():
    n=int(input("Enter the Number for Multiplication Table: "))
    a=int(input("Enter the Starting Range: "))
    b=int(input("Enter the Ending Range: "))
    multiplicationtable(n,a,b)
main()