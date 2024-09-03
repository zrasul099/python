import random
import  my_module
import string


random_integer = random.randint(3,6)
print(random_integer)
print(my_module.my_number)
number_0_1 = random.random()

print(number_0_1)

random_float = random.uniform(1,13)
print(random_float)

random_head_tail = random.randint(0,1)
if random_head_tail == 0:
    print("head")
else:
    print("tail")

states = ["new jersey", "pensilvania ", "california", "illinois"]
print(states)

random_list = random.choices(states)

print(random_list)
random_index = random.randint(0,3)
print(states[random_index])

vegitable = ["strawberry", "lettus","berry ","watermelon"]
fruits = ["apple","pear","peach"]
dirty_dozen = [vegitable, fruits]
print(dirty_dozen)
print(dirty_dozen[1][1])