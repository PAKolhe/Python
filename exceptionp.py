"""def example_raise_exception():

#Function to demonstrate exception handling using raise statement.

try:
 raise ValueError("This is a custom ValueError raised using raise statement.")
except ValueError as ve:
 print("Caught ValueError:", ve)
def example_assert_statement(x):

#Function to demonstrate exception handling using assert statement.

try:
assert x >= 0, "x should be non-negative"
print("x is:", x)
except AssertionError as ae:
print("AssertionError:", ae)
def example_multiple_exceptions():

#Function to demonstrate catching multiple specific exceptions.

try:
# Trying to open a non-existent file
with open("nonexistent.txt", "r") as file:
content = file.read()
# Trying to convert a string to an integer
int("abc")
except FileNotFoundError:
print("FileNotFoundError: The file does not exist.")
except ValueError:
print("ValueError: Could not convert the string to an integer.")
except Exception as e:
print("An unexpected error occurred:", e)
print("Example: Raise Statement")
example_raise_exception()
print("\nExample: Assert Statement")
example_assert_statement(-1)
print("\nExample: Catch Multiple Specific Exceptions")
example_multiple_exceptions()"""
