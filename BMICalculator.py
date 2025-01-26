def BMI():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    height = height/100  # Converting height from cm to m
    bmi = weight/(height**2) # Formula for calculating BMI
    print("Your BMI is: ", bmi)
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 24.9:
        print("You are Normal.")
    elif bmi >= 24.9 and bmi < 29.9:
        print("You are Overweight.")
    else:
        print("You are Obese.")
def main():
    while True:
        print()
        print("1. Calculate BMI")
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
            BMI()
        else:
            exit()
main()