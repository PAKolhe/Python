from functools import reduce
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]
# Example using map: Multiply each number by 2
mapped_numbers = map(lambda x: x * 2, numbers)
# Example using filter: Filter out even numbers
filtered_numbers = filter(lambda x: x % 2 != 0, numbers)
# Example using reduce: Calculate the product of all numbers
product = reduce(lambda x, y: x * y, numbers)
# Print the results
print("Original numbers:", numbers)
print("Mapped numbers (doubled):", list(mapped_numbers))
print("Filtered numbers (odd numbers only):", list(filtered_numbers))
print("Product of all numbers:", product)
