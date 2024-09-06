def fibonacci(num):
    a, b = 1, 1
    for x in range(num-1):
        a, b = b, a+b
    return a


def fib_(num):
    if num==1 or num==2:
        return 1
    return fib_(num-1) + fib_(num-2)

num = fibonacci(10)
num_ = fib_(10)
print(num, num_)