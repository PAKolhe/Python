class Car:
# Class attribute
 car_count = 0
def __init__(self, brand, model):
# Instance attributes
 self.brand = brand
 self.model = model
# Incrementing the class attribute car_count
Car.car_count += 1
def display_info(self):
 print(f"Brand: {self.brand}, Model: {self.model}")
# Creating instances of Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")
# Displaying information about each car
print("Information about car1:")
car1.display_info()
print()
print("Information about car2:")
car2.display_info()
print()
print("Information about car3:")
car3.display_info()
print()
# Displaying the total count of cars using the class attribute
print("Total number of cars:", Car.car_count)
