def add(a, b):
#Function to add two numbers.
 return a + b
def add_three(a, b, c=0):
#Function to add three numbers.
 return a + b + c
# Test the overloaded add function
print("Result of add(2, 3):", add(2, 3))
print("Result of add_three(2, 3, 4):", add_three(2, 3, 4))
print("Result of add_three(2, 3):", add_three(2, 3))