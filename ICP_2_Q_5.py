#CS 4710
#JJ Holbrook
#700514202
#ICP 2 Question 5

'''
Write a function that accepts a string and calculate the number of upper-case letters and lower-case
letters.
Input String: 'The quick Brow Fox'
Expected Output:
No. of Upper-case characters: 3
No. of Lower-case Characters: 12
'''

def find_uppercase(my_string):
    print("Uppercase Letters: ", sum(1 for c in my_string if c.isupper()))

def find_lowercase(my_string):
    print("Lowercase Letters: ", sum(1 for c in my_string if c.islower()))

def main():
    my_string = input("Enter the sentance: ")
    find_uppercase(my_string)
    find_lowercase(my_string)

main()
