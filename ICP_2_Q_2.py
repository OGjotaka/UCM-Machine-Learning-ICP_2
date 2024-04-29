#CS 4710
#JJ Holbrook
#700514202
#ICP 2 Question 2

'''
Use looping to output the elements from a provided list present at odd indexes.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''

# create list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# loop from 0 to length of list
for i in range(len(my_list)):
    # if remainder is not 0 (odd) then print
    if (i % 2 != 0):
        print(my_list[i])
