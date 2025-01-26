def factorial(n):
    if n == 0:
        return 1
    for i in range(1,n):
        n = n * i
    return n
def main():
    n = int(input("Enter the number: "))
    while n < 0:
            print("Factorial does not exist for negative numbers")
            n = int(input("Enter the number: "))
    print("Factorial of",n,"is",factorial(n))
main()