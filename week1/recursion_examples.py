"""Week 1 (2026-08-24): Recursion fundamentals."""


def string_length(text, i=0):
    if i == len(text):
        return 0
    return 1 + string_length(text, i + 1)


def power(x, n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return x * power(x, n - 1)


def fast_power(x, n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    half = fast_power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return x * half * half


def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fib(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_memo(n, memo=None):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_loop(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print("Length:", string_length("hello"))
    print("Power:", power(5, 3), fast_power(5, 3))
    print("Factorial:", factorial(4))
    print("Fibonacci:", fib(10), fib_memo(10), fib_loop(10))
