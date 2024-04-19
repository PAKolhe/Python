class Animal:
 def __init__(self, name):
  self.name = name
def speak(self):
 pass
class Dog(Animal):
 def speak(self):
  return f"{self.name} says Woof!"
class WorkingDog(Dog):
 def work(self):
  return f"{self.name} is working."
class GuardDog(WorkingDog):
 def guard(self):
  return f"{self.name} is guarding."
# Create instances of each class
dog = Dog("Buddy")
working_dog = WorkingDog("Max")
guard_dog = GuardDog("Rocky")
# Demonstrate multilevel inheritance by calling methods of each instance
print(dog.speak()) # Output: Buddy says Woof!
print(working_dog.speak()) # Output: Max says Woof!
print(working_dog.work()) # Output: Max is working.
print(guard_dog.speak()) # Output: Rocky says Woof!
print(guard_dog.work()) # Output: Rocky is working.
print(guard_dog.guard()) # Output: Rocky is guarding.