#CS 4710
#JJ Holbrook
#700514202
#ICP 2 Question 3

'''
Write a code that appends the type of elements from a given list.
Input
x = [23, ‘Python’, 23.98]
Expected output
[23, 'Python', 23.98]
[<class 'int'>, <class 'str'>, <class 'float'>]
'''

# create list
x = [23, "Python", 23.98]

# create list to hold types
x_types = [None] * len(x)

# print list and types
for i in range(len(x)):
    x_types[i] = type(x[i])
    print(x[i])
    print(x_types[i])
