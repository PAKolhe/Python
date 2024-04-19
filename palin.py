num = str(input("Enter any number"))
if num == num[::-1]:
    print("no is palindrome")
else:
    print("no is not  palindrome")

"""#another code
def is_palindrome(number):
 original_number = number
reversed_number = 0
# Reverse the number
while number > 0:
 digit = number % 10
reversed_number = reversed_number * 10 + digit
  number //= 10
#Check if the original number is equal to its reverse
  return original_number == reversed_number
#Test the function
number = int(input("Enter a number: "))
if is_palindrome(number):
   print(number, "is a palindrome!")
else:
    print(number, "is not a palindrome.")"""
