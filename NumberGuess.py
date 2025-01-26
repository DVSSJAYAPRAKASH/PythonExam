import random
def randomGen():
    global randint
    randint=random.randint(1,100) # Generates Random int from 1 to 100.
def Guess():
    userinput= (input("Enter the Number You Guessed(1 to 100)!: "))
    if userinput.isdigit():
        userinput=int(userinput)
    else:
        print("Invalid Input! Enter Number")
        return
    if userinput<1 or userinput>100:
        print("Outof Range Guess in between 1 to 100")
    if userinput==randint:
        print("Hey User! ")
        print("Congratulations You Guessed Right! ")
        exit()
    elif userinput>randint:
        print("Its too Big !")
        print("Try Thinking of Small Number")
    elif userinput<randint:
        print("Its too Small")
        print("Try Guessing of Large Number")
def main():
    randomGen()
    while True:
        s=input("Want to Continue Y or N? ")
        if s=='Y' or s=='y':
            Guess()
        elif s=='N' or s=='n':
            print("Exiting the Game!")
            exit()
        else:
            print("Enter Valid Choice!!")
            continue
main()