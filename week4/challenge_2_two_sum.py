"""Week 4 (2026-09-14): Challenge 2 — Two sum using a hash map."""


# Expected time: O(n); auxiliary space: O(n), for n input numbers.
def two_sum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], i]
        seen[value] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
    assert two_sum([], 3) == []
    assert two_sum([3], 6) == []
    print("Challenge 2: all tests passed.")
