""" Implement a Python program to demonstrate use of class method, static method and instance 
method"""

class MyClass:
    class_variable = "Class Variable"
    
    def __init__(self, value):
        self.instance_variable = value
        
    def instance_method(self):
        print(f"Instance method. Instance var: {self.instance_variable}")
        
    def class_method(cls):
        print(f"Class method. Class var: {cls.class_variable}")
        
    def static_method():
        print("Static method. No access to instance or class vars.")

# Create instance
obj = MyClass("Value")

# Call instance method
obj.instance_method()

# Call class method
MyClass.class_method(MyClass)

# Call static method
MyClass.static_method()

"""class MyClass:
 class_variable = 10
def __init__(self, value):
 self.instance_variable = value
def instance_method(self):
 print("This is an instance method")
print("Instance variable value:", self.instance_variable)
@classmethod
def class_method(cls):
 print("This is a class method")
print("Class variable value:", cls.class_variable)
@staticmethod
def static_method():
 print("This is a static method")
# Creating an instance of MyClass
obj = MyClass(20)
# Calling instance method
obj.instance_method()
# Calling class method
MyClass.class_method()
# Calling static method
MyClass.static_method()"""