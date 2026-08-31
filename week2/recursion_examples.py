"""Week 2 (2026-08-31): Tail and mutual recursion."""


def sum_tail(n, total=0):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return total
    return sum_tail(n - 1, total + n)


def sum_loop(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


def is_even(n):
    if n < 0:
        n = -n
    if n == 0:
        return True
    return is_odd(n - 1)


def is_odd(n):
    if n < 0:
        n = -n
    if n == 0:
        return False
    return is_even(n - 1)


def square(n):
    if n < 0:
        n = -n
    if n == 0:
        return 0
    return square(n - 1) + 2 * n - 1


def square_indirect(n):
    if n < 0:
        n = -n
    if n == 0:
        return 0
    return product(n) + n


def product(n):
    return square_indirect(n - 1) + n - 1


if __name__ == "__main__":
    print("Sum:", sum_tail(5), sum_loop(5))
    print("Parity:", is_even(6), is_odd(7))
    print("Square:", square(3), square_indirect(3))
