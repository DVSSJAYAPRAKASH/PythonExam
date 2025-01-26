def vowels(str):
    cnt = 0
    vowels = 'aeiou'
    for i in str:
        if i in vowels:
            cnt+=1
    return cnt
def consonants(str):
    cnt = 0
    consonants = 'bcdfghjklmnpqrstvwxyz'
    for i in str:
        if i in consonants:
            cnt+=1
    return cnt
    return cnt
def digits(str):
    cnt = 0
    digits = '0123456789'
    for i in str:
        if i in digits:
            cnt+=1
    return cnt
def specialcharacters(str):
    cnt = 0
    specialcharacters = '!@#$%^&*()_+'
    for i in str:
        if i in specialcharacters:
            cnt+=1
    return cnt

def stringanalyser():
    str = input("Enter a string: ")
    print()
    print(f"Number of vowels: {vowels(str)}")
    print(f"Number of consonants: {consonants(str)}")
    print(f"Number of digits: {digits(str)}")
    print(f"Number of special characters: {specialcharacters(str)}")
    print()
    print("String After Reversed:",str[::-1])
def main():
    while True:
        print()
        print("1. String Analyser")
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
            stringanalyser()
        else:
            exit()
main()