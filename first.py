"""Implement a Python program to find all the numbers divisible by 7 but are not multiple of 5, between 
the range 2000 to 3000. """
# Using list comprehension
numbers = [num for num in range(2000, 3001) if num % 7 == 0 and num % 5 != 0]

# Printing the numbers
print(numbers)

