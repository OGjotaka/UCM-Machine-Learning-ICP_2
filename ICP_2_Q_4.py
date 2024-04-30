#CS 4710
#JJ Holbrook
#700514202
#ICP 2 Question 4

'''
Write a function that takes a list and returns a new list with unique items of the first list.
Sample List: [1,2,3,3,3,3,4,5]
Unique List: [1, 2, 3, 4, 5]
'''

# create list and print
def main():
    my_list = [1, 2, 3, 3, 3, 3, 4, 5]
    print(unique(my_list))

# find unique items from a list and return new list of unique items
def unique(my_list):
    my_list_unique = []
    for i in range(len(my_list)):
        if my_list[i] not in my_list_unique:
            my_list_unique.append(my_list[i])

    return my_list_unique

# execute the main function
main()



