from xml.dom.minidom import ProcessingInstruction

print("welcome to rollercoster")
height = int(input("what is your height in cm"))
bill = 0
if height > 120:
    print("it is greater then 120")
    age = int(input("enter age"))
    if age <= 12:
        bill = 5
        print(bill)
    elif age >= 12 & age <= 18:
        bill = 7
        print(bill)
    else:
        bill = 10
        print(bill)

    wants_photo = input("do you want a photo? Answer yes or no")
    photo = 3
    if wants_photo == "yes":
        print(bill + photo)
    else:
        print(bill)
else:
    print("it is less then 120")


check_number = int(input("enter the number that you want to check?"))
if check_number % 2 == 0:
    print("this is even number")
elif check_number % 2 == 1:
    print("this is odd number")
else:
    print("this this is not a number  ")

size = input("enter S, M, or L")
pepperoni = input("do want pepperoni? answer Y or N")
extra_chese = input("do you want extra chese? enter Y or N")
total_bill = 0

if size == "S":
    total_bill  = 10
elif size == "M":
    total_bill = 15
elif size == "L":
    total_bill = 20
else:
    print("we dont have that pizza")

if pepperoni == "Y":
    total_bill += 5
if  extra_chese == "Y":
    total_bill += 4

else:
    total_bill += 0

print(total_bill)


