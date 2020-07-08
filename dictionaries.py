#!/usr/local/bin/python3.7


#Dictionaries

#Dictionaries are the main mapping type that we'll use in Python. This object is comparable to a Hash or "associative array" in other languages.

#Things to note about dictionaries:
#
#        Unlike Python 2 dictionaries, as of Python 3.6 keys are ordered in dictionaries. Will need OrderedDict if you want this to work on another version of Python.
#        You can set the key to any IMMUTABLE type (no lists)
#        Avoid using things other than simple objects as keys.
#        Each key can only have one value (so don't have duplicates when creating a dict)
#        We create dictionary literals by using curly braces ({ and }), separating keys from values using colons (:), and separating key/value pairs using commas (,). Here's an example dictionary:


ages ={'david': 29, 'alex': 30}

x=ages['david']
print (f"david age:{x}")

# add an item
ages['trevor'] = 33
x=ages['trevor']
print (f"trevor age:{x}")

# update an item
ages['david'] = 3
x=ages['david']
print (f"david age:{x}")

# remove an item

ages.pop('trevor')
x=ages
print (f"removed trevor from dictionary {x}")

# get a item contents
x= ages.get('alex')
print (f"alex age: {x}")

# get just the keys
x=ages.keys()
print (f"{x}")
x=list(ages.keys()) # put in a list
print (f" put in a list {x}")

# get just the values
x=ages.values()
print (f"{x}")
x=list(ages.values()) # put in a list
print (f" put in a list {x}")

# another way of creating dict
weights=dict(kevin=160, bob=250)




