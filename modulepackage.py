# module1.py
def public_function():
 print("This is a public function in module1.")
def _private_function():
 print("This is a private function in module1.")
public_variable = "This is a public variable in module1."
_private_variable = "This is a private variable in module1."
# module2.py
def public_function():
 print("This is a public function in module2.")
def _private_function():
 print("This is a private function in module2.")
public_variable = "This is a public variable in module2."
_private_variable = "This is a private variable in module2."
# main_script.py
from my_package import module1, module2
# Accessing public functions and variables
module1.public_function()
module2.public_function()
print(module1.public_variable)
print(module2.public_variable)
# Attempting to access private functions and variables
# Note: This will raise AttributeError since private members are not accessible outside the modules they
belong to.
module1._private_function()
module2._private_function()
print(module1._private_variable)
print(module2._private_variable)
