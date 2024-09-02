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