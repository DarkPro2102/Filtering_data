# Filtering_data

This is a filtering data mini project that uses list comprehension and high order functions solutions, both of them filtering the same data from a list of dictionaries. 

The project was intended to an [Intermidiate Python course](https://platzi.com/clases/python-intermedio/ "Intermidiate Python course") from Platzi.

For the list comprehension solutions, it is important to learn how to read the new list created, as well as correctly saying which is your iterable dataset. 

An example to show how list comprehension is read is: 

```Python
squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)
```

Where "squares" is a new list generated from the input sequence, which is the for loop, acomplishing the condition given after the loop, and filling the list with the "i" iterator value. 

And for the high order functions solution, I am only using "filter" and "map". Both functions receive lambda functions as their first parameter followed by the iterable dataset as you can see below: 

```Python
# Filter function
my_list = [1,4,5,6,9,13,19,21]
odd_filter = list(filter(lambda x: x%2 != 0, my_list))
print(odd_filter)

# Map function
my_list_map = [1,2,3,4,5]
square_map = list(map(lambda x: x**2, my_list))
print(square_map)
```

## Dependencies: 
* Python 3.9.0



