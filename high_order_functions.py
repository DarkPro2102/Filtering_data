# Filter function
# Example using list comprehension

# my_list = [1,4,5,6,9,13,19,21]
# odd = [i for i in my_list if i%2!=0]
# print(odd)

## Now, we use filter function 

# odd_filter = list(filter(lambda x: x%2 != 0, my_list))
# print(odd_filter)

#---------------------------------#-------------------#
# Map function
# Example using list comprehension

# my_list = [1,2,3,4,5]
# square = [i**2 for i in my_list]
# print(square)

# # Now, using map function

# square_map = list(map(lambda x: x**2, my_list))
# print(square_map)

#---------------------------------#--------------------------#
# Reduce function
# We have to import reduce from functools

# from functools import reduce

# my_list = [2,2,2,2,2]

# all_multiplied = reduce(lambda a,b: a * b, my_list)
# print(all_multiplied)

# # In case we want to use a for loop: 

# all_multi = 1

# for i in my_list:
#     all_multi = all_multi * i

# print(all_multi)