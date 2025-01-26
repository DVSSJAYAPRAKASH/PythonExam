def inputfun():
    global name
    name=input("Enter Your name: ")
    print("Enter the Marks of 5 Subjects")
    global sub1
    sub1 = int(input("Enter the Marks of Subject 1:"))
    while (sub1<0 or sub1>100):
        print("Invalid Marks")
        sub1 = int(input("Enter the Marks of Subject 1:"))
    if sub1<40:
        print("Fail!!!")
        exit()
    global sub2
    sub2 = int(input("Enter the Marks of Subject 2: "))
    while sub2<0 or sub2>100:
        print("Invalid Marks")
        sub2 = int(input("Enter the Marks of Subject 2: "))
    if sub2<40:
        print("Fail!!!")
        exit()
    global sub3
    sub3 = int(input("Enter the Marks of Subject 3: "))
    while sub3<0 or sub3>100:
        print("Invalid Marks")
        sub3 = int(input("Enter the Marks of Subject 3: "))
    if sub3<40:
        print("Fail!!!")
        exit()
    global sub4
    sub4 = int(input("Enter the Marks of Subject 4: "))
    while sub4<0 or sub4>100:
        print("Invalid Marks")
        sub4 = int(input("Enter the Marks of Subject 4: "))
    if sub4<40:
        print("Fail!!!")
        exit()
    global sub5
    sub5 = int(input("Enter the Marks of Subject 5: "))
    while sub5<0 or sub5>100:
        print("Invalid Marks")
        sub5 = int(input("Enter the Marks of Subject 5: "))
    if sub5<40:
        print("Fail!!!")
        exit()
def calculate():
    global total
    total = sub1+sub2+sub3+sub4+sub5
    global percentage
    percentage = total/5
def grade():
    if percentage>=85:
        print("Grade A")
    elif percentage>=70 and percentage<85:
        print("Grade B")
    elif percentage>=60 and percentage<70:
        print("Grade C")
    elif percentage>=40 and percentage<60:
        print("Grade D")
    else:
        print("Grade F")
def main():
    inputfun()
    calculate()
    print(f"Name : {name}")
    print(f"Marks : {total}")
    print(f"Percentage : {percentage}")
    grade()
main()
