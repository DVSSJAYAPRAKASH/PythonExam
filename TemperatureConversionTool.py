def celsius():
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32   # Formula for converting Celsius to Fahrenheit
    print(f"The temperature in Fahrenheit is {fahrenheit}F")
    kelvin = celsius + 273  # Formula for converting Celsius to Kelvin
    print(f"The temperature in Kelvin is {kelvin}K")
def fahrenheit():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9 # Formula for converting Fahrenheit to Celsius
    print(f"The temperature in Celsius is {celsius}C")
    kelvin = (fahrenheit - 32) * 5/9 + 273   # Formula for converting Fahrenheit to Kelvin
    print(f"The temperature in Kelvin is {kelvin}K")
def kelvin():
    kelvin = float(input("Enter the temperature in Kelvin: "))
    celsius = kelvin - 273.15 # Formula for converting Kelvin to Celsius
    print(f"The temperature in Celsius is {celsius}C")
    fahrenheit = (kelvin - 273.15) * 9/5 + 32  # Formula for converting Kelvin to Fahrenheit
    print(f"The temperature in Fahrenheit is {fahrenheit}F")   
def main():
    while True:
        print()
        print("1. Celsius to Fahrenheit and Kelvin")
        print("2. Fahrenheit to Celsius and Kelvin")
        print("3. Kelvin to Celsius and Fahrenheit")
        print("4. Exit")
        print()
        choice = int(input("Enter the Choice You Want!: "))
        if choice < 1 or choice > 4:
            print("You Entered Invalid Choice")
            continue
        elif choice == 1:
            celsius()
        elif choice == 2:
            fahrenheit()
        elif choice == 3:
            kelvin()
        else:
            exit()
main()
