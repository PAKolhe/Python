def check_replace(numbers):
#Function to check each number in the tuple and replace odd numbers with 0 and even numbers with 1
 replaced_tuple = tuple(0 if num< 0 else 1 for num in numbers)
 return replaced_tuple
# Read the tuple of integer numbers from the user
input_tuple = tuple(input("Enter the tuple of numbers separated by space: ").split())
input_tuple = [int(x) for x in input_tuple]
# Call check_replace function
result = check_replace(input_tuple)
# Print the result tuple
print("Tuple after replacing odd numbers with 0 and even numbers with 1:")
print(result)
