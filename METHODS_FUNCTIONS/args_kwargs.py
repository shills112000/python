#!/usr/local/bin/python3.7

def myfuc(a,b):
    # RETURNS 5 % of the sum of a and b
    return sum((a,b)) * 0.05

print(myfuc(40,60))


def myfunc(*args):   # turple of parameters for args
    for item in args:
        print (item)
    return sum(args) * 0.05

print(myfunc(40,60))  # YOU CAN ADD AS MANY ARGS as you want now in a tuple
print(myfunc(40,60,100,100,100,100,100,100))  # YOU CAN ADD AS MANY ARGS as you want now in a tuple


def newfunc(**kwargs):   # KARGS , key,word arguements from a dictionary
    print (kwargs)
    if 'fruit' in kwargs:
        print (f"My fruit of choice is {kwargs['fruit']}")
    else:
        print ('I did not find fruit')

newfunc(fruit='apple',Veggie='tomato')

def both_args_kwargs(*args,**kwargs):
    print (f"I would like {args[0]} {kwargs['food']}")

print(both_args_kwargs(10,20,30,fruit='orange',food='eggs',animal='dog'))
