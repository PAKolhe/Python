"""Implement a Python program to find all prime numbers between 100 and 500."""
def isprime(num):
    for i in range (2, int (num ** 0.5)+1):
        if( num %i == 0):
            return False
    return True
pm =[ num for num in range( 100, 501) if isprime(num)]
print(pm) 
  