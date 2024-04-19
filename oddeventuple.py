""" Implement a python program which read integer numbers form user and create a tuple. Then check 
every number in tuple is odd or even. Then replace odd numbers by 0 and even numbers by 1. (for 
example, for input T1= (2,6,7,19,8) then output will be T1= (1,1,0,0,1))
"""
def check_and_replace_numbers(tup):
    new_tup = ()
    
    for num in tup:
        if num % 2 == 0:  # Even number
            new_tup += (1,)
        else:  # Odd number
            new_tup += (0,)
            
    return new_tup

# Read a list of integer numbers from user input
input_list = input("Enter a list of integer numbers separated by space: ").split()
input_list = [int(num) for num in input_list]  # Convert input strings to integers

# Convert the list to a tuple
input_tuple = tuple(input_list)

# Check and replace numbers in the tuple
result_tuple = check_and_replace_numbers(input_tuple)

# Print the result tuple
print("Result Tuple:", result_tuple)

"""def check_replace(numbers):
#Function to check each number in the tuple and replace odd numbers with 0 and even numbers with 1
replaced_tuple = tuple(0 if num % 2 != 0 else 1 for num in numbers)
return replaced_tuple
# Read the tuple of integer numbers from the user
input_tuple = tuple(input("Enter the tuple of numbers separated by space: ").split())
input_tuple = [int(x) for x in input_tuple]
# Call check_replace function
result = check_replace(input_tuple)
# Print the result tuple
print("Tuple after replacing odd numbers with 0 and even numbers with 1:")
print(result)"""
