programming_dictionary = {
    "Bub": " an error in a program that prevents the program from running as expected",
    "Funtion": "a piece of code that you can easily call over and over again",
    "loop": "the action of doing something over and over again "
}
#print(programming_dictionary["Bub"])
#programming_dictionary["Loop"] = "the action of doing something over and over again "
#print(programming_dictionary)
#empty_dictionary = {}
# wipe an existing dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

dictionary = {
    "france":["paris","marsel","lion"],
    "germany":["berlin","dordmund"]

}
print(dictionary["germany"])
nested_list = ["a","b",["c","d"]]

print(nested_list[2][1])

dictionary = {
    "france":{
        "visited_cities": ["paris","marsel","lion"],
        "total": 2
    },
    "germany":["berlin","dordmund"]

}
print(dictionary["france"]["visited_cities"][2])