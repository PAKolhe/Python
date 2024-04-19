class Animal:
"""
Base class representing an animal.
"""
def __init__(self, name):
 self.name = name
def sound(self):
"""
Method to make a sound.
"""
print(f"{self.name} makes a sound.")
class Dog(Animal):
"""
Derived class representing a dog.
"""
def __init__(self, name, breed):
 super().__init__(name)
self.breed = breed
def bark(self):
"""
Method for a dog to bark.
"""
print(f"{self.name} the {self.breed} barks.")
class Cat(Animal):
"""
Derived class representing a cat.
"""
def __init__(self, name, color):
 super().__init__(name)
self.color = color
def meow(self):
"""
Method for a cat to meow.
"""
print(f"{self.name} the {self.color} cat meows.")
# Create instances of derived classes
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "white")
# Call methods of derived classes
dog.bark()
cat.meow()
# Call method from the base class
dog.sound()
cat.sound()