def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()
def main():
    n=int(input("Enter User Input: "))
    pattern(n)

main()