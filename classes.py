#!/usr/local/bin/python3.7


#https://docs.python.org/3/tutorial/classes.html#classes


# class allows us to define a type that allows functionaility
#defining own types using classes


# camelcase , CarModel
# """ this is documentation uses qutoes to stop and start

# __init__  , recreate a new instance method Dunder method

### OOP allows programmers to create their own objects that have methods and attributes


class Car:
    """
    Car models a car
    """

    def __init__(self, engine, tires, licence):
        self.engine = engine
        self.tires = tires
        self.licence = licence

    def print (self):
        print (self.tires)
        print (self.licence)

# pass just leaves the class
class Dog():
    def __init__(self, breed): # create init method , always called upon when you create a instance of the class
        self.breed = breed

#my_sample = Sample() # create an instance of class sample
my_dog = Dog(breed='woofer')
x=my_dog.breed
print (f"{x}")
