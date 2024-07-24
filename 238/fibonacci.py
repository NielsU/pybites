def fib(n):
    if n < 0:
        raise ValueError
    elif n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)



'''to generate some test data''''
params = ""

for i in range(20):
    params += f",({i},{fib(i)})"


print(params)
