
# yield will return the value before continue the code 
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create an instance of the Fibonacci sequence generator
fib_gen = fibonacci_sequence()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))
