def linear_search(string, char):
#Function to perform linear search to find a character within a string.
 for i, ch in enumerate(string):
  if ch == char:
   return i
   return -1
input_string = input("Enter the string: ")
input_char = input("Enter the character to search for: ")
# Perform linear search
index = linear_search(input_string, input_char)
# Print the result
if index != -1:
 print(f"Character '{input_char}' found at index {index}.")
else:
 print(f"Character '{input_char}' not found in the string.")
