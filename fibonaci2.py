def Fibonacci(n: int, flag: bool):
    if flag is False:
        return fib_loop(n)
    else:
        raise ValueError("flag must be False for loop implementation")


def fib_loop(n: int):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b