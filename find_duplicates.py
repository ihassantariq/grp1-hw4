import pandas as pd
import collections
import numpy

# use chunk size 500
c_size = 10

txt_file = "passwords2.txt"
# load the big file in smaller chunks
# i = 0
# for line in open(txt_file):
#     if i == c_size:
#         break
#     password = line.strip()
#     print(password + "Count: " + str(len(password)))
#     i += 1


def hash_function_with_weighting(password, table_size, INITIAL_VALUE = 5381, M = 33 ):
    hash_value = INITIAL_VALUE;
    m = M
    for i in range(len(password)):
        hash_value =  m * hash_value + i * ord(password[i])
    return hash_value % table_size

table_size = ord('z') * 2  # considering we have 20 character password
hash_table =[] # we will use chaining technique for hash table values
passwords = ["ab","cd","ef","ef","fe"] # open_file_and_return_passwords(txt_file, c_size)

for i in range(table_size):
    hash_table.append({})

i = 0
for password in passwords:
    table_index = hash_function_with_weighting(password, table_size)
    if password not in hash_table[table_index].keys():
        hash_table[table_index][password] = 0
    hash_table[table_index][password] = hash_table[table_index][password] + 1
    i = i+1

# number of duplicates
duplicates = 0 # this duplicate consider that we have total duplicate item adding both number of duplicates
# which can be more than 1
for item in hash_table:
    i = 0
    for key, value in item.items(): # dictionary item should have only one item otherwise they are false positive
        if(value > 1):
            duplicates += (value - 1) # removing 1 if only one count then that is not duplicate
    #if (len(item.items()) > 1):
        #duplicates += (len(item.items()) - 1)  # removing 1 if only one count then that is not duplicate
duplicates

def open_file_return_passwords(file_name, number_of_lines = 10000, starting_index = 0, consider_size = True):
    i = 0
    c_size = number_of_lines
    p_items = []
    if(starting_index > 0):
        number_of_lines +=  starting_index
    for line in open(txt_file):
        if i == c_size and consider_size:
            break
        password = line.strip()
        if not starting_index > i:
            p_items.append(password)
        i += 1
    return p_items


# Part 1
# I am considering order does not matter


# Part 2
# Use a hash function to map the number to a large range.
# Read the class material and search the internet for
# this part (but you need to write the code yourself).
# http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html


