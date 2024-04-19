class MyClass:
 class_variable = "This is a class variable"
def __init__(self, name):
 self.name = name
 self.instance_variable = "This is an instance variable"
def instance_method(self):
 local_variable = "This is a local variable"
print("Inside instance method:")
print("Class variable:", MyClass.class_variable)
print("Instance variable:", self.instance_variable)
print("Local variable:", local_variable)
print("Name:", self.name)
def main():
# Creating an object of MyClass
 obj = MyClass("John")
# Accessing instance method of MyClass
 obj.instance_method()
# Accessing class variable directly using class name
print("\nAccessing class variable directly using class name:")
print("Class variable:", MyClass.class_variable)
main()
