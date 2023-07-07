

# def fibonacci_sequence():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# fib_gen = fibonacci_sequence()


# for _ in range(10):
#     print(next(fib_gen))




def to():
    n=1 
    while n<=5:
        s=n*n
        yield s
        n+=1
values=to()

for i in values:
    print(i)