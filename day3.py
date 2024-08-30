from xml.dom.minidom import ProcessingInstruction

print("welcome to rollercoster")
height = int(input("what is your height in cm"))
if height > 120:
    print("it is greater then 120")
    age = int(input("enter age"))
    if age <= 12:
        print("pay 5")
    elif age >= 12 & age <= 18:
        print("pay 7")
    else:
        print("pay 10")
else:
    print("it is less then 120")


check_number = int(input("enter the number that you want to check?"))
if check_number % 2 == 0:
    print("this is even number")
elif check_number % 2 == 1:
    print("this is odd number")
else:
    print("this this is not a number  ")

