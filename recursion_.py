# recursion if a function call itself it is known recursion
import time


def fact(n):
    if n < 1:
        return 1
    return n * fact(n-1)


start_time = time.time()
print(fact(900))
print(time.time() - start_time)

start_time = time.time()
prod = 1
for i in range(1, 901):
    prod = prod * i
print(prod)
print(time.time() - start_time)


# merge sort code

# fabonacci