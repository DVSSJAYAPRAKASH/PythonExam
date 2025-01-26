import math
def isprime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0):
            return False
    return True
def take_input():
    start=input("Enter Starting range :")
    if start.isdigit():
        start=int(start)
    else:
        print("Invalid value Provide Valid Input")
        start=input("Enter Starting range :")
        while not(start.isdigit()):
            start=input("Enter Starting range :")
        start=int(start)
    end=input("Enter Ending range :")
    if end.isdigit():
        end=int(end)
    else:
        print("Invalid value Provide Valid Input")
        end=input("Enter Starting range :")
        while not(end.isdigit()):
            end=input("Enter Starting range :")
        end=int(end)
    if start>end:
        print("Entered range is Invalid!!!")
        return
    for i in range(start,end+1):
        if isprime(i):
            print(i,end=" ")
def main():
    take_input()

main()

        
