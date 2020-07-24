#!/usr/local/bin/python3.7

#https://docs.python.org/3/tutorial/controlflo.html#for-statements


colours = ['red', 'blue', 'green']
for colour in colours:
    print (f"{colour}")

# working with dictionarys
ages ={'david': 29, 'alex': 50, 'simon': 60}
print (f"{ages}")
for key in ages:
    print (f"This is the key: {key}")
    print (f"{key} is {ages[key]}")
    x=ages[key]
    print (f"This is the value :{x}")
    if  x >= 50:
        print (f" {key} is over 50 years old")


for colour in colours:
    if colour == 'red':
        print ("Got Red from colours")



for letter in "my_string":
    print (f"{letter}")


list_of_points = [ (1,2) , (2,3) , (3,4)]
for x , y in list_of_points:
    print (f" x: {x} y: {y}")


ages ={'david': 29, 'alex': 50, 'simon': 60}

for name,age in ages.items():
    print (f"Person named : {name}")
    print (f"Age of {age}")

x=ages.items()  # puts into a tuple list
print (f" {x}")
