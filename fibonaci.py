def fibonacci_series(n):
 fib_series = []
a, b = 0, 1
for _ in range(n):
  fib_series.append(a)
a, b = b, a + 
 return tuple(fib_series)
# Input the number of terms in the Fibonacci series
num_terms = int(input("Enter the number of terms for Fibonacci series: "))
# Calculate Fibonacci series and store it in a tuple
fibonacci_tuple = fibonacci_series(num_terms)
# Print the Fibonacci series stored in the tuple
print("Fibonacci Series:")
print(fibonacci_tuple)
