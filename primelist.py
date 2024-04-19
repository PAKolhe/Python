def is_prime(num):
"""
Function to check if a number is prime.
"""
if num <= 1:
 return False
for i in range(2, num):
 if num % i == 0:
  return False
return True
# Read the list of integers from the user
listInt = list(map(int, input("Enter the list of integers separated by space: ").split()))
# Initialize empty lists for prime and non-prime numbers
primeList = []
notPrimeList = []
# Separate prime and non-prime numbers
for num in listInt:
 if is_prime(num):
  primeList.append(num)
else:
 notPrimeList.append(num)
# Print the prime and non-prime lists
print("Prime numbers:", primeList)
print("Non-prime numbers:", notPrimeList)
