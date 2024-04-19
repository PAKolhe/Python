""" Implement a python program which will read a list of integer numbers. Then it will create a dictionary 
which contains the key: value pair as: key is N and value is the number of negative numbers and the 
second key is P and the value is the number of positive numbers contained in list. (for example List=[ 
9,-3,4,8,-17] the output will be Dlist={ ‘N’:2, ‘P’:3})
"""
def count_numbers(numbers):
    positive_count = 0
    negative_count = 0
    
    # Iterate through the list of numbers
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
            
    # Create and return the dictionary
    count_dict = {'P': positive_count, 'N': negative_count}
    return count_dict

# Read a list of integer numbers from user input
input_list = input("Enter a list of integer numbers separated by space: ").split()
input_list = [int(num) for num in input_list]  # Convert input strings to integers

# Get the count of positive and negative numbers
result_dict = count_numbers(input_list)

# Print the result dictionary
print("Result Dictionary:", result_dict)

"""def count_neg_pos(numbers):
#Function to count the number of negative and positive numbers in a list.
count_neg = sum(1 for num in numbers if num < 0)
count_pos = sum(1 for num in numbers if num > 0)
return {'N': count_neg, 'P': count_pos}
# Read the list of integer numbers
input_list = input("Enter the list of numbers separated by space: ").split()
input_list = [int(x) for x in input_list]
# Call count_neg_pos function
result = count_neg_pos(input_list)
# Print the result dictionary
print("Dictionary containing count of negative and positive numbers:")
print(result)"""