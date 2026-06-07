a = complex(8,9)
b = True
c = "Hello, World!"
d = 3.14
print(a)
print(b)
a1 = 89
print(a+a1)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))


# Lists are built-in data type in python that can be used to store mutiple items in a single variable. 
# Lists are ordered, changeable, and allow duplicate values.
# They are defined using square brackets [].
list1 = [8, 2.3, [-4,5],["apple", "banana"], True]
print(list1)
print("The type of list1 is ", type(list1))


# Tuple are same as list but they are immutable, which means that once a tuple is created, 
# its elements cannot be modified.
tuple1 = (8, 2.3, (-4,5),("apple", "banana"), True)
print(tuple1)
print("The type of tuple1 is ", type(tuple1))


'''Dict: Adictionary is an unordered collection of data contaning a key:value pair 
   are enclosed within curly braces {}.'''
dict1 = {"name": "Arjrun", "age": 20, "can_vote": True}
print(dict1)
print("The type of dict1 is ", type(dict1))