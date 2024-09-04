fruits = ["apple","peach","pear"]
for fruit in fruits:
    print(fruit)

student_score = [12,34,56,87,6,53,56,100]
total_exam = sum(student_score)
print(total_exam)
#print(max(student_score))


#summ = 0
#for score in student_score:
 #  summ = summ + score
  # print(summ)

i = 0
for score in student_score:
    if score > i:
        i = score
print(score)

#num = 0
#for number in range(1,20):
 #   print(number)
  #  num = num+number
#print(num)

for num in range(1,101):
    if num%3==0:
        print("Fizz")
    elif num%5==0:
        print("buzz")
    elif num%3==0 and num%5==0:
        print("FizzBuzz")
    else:
        print(num)