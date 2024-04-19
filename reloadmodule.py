# example_module.py
# Initial variable
variable = "Initial value"
def print_variable():
 print("Variable value:", variable)
def change_variable(new_value):
 global variable
 variable = new_value
print("Variable changed to:", variable)
# main_program.py
import example_module
import importlib
def main():
# Print initial variable value
  print("Initial state:")
  example_module.print_variable()
# Change variable value
  example_module.change_variable("New value")
# Print variable value after change
  print("\nState after change:")
  example_module.print_variable()
# Demonstrate module reloading
  print("\nReloading module...")
  importlib.reload(example_module)
# Print variable value after reloading
  print("\nState after reloading:")
  example_module.print_variable()
main()
