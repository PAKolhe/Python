# Practical 6
import re

# Define a pattern
pattern = r'appl'

# Define a string to search
text = 'I like apples and oranges.'

# Search for the pattern in the string
match = re.search(pattern, text)

# Check if a match is found
if match:
    print('Pattern found:', match.group())
else:
    print('Pattern not found.')

import re
# Example 1: Matching a pattern in a string
text = "The quick brown fox jumps over the lazy dog"
pattern = r"fox"
if re.search(pattern, text):
 print("Pattern found in text.")
else:
 print("Pattern not found in text.")
# Example 2: Extracting phone number from a string
phone_text = "Call me at 123-456-7890 or 987-654-3210"
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone_list = re.findall(phone_pattern, phone_text)
print("Phone Number found:", phone_list)
