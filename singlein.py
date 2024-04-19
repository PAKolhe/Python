class Animal:
 def __init__(self, name):
  self.name = name
def speak(self):
 print(f"{self.name} makes a sound")
class Dog(Animal):
 def __init__(self, name):
  super().__init__(name)
def speak(self):
 print(f"{self.name} says Woof!")
class Cat(Animal):
 def __init__(self, name):
  super().__init__(name)
def speak(self):
 print(f"{self.name} says Meow!")
# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")
# Calling speak() method for Dog and Cat
dog.speak()
cat.speak()
