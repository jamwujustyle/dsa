"""Week 2 (2026-08-31): Recursive digit sum."""


def sum_digits(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


if __name__ == "__main__":
    for n in (1234, 9, 1000, 0):
        print(n, sum_digits(n))
