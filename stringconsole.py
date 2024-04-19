def count_characters(input_string):
# Create an empty dictionary to store character counts
 char_count = {}
# Iterate through each character in the input string
for char in input_string:
# If the character is already in the dictionary, increment its count
 if char in char_count:
  char_count[char] += 1
# Otherwise, add the character to the dictionary with a count of 1
else:
 char_count[char] = 1
# Print the character counts
for char, count in char_count.items():
 print(f"Character '{char}' occurs {count} time(s)")
# Get input string from the user
input_string = input("Enter a string: ")
# Call the function to count and print character occurrernces