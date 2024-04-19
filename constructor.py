class MyClass:
 def __init__(self, name):
  self.name = name
 print(f"Initializing object {self.name}")
def some_method(self):
 print(f"Doing something with object {self.name}")
def __del__(self):
 print(f"Destructing object {self.name}")
# Creating instances of MyClass
obj1 = MyClass("obj1")
obj2 = MyClass("obj2")
# Calling a method of the objects
obj1.some_method()
obj2.some_method()
# Deleting objects explicitly
del obj1
del obj2
