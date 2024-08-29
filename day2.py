print(len("hello"))
print(type("hello"))
print(type(2))
print(type(True))
print(type(4.43234))
print(int("123") + int("234"))

name_of_user = input("enter the name")
lenth_of_name = len(name_of_user)
print(name_of_user + str(lenth_of_name))

print(11+11)
print(22-11)
print(22 / 11)
print(22 * 11)

score = 0
score += 1
print(score)
print("your score is " + str(score))
height = 1.8
is_winning = True
print(f"your score is  {score}" + f"your height is {height}" + f" you are winning {is_winning}" )

total_price  = float(input("How much is total price"))
tips_persentage = float(input("how much tips would like to give?"))
tips_amount = (total_price/100)*tips_persentage

people = int(input("how many people are you dividing?"))
each_person =  (total_price+tips_amount) / people

print(total_price)
print(tips_amount)
print(people)
print(each_person )