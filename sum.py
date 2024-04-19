def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print("Sum of numbers:", sum_of_numbers(numbers))

"""def difference_odd_even_digits(num):
# Convert the number to a string to iterate through its digits
 num_str = str(num)
# Initialize variables to store the sums of odd and even digits
sum_odd = 0
sum_even = 0
# Iterate through each digit in the number
for digit in num_str:
# Convert the digit back to an integer
 digit_int = int(digit)
# Check if the digit is odd
if digit_int % 2 != 0:
 sum_odd += digit_int
# Otherwise, the digit is even
else: 
 sum_even += digit_int
# Calculate the difference between the sums of odd and even digits
difference = sum_odd - sum_even
return difference
# Example usage
number = int(input("Enter a number: "))
result = difference_odd_even_digits(number)"""
print("Difference between sums of odd and even digits:", result)"""