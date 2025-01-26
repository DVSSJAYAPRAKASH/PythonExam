import math
def secondlargestnumber(array):
    if len(array)<2:
        print("Invalid Input")
        return
    maxi=-math.inf
    secondmaxi=-math.inf
    for i in array:
        if i>maxi:
            secondmaxi=maxi
            maxi=i
        elif i>secondmaxi and i<maxi:
            secondmaxi=i
    if secondmaxi==-math.inf:
        print("There is no Second Largest Number")
        return
    print(f"Second Largest Number is {secondmaxi}")
def main():
    array=[]
    while True:
        choice =input("Do you want to Continue Y or N?")
        if choice=='y' or choice=='Y':
            value=input()
            if value.isdigit():
                value=int(value)
                array.append(value)
            else:
                print("Enter a Valid input")
                while not(value.isdigit()):
                    value=input()
                value=int(value)
                array.append(value)
        else:
            break
    secondlargestnumber(array)
main()

        
