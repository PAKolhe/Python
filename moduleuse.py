#MODULE
# math_operations.py
def add(a, b):
 return a + b
def subtract(a, b):
 return a - b
def multiply(a, b):
 return a * b
def divide(a, b):
 if b != 0:
  return a / b
 else:
  return "Error: Division by zero"
# main.py
import math_operations
# Using the functions from math_operations module
result1 = math_operations.add(5, 3)
result2 = math_operations.subtract(10, 4)
result3 = math_operations.multiply(6, 7)
result4 = math_operations.divide(15, 5)
# Displaying the results
print("Result of addition:", result1)
print("Result of subtraction:", result2)
print("Result of multiplication:", result3)
print("Result of division:", result4