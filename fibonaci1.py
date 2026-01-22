def Fibonacci(n: int, flag: bool):
    if flag is True:
        return fib_recursive(n)
    else:
        raise ValueError("flag must be True for recursive implementation")


def fib_recursive(n: int):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)