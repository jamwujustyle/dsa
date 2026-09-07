"""Week 3 (2026-09-07): Tower of Hanoi."""


def hanoi(n, src="A", dst="C", via="B"):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    count = hanoi(n - 1, src, via, dst)
    print(f"{src} -> {dst}")
    count += 1
    count += hanoi(n - 1, via, dst, src)
    return count


if __name__ == "__main__":
    n = 3
    count = hanoi(n)
    print("Moves:", count)
    assert count == 2 ** n - 1
