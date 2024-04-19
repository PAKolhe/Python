class Point:
 def __init__(self, x, y):
  self.x = x
  self.y = y
# Overloading the addition operator (+)
def __add__(self, other):
 return Point(self.x + other.x, self.y + other.y)
# Overloading the subtraction operator (-)
def __sub__(self, other):
 return Point(self.x - other.x, self.y - other.y)
# Overloading the equality operator (==)
def __eq__(self, other):
 return self.x == other.x and self.y == other.y
# Overloading the string representation
def __str__(self):
 return f'({self.x}, {self.y})'
# Creating some Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)
# Adding two Point objects using the overloaded '+' operator
sum_point = point1 + point2
print('Sum of points:', sum_point)
# Subtracting two Point objects using the overloaded '-' operator
diff_point = point1 - point2
print('Difference of points:', diff_point)
# Testing equality using the overloaded '==' operator
print('Are the points equal?', point1 == Point(1, 2))
print('Are the points equal?', point1 == Point(3, 4))
