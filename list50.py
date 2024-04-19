def count_less_than_or_equal_to_50(lst):
 count = 0
 for num in lst:
  if num <= 50:
   count += 1
 return count
# Read a list of numbers from the user
lst = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
# Call the function to count numbers less than or equal to 50
count = count_less_than_or_equal_to_50(lst)
# Print the count
print("Number of elements less than or equal to 50:", count)
