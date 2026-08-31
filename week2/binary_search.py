"""Week 2 (2026-08-31): Recursive binary search."""


def bsearch(a, key, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == key:
        return mid
    if key < a[mid]:
        return bsearch(a, key, lo, mid - 1)
    return bsearch(a, key, mid + 1, hi)


if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10]
    print(bsearch(numbers, 8))
    print(bsearch(numbers, 5))
