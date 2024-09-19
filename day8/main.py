def greet():
    print("hello")
    print("hello")
    print("hello")
greet()

def greet_with_data(name):
    print(f"hello {name}")
    print(f"hello{name}")

greet_with_data("Rasul")
print("heloo")
print("hello")


def life_in_weeks(age):
    final_age = 90
    weeks_left = (final_age - age)*52
    print(weeks_left)
life_in_weeks(56)

def greet_with(name,location):
    print(f"hello {name}")
    print(f"hello {location}")
greet_with("Rasul","chicago hello Rasul")