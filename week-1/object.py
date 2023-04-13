# This is Advanced Python Course for Everything is Object topic

x = 13 # this is built-in data type but have you ever think that x is object?

# in python if you want to know what is the type of variable you can use type() function
# So let's use type() function to know what is the type of x
print(type(x)) # output: <class 'int'>

# how about if we want to know what is the type of type() function?
print(type(type(x))) # output: <class 'type'>

# Amazing right? type() function is also object

# Let's see more example

string = "Hello World"
print(type(string)) # output: <class 'str'>

# So string is also object

# So everything in python is object

# Let's see create an object

class Person:
    pass

print(type(Person)) # output: <class 'type'>

# How can we check the object is instance of class?

print(isinstance(Person, type)) # output: True

# What about comparing to object instance?
print(isinstance(Person(), type)) # output: False

# See when we use Person() it will create an object instance

print(isinstance(Person(), Person)) # output: True

# Generally we use isinstance() function to check the object is instance of class

# Summary

# - Everything in python is object
# - type() function is also object
# - isinstance() function is used to check the object is instance of class
# - when you create class it will inherit from type class
# - deep down everything is object and literally everything


